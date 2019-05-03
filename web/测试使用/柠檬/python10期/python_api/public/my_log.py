__author__ = 'Administrator'
#日志：记录系统的操作 记录代码的运行
#log
#日志级别（debug info warning error critical） 从左往右级别一次加重
#python中自带日志模块 logging  可以直接拿来用


#收集日志
#收集器会有名字，默认顶级收集器：root
#默认只收集warning（包含）以上的信息
#输出日志

import logging
from python_api.public import api_path
class My_Log:
    def my_log(self,level,msg):
#自己定义一个日志收集器
        mylog=logging.getLogger('python20')
        mylog.setLevel('DEBUG')  #只与收集有关

        #格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        #自己创建一个专属输入渠道   设置输出渠道
        ch=logging.StreamHandler()#自己创建一个，输出到控制台
        ch.setLevel('DEBUG')    #设置输出级别 一定要是大写或者数字
        #收集和输出取交集
        ch.setFormatter(formatter)

        sh=logging.FileHandler(api_path.log_path,encoding='utf-8')
        # sh.setLevel('DEBUG')
        sh.setFormatter(formatter)

        #对接起来   给日志收集器一个渠道，收集到的日志通过渠道输出
        mylog.addHandler(ch)
        mylog.addHandler(sh)

        if level=='DEBUG':
            mylog.debug(msg)

        if level=='INFO':
            mylog.info(msg)

        if level=='WARNING':
            mylog.warning(msg)

        if level=='ERROR':
            mylog.error(msg)

        if level=='CRITICAL':
            mylog.critical(msg)

        #每次使用之后要移除掉
        mylog.removeHandler(ch)
        mylog.removeHandler(sh)

    def debug(self,msg):
        self.my_log('DEBUG',msg)

    def info(self,msg):
        self.my_log('INFO',msg)

    def warning(self,msg):
        self.my_log('WARNING',msg)

    def error(self,msg):
        self.my_log('ERROR',msg)

    def critical(self,msg):
        self.my_log('CRITICAL',msg)

