import configparser

class Config:
    def config(self,file,section,option):
        cf=configparser.ConfigParser()
        cf.read(file,encoding='utf-8')

        value=cf.get(section,option)
        return value

