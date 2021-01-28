import requests
import base64

'''通用文字识别（高精度版）'''
AK='vCHpWwvTMTaH0he7W71GkWEQ'
SK='37N6MvoUx5QfyczrUa9q7jvjL8OEc0GC'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'%(AK,SK)
response = requests.get(host)

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# 二进制方式打开图片文件
f = open('1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = response.json()['access_token']
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
	doc = open('out.txt','w')
	print(response.json())
	print(response.json(),file=doc)
	doc.close()
