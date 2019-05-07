# -*- coding:utf-8 -*-
import unittest
from webservice.Common.mylog import Logger
from webservice.Common.websuds import Suds
from ddt import ddt,data
from webservice.Common.data import Data
from webservice.Common.excel import Do_Excel
from webservice.Common import path

@ddt
class Test_SendMCode(unittest.TestCase):

    test_data=Data().data('sendMCode')

    @classmethod
    def setUpClass(cls):
        cls.logger=Logger()
        cls.excel=Do_Excel(path.excel_path)

    @data(*test_data)
    def test_api(self,item):

        self.logger.info('当前正在执行的第{}条用例'.format(item['id']))
        self.logger.info('当前执行的用例是：{}'.format(item['description']))
        self.logger.info('当前正在执行的数据是：{}'.format(item['param']))
        self.logger.info('期望结果是：{}'.format(item['expected']))


        actual=Suds().suds(item['method'],item['module'],eval(item['param']))
        self.logger.info('实际结果是：{}'.format(actual))


        if str(actual).find('retInfo')!=-1:
            try:
                self.assertEqual(item['expected'],actual['retInfo'])
                result='Ture'

            except AssertionError as error:
                result='False'
                self.logger.error('断言错误，错误是：{}'.format(error))
                raise error

            finally:
                self.excel.write(item['sheet_name'],item['id']+1,str(actual['retInfo']),result)

        else:
            try:
                self.assertEqual(item['expected'],actual['faultstring'])
                result = 'Ture'

            except AssertionError as error:
                result = 'False'
                self.logger.error('断言错误，错误是：{}'.format(error))
                raise error

            finally:
                self.excel.write(item['sheet_name'], item['id'] + 1, str(actual['faultstring']), result)


