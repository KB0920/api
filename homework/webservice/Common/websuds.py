# -*- coding:utf-8 -*-
from suds.client import Client
from webservice.Common.mylog import Logger
from suds import WebFault

class Suds:

    def suds(self,method,url,param):
        client = Client(url)
        if method=='userRegister':
            try:
                result=client.service.userRegister(param)
            except WebFault as error:
                Logger().error('请求出错：错误是{}'.format(error))
                result = error.fault

        elif method=='sendMCode':
            try:
                result=client.service.sendMCode(param)
            except WebFault as error:
                Logger().error('请求出错：错误是{}'.format(error))
                result=error.fault


        elif method=='verifiedUserAuth':
            try:
                result=client.service.verifyUserAuth(param)
            except WebFault as error:
                Logger().error('请求出错：错误是{}'.format(error))
                result = error.fault

        elif method=='bindBankCard':
            try:
                result=client.service.bindBankCard(param)
            except WebFault as error:
                Logger().error('请求出错：错误是{}'.format(error))
                result = error.fault

        elif method=='setPayPwd':
            try:
                result=client.service.setPayPwd(param)
            except WebFault as error:
                Logger().error('请求出错：错误是{}'.format(error))
                result = error.fault

        return result

