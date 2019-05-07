# -*- coding:utf-8 -*-
import configparser

class Config:

    def __init__(self,file):
        self.config=configparser.ConfigParser()
        self.config.read(file)
        self.rawconfig=configparser.RawConfigParser()
        self.rawconfig.read(file)

    def config_get(self,section,option):
        value=self.config.get(section,option)
        return value

    def rawconfig_get(self,section,option):
        value=self.rawconfig.get(section,option)
        return value
