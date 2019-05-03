import requests
from python_api.public.my_log import My_Log
logger=My_Log()


class Request:
    def request(self,url,param,method,cookies):
        if method.upper()=='GET':
            try:
                result=requests.get(url,param,cookies=cookies)
            except Exception as error:
                logger.error('错误是：{}'.format(error))
                raise error
        elif method.upper()=='POST':
            try:
                result=requests.post(url,param,cookies=cookies)
            except Exception as error:
                logger.error('错误是：{}'.format(error))
                raise error
        return result


if __name__ == '__main__':
    url='http://119.23.241.154:8080/futureloan/mvc/api/member/register'
    param={'mobilephone':'13344445667','pwd':'123456','regname':'lemon'}
    result=Request().request(url,param,'get',cookies=None).json()
    print(result)