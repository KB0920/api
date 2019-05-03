__author__ = 'Administrator'


#configparser python自带的处理配置文件的模块
import configparser
class ReadConfig:
    def readconfig(self,file_path,section,option):
        cf=configparser.ConfigParser()#实例化

        cf.read(file_path,encoding='utf-8')#read函数打开文件

        value=cf.get(section,option)#获取之后的类型都是字符串类型
        #getint 可以直接获取数字类型的
        return value