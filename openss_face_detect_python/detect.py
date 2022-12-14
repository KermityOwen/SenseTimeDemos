# -*- coding: utf-8 -*-

"""
Image Face Detection case
"""
import json
import os

import requests

import editimage
import utils

# Authentication token request url
token_url = "http://eco-open.study.sensetime.com/api/common/v1/token"
# Image face fetection request url
url = "https://eco-open.study.sensetime.com/api/internal_sdk/v1/detect/face"
# API calling access key
ACCESS_KEY_ID = "PQT7s9q3sWUJkXho";
ACCESS_KEY_SECRET = "m3Jw2qq0AwGtNZo8ZvfezpZeJAvGpgZE";
# Image resource
file_name = "capture.jpeg"
file_path = os.path.join(".", file_name)

editimage.camCapture(file_path)

# obtain authentication token
headers = {"languageType": "en"}
token_params = {"accessKeyId": ACCESS_KEY_ID, "accessKeySecret": ACCESS_KEY_SECRET}
token_response = requests.get(url=token_url, headers=headers, params=token_params, verify=False).text
token = json.loads(token_response).get("data")

if not token:
    print("failed to obtain authentication token")
else:
    # request headers
    headers = {"languageType": "en", "X-Authorization": token}
    # request parameters
    params = {"modelType": 2, "isResponseImageRequired": False}

    use_binary = True

    if use_binary:
        binary_files = {'file': (file_name, open(file_path, 'rb'))}
        response = requests.post(url=url, headers=headers, data=params, files=binary_files, verify=False).text
        response = json.loads(response)
        print(json.dumps(response, ensure_ascii=False))
    else:
        base64_img = utils.img_to_base64(file_path)
        base64_files = {'base64Image': (None, base64_img)}
        response = requests.post(url=url, headers=headers, data=params, files=base64_files, verify=False).text
        response = json.loads(response)
        print(json.dumps(response, ensure_ascii=False))

# If isResponseImageRequired is set to True, store the processed image
response_data = response.get('data')
points_3d_array = []
if response_data:
    base64_img_data = response_data.get('base64ImageDst')
    point_list_data = response_data["targetList"]  # short for point list data
    if base64_img_data and base64_img_data != '':
        utils.base64_to_img(base64_img_data, utils.get_current_timestamp() + ".jpg")
    else:
        for i in point_list_data:
            aBounds = i.get("area")
            points_3d_array.append([[aBounds["left"], aBounds["top"]], [aBounds["right"], aBounds["top"]],
                                   [aBounds["right"], aBounds["bottom"]], [aBounds["left"], aBounds["bottom"]],
                                   [aBounds["left"], aBounds["top"]]])
        editimage.editShowImage(file_path, points_3d_array)
    #print(points_3d_array)
