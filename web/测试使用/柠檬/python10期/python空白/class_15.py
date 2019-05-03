__author__ = 'Administrator'
#作自动化测试很多时候都是回归测试
#配置文件：（.ini .properties .config .conf .xml ）
#主要讲解文本模式的（业界通用）
#配置文件的读取

#configparser python自带的处理配置文件的模块
import configparser
class ReadConfig:
    def readconfig(self,file_path,section,option):
        cf=configparser.ConfigParser()#实例化

        cf.read(file_path,encoding='utf-8')#read函数打开文件

        value=cf.get(section,option)#获取之后的类型都是字符串类型
        #getint 可以直接获取数字类型的
        return value