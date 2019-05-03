# -*- coding:utf-8 -*-
import logging
from api_test.Public.test_config import Config
from api_test.Public import test_path

class Logger:
    def logger(self,level,msg):
        mylog=logging.getLogger('测试日志')
        mylog.setLevel('DEBUG')

        formatter=logging.Formatter(Config(test_path.config_path).rawconfig_get('LOGGER','formatter'))

        streamhandler=logging.StreamHandler()
        streamhandler.setLevel(Config(test_path.config_path).config_get('LOGGER','streamlevel'))
        streamhandler.setFormatter(formatter)

        filehandler=logging.FileHandler(test_path.log_path,encoding='utf-8')
        filehandler.setLevel(Config(test_path.config_path).config_get('LOGGER','filelevel'))
        filehandler.setFormatter(formatter)

        mylog.addHandler(streamhandler)
        mylog.addHandler(filehandler)

        if level=='DEBUG':
            mylog.debug(msg)
        elif level=='INFO':
            mylog.info(msg)
        elif level=='WARNING':
            mylog.warning(msg)
        elif level=='ERROR':
            mylog.error(msg)
        elif level=='CRITICAL':
            mylog.critical(msg)

        mylog.removeHandler(streamhandler)
        mylog.removeHandler(filehandler)

    def debug(self,msg):
        self.logger('DEBUG',msg)

    def info(self,msg):
        self.logger('INFO',msg)

    def warning(self,msg):
        self.logger('WARNING',msg)

    def error(self,msg):
        self.logger('ERROR',msg)

    def critical(self,msg):
        self.logger('CRITICAL',msg)


if __name__ == '__main__':

    Logger().info('出错了')