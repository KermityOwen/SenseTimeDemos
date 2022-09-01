# -*- coding: utf-8 -*-

"""
Face Comparison case
"""
import json
import os

import requests

import utils
import editimage

# Authentication token request url
token_url = "http://eco-open.study.sensetime.com/api/common/v1/token"
# Face Comparison request url
url = "https://eco-open.study.sensetime.com/api/internal_sdk/v1/face/compare"
# API calling access key
ACCESS_KEY_ID = "PQT7s9q3sWUJkXho";
ACCESS_KEY_SECRET = "m3Jw2qq0AwGtNZo8ZvfezpZeJAvGpgZE";
# Image resources
file_name_1 = "capture1.jpeg"
file_path_1 = os.path.join(".", file_name_1)
file_name_2 = "capture2.jpeg"
file_path_2 = os.path.join(".", file_name_2)

editimage.camCapture(file_path_1)
editimage.camCapture(file_path_2)

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
    params = {'garble':False}

    use_binary = True

    if use_binary:
        binary_files = [('files', (file_name_1, open(file_path_1, 'rb'))), ('files', (file_name_2, open(file_path_2, 'rb')))]
        response = requests.post(url=url, headers=headers, data=params, files=binary_files, verify=False).text
        response = json.loads(response)
        print(json.dumps(response, ensure_ascii=False))
    else:
        base64_img_1 = utils.img_to_base64(file_path_1)
        base64_img_2 = utils.img_to_base64(file_path_2)
        base64_img = base64_img_1 + b"&" + base64_img_2
        base64_files = {'base64Image':(None, base64_img)}
        response = requests.post(url=url, headers=headers, data=params, files=base64_files, verify=False).text
        response = json.loads(response)
        print(json.dumps(response, ensure_ascii=False))

    response_data = response.get("data")
    editimage.drawCompare(file_path_1, file_path_2, response_data)