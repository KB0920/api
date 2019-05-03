import configparser
#生成一个读取配置文件的类
class Config:
    def config(self,file,section,option):
        config=configparser.ConfigParser()
        config.read(file,encoding='utf-8')
        result=config.get(section,option)
        return result

