# -*- coding:utf-8 -*-
import unittest
from ddt import ddt,data
from api_test.Public.test_data import Test_Data
from api_test.Public.test_logger import Logger
from api_test.Public.test_request import Request
from api_test.Public.test_excel import Do_Excel
from api_test.Public import test_path
from api_test.Public.test_sql import Do_Sql
from api_test.Public.test_config import Config


COOKIES=None

@ddt
class TestRecharge(unittest.TestCase):
    test_data=Test_Data().test_data('recharge')

    @classmethod
    def setUpClass(cls):
        cls.logger=Logger()
        cls.excel=Do_Excel(test_path.excel_path)
        cls.sql=Do_Sql()
        cls.config=Config(test_path.config_path)

    @data(*test_data)
    def test_api(self,item):
        global COOKIES
        self.logger.info('当前正在执行第{}条用例'.format(item['id']))
        self.logger.info('当前的url是：{}'.format(item['module']))
        self.logger.info('测试数据是：{}'.format(item['param']))

        if item['description']=='正常充值':
            mobilephone = eval(item['param'])['mobilephone']
            amount_before=self.sql.fetchone("select leaveamount from member where mobilephone ={}".format(eval(mobilephone)))[0]
            amount=eval(item['param'])['amount']
            actual=Request().request(item['method'],item['module'],eval(item['param']),cookies=COOKIES)
            self.sql.commit()
            amount_after=self.sql.fetchone("select leaveamount from member where mobilephone ={}".format(eval(mobilephone)))[0]

        else:
            actual=Request().request(item['method'],item['module'],eval(item['param']),cookies=COOKIES)

        if actual.cookies:
            COOKIES=actual.cookies

        self.logger.info('期望结果是：{}'.format(item['expected']))
        self.logger.info('实际结果是：{}'.format(actual.json()))

        try:
            if item['description']=='正常充值':
                self.assertEqual(eval(amount)+amount_before,amount_after)
                result='PASS'
            else:
                self.assertEqual(actual.json()['code'],str(item['expected']))
                result='PASS'
        except AssertionError as error:
            self.logger.error('断言错误，错误是：{}'.format(error))
            result='FAIL'
            raise error
        finally:
            self.excel.write(item['sheet_name'],item['id']+1,actual.json()['code'],result)

    @classmethod
    def tearDownClass(cls):
        Do_Sql().close()

