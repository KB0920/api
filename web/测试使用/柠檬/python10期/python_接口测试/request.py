import requests
url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
param={'mobilephone':'13344455555','pwd':'123456','regname':'lemonbest'}

class HttpRequest:
    def httprequest(self,url,param,method):
        if method.upper()=='GET':
            try:
                result=requests.get(url,param).json()
            except Exception as error:
                print('错误：',error)
                raise error
        elif method.upper()=='POST':
            try:
                result=requests.post(url,param).json()
            except Exception as error:
                print('错误：',error)
                raise error

        return result
if __name__ == '__main__':
    url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    param = {'mobilephone': '13344455515', 'pwd': '123456', 'regname': 'lemonbest'}
    HttpRequest().httprequest(url,param,'get')