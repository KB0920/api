import mysql.connector
from Python_api_work.api_public.api_config import Config
from Python_api_work.api_public import api_path


#数据库类
class DoMysql:
    def do_mysql(self,database,sql_name):

        config=eval(Config().config(api_path.mysql_path,'DBCONFIG','config'))

        data_base=database
        #传入数据库信息
        conn=mysql.connector.connect(**config,database=data_base)

        cursor=conn.cursor()
        #传入sql语句
        sql=sql_name
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()
        return result

