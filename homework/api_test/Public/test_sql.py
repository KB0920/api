

import pymysql
from api_test.Public.test_config import Config
from api_test.Public import test_path

class Do_Sql:

    def __init__(self):
        config = eval(Config(test_path.config_path).config_get('DB', 'connect'))
        self.connect = pymysql.connect(**config)
        self.cursor =self.connect.cursor()

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



if __name__ == '__main__':

    loanid = Do_Sql().fetchone("select leaveamount from member where mobilephone ='13344442283'")[0]
    print(loanid)