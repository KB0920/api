# -*- coding:utf-8 -*-

import pymysql
from webservice.Common.config import Config
from webservice.Common import path

class Do_Mysql:

    def __init__(self,database):

        data=eval(Config(path.conf_path).config_get('SQL','database'))
        self.connect=pymysql.connect(**data,database=database)
        self.cursor=self.connect.cursor()

    def commit(self):
        self.connect.commit()


    def fetchone(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connect.close()

