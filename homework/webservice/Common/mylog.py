# -*- coding:utf-8 -*-

from webservice.Common.config import Config
import logging
from webservice.Common import path

class Logger:

    def logger(self,level,msg):

        mylog=logging.getLogger('接口测试')
        mylog.setLevel('DEBUG')


        formatter=logging.Formatter(Config(path.conf_path).rawconfig_get('LOG','formatter'))

        fh=logging.FileHandler(path.log_path,encoding='utf-8')
        fh.setLevel(Config(path.conf_path).config_get('LOG','filehandler'))
        fh.setFormatter(formatter)

        sh=logging.StreamHandler()
        sh.setLevel(Config(path.conf_path).config_get('LOG','streamhandler'))
        sh.setFormatter(formatter)

        mylog.addHandler(sh)
        mylog.addHandler(fh)

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

        mylog.removeHandler(sh)
        mylog.removeHandler(fh)

    def debug(self,msg):
        self.logger('DEBUG',msg)

    def info(self,msg):
        self.logger('INFO', msg)

    def warning(self,msg):
        self.logger('WARNING', msg)

    def error(self,msg):
        self.logger('ERROR', msg)

    def critical(self,msg):
        self.logger('CRITICAL', msg)


