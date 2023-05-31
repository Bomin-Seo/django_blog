import requests

HOST = 'http://127.0.0.1:8000'
res = requests.post(HOST + '/api-token-auth/', {
    'username':'seo78200','password':'sb159753',
    })
res.raise_for_status()
token = res.json()['token']
print(token)

headers = {'Authorization' : 'JWT ' + token, 'Accept' : 'application/json'}

data = {
    'title' : '제목 by code',
    'text' : 'API내용 by code',
    'created_date' : '2023-05-31',
    'published_date' : '2023-05-31'
}
file = {'image' : open('/Users/sbm78/pic.jpg', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers)
print(res)
print(res.json())