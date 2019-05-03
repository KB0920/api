#-*- coding: utf-8 -*-
import unittest
from python_api.public.api_request import Request
from python_api.public.api_excel import Doexcel
from ddt import ddt,data
from python_api.public.api_config import Config
from python_api.public import api_path
from python_api.public.my_log import My_Log
from python_api.public.api_tel import Tel
from python_api.public.api_mysql import DoMysql

logger=My_Log()
test_data=Tel().tel()





COOKIES=None
@ddt
class TestApi(unittest.TestCase):
    def setUp(self):
        self.t=Doexcel(api_path.data_path)

    @data(*test_data)
    def test_case(self,item):
        global COOKIES
        logger.info('正在执行第{}条测试用例'.format(item['id']))
        logger.info('测试数据是：{}'.format(item['param']))

        if item['param'].find('loan_id')!=-1:
            sql_name=Config().config(api_path.sql_path,'DBCONFIG','sql_name_1')
            sql_name_1=DoMysql().read_mysql(sql_name)
            memberid=str(sql_name_1[0][0])
            sql_name = 'select max(id) from loan where memberid={}'.format(memberid)
            loanid = DoMysql().read_mysql(sql_name)[0][0]
            param=item['param'].replace('loan_id',str(loanid))
        else:
            param=item['param']

        actual=Request().request(item['module'],eval(param),item['method'],COOKIES)

        if actual.cookies:
            COOKIES=actual.cookies

        logger.info('实际结果是：{}'.format(actual.json()))
        try:
            self.assertEqual(str(actual.json()['code']),str(item['expected']))
            result='PASS'
        except AssertionError as error:
            result='FAIL'
            raise error
        finally:
            self.t.write(item['sheet_name'],item['id']+1,actual.json()['code'],result)


