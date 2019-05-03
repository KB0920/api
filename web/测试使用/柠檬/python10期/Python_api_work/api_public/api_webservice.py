from suds.client import Client

class Suds:
    def suds(self,method,url,param):
        client=Client(url,faults=False)
        #设置支付密码的接口
        if method=='setPayPwd':
            try:
                result=client.service.setPayPwd(param)
            except Exception as error:
               raise error
        #设置注册的接口
        elif method=='userRegister':
            try:
                result=client.service.userRegister(param)
            except Exception as error:
                raise error
        #设置实名认证的接口
        elif method=='verifyUserAuth':
            try:
                result=client.service.verifyUserAuth(param)
            except Exception as error:
                raise error
        #设置绑定银行卡的接口
        elif method=='bindBankCard':
            try:
                result=client.service.bindBankCard(param)
            except Exception as error:
                raise error
        #设置发送验证码的接口
        elif method=='sendMCode':
            try:
                result=client.service.sendMCode(param)
            except Exception as error:
                raise error

        return result


