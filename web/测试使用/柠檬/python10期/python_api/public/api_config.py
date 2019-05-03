import configparser

class Config:
    def config(self,file,section,option):
        config=configparser.ConfigParser()
        config.read(file,encoding='utf-8')
        value=config.get(section,option)
        return value

if __name__ == '__main__':
    mode=Config().config('case.config','CASECONFIG','mode')
    print(mode)