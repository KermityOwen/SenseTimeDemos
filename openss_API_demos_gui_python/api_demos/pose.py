# -*- coding: utf-8 -*-

"""
Human Pose Recognition case
"""

# Native python imports
import json
import os

# External dependencies
import requests

# Local imports
from . import utils, editimage

# Authentication token request url
token_url = "http://eco-open.study.sensetime.com/api/common/v1/token"
# Human Pose Recognition request url
url = "https://eco-open.study.sensetime.com/api/internal_sdk/v1/pose/recognition"
# Image resource
file_name = "capture.jpeg"
file_path = os.path.join(".", file_name)

def main(ACCESS_KEY_ID, ACCESS_KEY_SECRET):
    editimage.camCapture(file_path)

    # obtain authentication token
    headers = {"languageType": "en"}
    token_params = {"accessKeyId":ACCESS_KEY_ID, "accessKeySecret":ACCESS_KEY_SECRET}
    token_response = requests.get(url=token_url, headers=headers, params=token_params, verify=False).text
    token = json.loads(token_response).get("data")

    if not token:
        print("failed to obtain authentication token")
    else:
        # request headers
        headers = {"languageType": "en", "X-Authorization": token}
        # request parameters
        params = {"isResponseImageRequired": False}

        use_binary = True

        if use_binary:
            binary_files = {'file': (file_name, open(file_path, 'rb'))}
            response = requests.post(url=url,headers=headers, data=params,files=binary_files,verify=False).text
            response = json.loads(response)
            print(json.dumps(response, ensure_ascii=False))
        else:
            base64_img = utils.img_to_base64(file_path)
            base64_files = {'base64Image': (None,base64_img)}
            response = requests.post(url=url, headers=headers, data=params, files=base64_files, verify=False).text
            response = json.loads(response)
            print(json.dumps(response, ensure_ascii=False))

        # If isResponseImageRequired is set to True, store the processed image
        response_data = response.get('data')
        area_points_data = response_data["poseRecognitionList"]
        if response_data:
            area_points_array = []
            pose_points_array = []
            for i in area_points_data:
                aBounds = i["targetDetectResult"]["area"]
                area_points_array.append([[aBounds["left"], aBounds["top"]], [aBounds["right"], aBounds["top"]],
                                       [aBounds["right"], aBounds["bottom"]], [aBounds["left"], aBounds["bottom"]],
                                       [aBounds["left"], aBounds["top"]]])
                pose_points_array.append(i["recognitionResult"])

            print("area_points_array")
            editimage.showPoseImage(file_path, area_points_array, pose_points_array)