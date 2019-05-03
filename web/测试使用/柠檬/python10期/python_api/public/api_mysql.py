#mysql-connector-python 操作数据库的插件
import mysql.connector
from python_api.public.api_config import Config
from python_api.public import api_path
#要提供数据库的信息：地址，端口，用户名，密码
# config={'host':'119.23.241.154',
#         'user':'python',
#         'password':'python666',
#         'port':'3306',
#         'database':'future'}#指定数据库的名字
# sql_name=Config().config(api_path.sql_path,'DBCONFIG','sql_name')
#1、登录数据库，产生一个数据库连接
class DoMysql:
    def read_mysql(self,sql_name):
        config=eval(Config().config(api_path.sql_path,'DBCONFIG','config'))
        conn=mysql.connector.connect(**config)#以字典的形式传递参数

#2、连接之后，产生一个游标，可以获得操作数据库的权限
        cursor=conn.cursor()

#3、利用游标进行操作
        sql=sql_name
        cursor.execute(sql)

#4获取结果，获取单条数据，或者获取多条数据
        #result=cursor.fetchone()#返回的是一个元组
        result=cursor.fetchall()#返回的是一个列表嵌套的元组
        cursor.close()
        conn.close()
        return result

#5、关掉游标，关掉连接


