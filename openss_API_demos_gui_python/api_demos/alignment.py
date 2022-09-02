# -*- coding: utf-8 -*-

"""
Facial keypoints detect case
"""
import json
import os

import requests

from . import editimage
from . import utils

# Authentication token request urlq
token_url = "http://eco-open.study.sensetime.com/api/common/v1/token"
# Facial keypoints detect request url
alignment_url = "https://eco-open.study.sensetime.com/api/internal_sdk/v1/alignment"
# Image resource
file_name = "capture.jpeg"
file_path = os.path.join(".", file_name)

def main(ACCESS_KEY_ID, ACCESS_KEY_SECRET):
    # obtain authentication token
    headers = {"languageType": "en"}
    token_params = {"accessKeyId":ACCESS_KEY_ID, "accessKeySecret":ACCESS_KEY_SECRET}
    token_response = requests.get(url=token_url, headers=headers, params=token_params, verify=False).text
    token = json.loads(token_response).get("data")

    # takes picture from face cam
    editimage.camCapture(file_path)

    # ensure token is valid (crash prevention)
    if not token:
        print("failed to obtain authentication token")
    else:
        # request headers
        headers = {"languageType": "en", "X-Authorization": token}
        # request parameters
        params = {"rotateDegree": 0, "modelType": 0, "isResponseImageRequired": False}

        # to be set up in a config file
        use_binary = False

        if use_binary:
            binary_files = {'file': (file_name, open(file_path, 'rb'))}
            response = requests.post(url=alignment_url, headers=headers, data=params, files=binary_files, verify=False).text
            response = json.loads(response)
            print(json.dumps(response, ensure_ascii=False))
        else:
            base64_img = utils.img_to_base64(file_path)
            base64_files = {'base64Image': (None, base64_img)}
            response = requests.post(url=alignment_url, headers=headers, data=params, files=base64_files, verify=False).text
            response = json.loads(response)
            print(json.dumps(response, ensure_ascii=False))

        # If isResponseImageRequired is set to True, store the processed image
        # If isResponseImageRequired is set to False, returns a 3d array containing all the points-
        # -in format of [[x1, y1], [x2, y2], [x3, y3], ...]

        response_data = response.get('data')
        points3d_array = []
        if response_data:
            base64_img_data = response_data.get('base64ImageDst')
            point_list_data = response_data["faceKeyCoordinates"]["point3dList"]
            if base64_img_data and base64_img_data != '':
                utils.base64_to_img(base64_img_data, utils.get_current_timestamp() + ".jpg")
            else:
                for i in point_list_data:
                    points3d_array.append([int(i["x"]), int(i["y"])])
                editimage.showPointImage(file_path, points3d_array)
    return False