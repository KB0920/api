import requests

url='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
data={'mobilephone':'15358889997','pwd':'123456'}

res=requests.post(url,data)
cookie=res.cookies
print(cookie)