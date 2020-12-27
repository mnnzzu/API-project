import urllib.request #python에서 브라우저 없이 http 프로토콜에 따라서 서버 요청/응답을 할 수 있도록 도와주는 것
client_id = "GZajzk2Q51yChHZGUAlz"
client_secret = "5L3GLUpAUL" 
encText = urllib.parse.quote("해리포터") #한글에 URL을 추가하기 위해 UTP-8 형식으로 URL 인코딩
url = "https://openapi.naver.com/v1/search/book?query=" + encText +"&display=3&sort=count"
request = urllib.request.Request(url) #클라이언트의 요청을 처리
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request) #서버의 응답을 처리
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)


import json
json_rt = response.read().decode('utf-8')
py_rt = json.loads(json_rt)
