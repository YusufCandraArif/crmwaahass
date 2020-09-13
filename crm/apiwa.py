"""
https://wablas.com/api/send-message
header:
- Authorization = {api-token}
body:
- phone (mandatory)
- message (mandatory)
- type (optional)

https://wablas.com/api/send-image
header:
- Authorization = {api-token}
body:
- phone (mandatory)
- caption (mandatory)
- image (mandatory)
- type (optional)

import requests

headers = {'Authorization': 'token'}
payload = {'phone': '081xxxxx', 'message': 'hello world'}

r = requests.post("https://wablas.com/api/send-message", data=payload, headers=headers)
"""
import requests

def send_whatsapp(message, media_url, choices, phone, token_api, server_address):
    print(message, media_url, choices, phone, token_api, server_address)
    # headers = {'Authorization': 'IL4Ab7MXA8JmMcbE88DGydVoApfSy2ezAW1l5OISz1HQjzwzMOX8k3Dd7qmHZ8ha'}
    headers = {'Authorization': token_api}
    if choices == 'Image Text':
        payload = {'phone': phone,'caption': message,'image':media_url}
        type_msg = 'send-image'
    elif choices == 'Text Only':
        payload = {'phone': phone,'message': message}
        type_msg = 'send-message'
    elif choices == 'Video':
        payload = {'phone': phone,'caption': message,'video':media_url}
        type_msg = 'send-video'
    elif choices == 'Document':
        payload = {'phone': phone,'caption': message,'document':media_url}
        type_msg = 'send-document'
    else:
        type_msg = ""

    if type_msg:
        # url = "https://selo.wablas.com/api/{}".format(type_msg)
        url = "https://{}/api/{}".format(server_address, type_msg)
        r = requests.post(url, data=payload, headers=headers)
        print("send type: ", type_msg)
        print(r.status_code)
        status = str(r.status_code)
        if status == '200':
            return True
        else:
            return False
    else:
        return False

# https://selo.wablas.com/api/send-video?phone=082221810304&video=https://dewatemplate.com/wp-content/uploads/2020/08/buat_upload_test_wa_video.mp4&caption=test
