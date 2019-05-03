#requests模块的安装：pip install requests

#python的requests模块参数都是以字典的方式传递
import requests


url='https://www.ketangpai.com/UserApi/login'
param={'email':'15204589879',
       'password':'nzj950920',
       'remember':0}
res=requests.post(url,param)
#状态码
print('响应状态码：',res.status_code)
#响应头
print('响应头是：',res.headers)
#响应报文
print('响应报文：',res.text)#返回的是字符串，可以解析html，json，xml
print('响应报文：',res.json())#返回的是字典，只能解析json格式

print(res.cookies)