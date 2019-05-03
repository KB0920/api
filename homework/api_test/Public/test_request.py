# -*- coding:utf-8 -*-

import requests
from api_test.Public.test_logger import Logger

class Request:
    def request(self,method,url,param,cookies=None):
        if method.upper()=='GET':
            try:
                result=requests.get(url,param,cookies=cookies)
            except Exception as error:
                Logger().error('GET请求出现错误，错误是:{}'.format(error))
                raise error

        elif method.upper()=='POST':
            try:
                result = requests.post(url, param, cookies=cookies)
            except Exception as error:
                Logger().error('POST请求出现错误，错误是:{}'.format(error))
                raise error

        return result

if __name__ == '__main__':
    register_url='http://test.lemonban.com/futureloan/mvc/api/member/register'
    login_url='http://test.lemonban.com/futureloan/mvc/api/member/login'
    recharge_url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    register_param_1={'mobilephone':'13322222244','pwd':'123456','regname':'lemon'}
    register_param_2={'mobilephone':'13322222256','pwd':'123456','regname':'lemon'}
    login_param={'mobilephone':'13322222244','pwd':'123456','regname':'lemon'}
    recharge_param={'mobilephone':'13322222256','amount':'10000'}
    result_register=Request().request('get',register_url,register_param_1)
    print(result_register.json())
    result_register = Request().request('get', register_url, register_param_2)
    print(result_register.json())
    result_login=Request().request('get',login_url,login_param)
    print(result_login.json())
    # cookies=result_login.cookies
    # print(cookies)
    result_recharge=Request().request('get',recharge_url,recharge_param)
    print(result_recharge.json())