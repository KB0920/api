# -*- coding:utf-8 -*-

import unittest
from webservice.Common.mylog import Logger
from webservice.Common.websuds import Suds
from ddt import ddt,data
from webservice.Common.data import Data
from webservice.Common.excel import Do_Excel
from webservice.Common import path
from webservice.Common.mysql import Do_Mysql
from webservice.Common.attr import Attr


@ddt
class Test_VerifiedUserAuth(unittest.TestCase):

    test_data=Data().data('verifiedUserAuth')

    @classmethod
    def setUpClass(cls):
        cls.logger=Logger()
        cls.excel=Do_Excel(path.excel_path)


    @data(*test_data)
    def test_api(self,item):

        if item['param'].find('yzm_1')!=-1:
            data=item['param']
            mobile=eval(item['param'])['mobile']
            database='sms_db_{}'.format(str(mobile)[-2::])
            yzm=Do_Mysql(database=database).fetchall('select Fverify_code from t_mvcode_info_{} where Fmobile_no = {}'.format(mobile[-3],mobile))[0][0]
            item['param']=data.replace('yzm_1',str(yzm))

        if item['param'].find('user_id')!=-1:
            usr = eval(item['param'])['user_id']
            setattr(Attr, 'usr', usr)

        if item['param'].find('uid_1')!=-1:
            data=item['param']
            print(getattr(Attr,'usr'))
            uid=Do_Mysql(database='user_db').fetchone("SELECT max(Fuid) FROM t_user_info where Fuser_id='{}'".format(getattr(Attr,'usr')))[0]
            item['param']=data.replace('uid_1',str(uid))


        self.logger.info('当前正在执行的第{}条用例'.format(item['id']))
        self.logger.info('当前执行的用例是：{}'.format(item['description']))
        self.logger.info('当前正在执行的数据是：{}'.format(item['param']))
        self.logger.info('期望结果是：{}'.format(item['expected']))

        actual=Suds().suds(item['method'],item['module'],eval(item['param']))
        self.logger.info('实际结果是：{}'.format(actual))


        if str(actual).find('retInfo') != -1:
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
                self.assertEqual(item['expected'], str(actual['faultstring']))
                result = 'Ture'

            except AssertionError as error:
                result = 'False'
                self.logger.error('断言错误，错误是：{}'.format(error))
                raise error

            finally:
                self.excel.write(item['sheet_name'], item['id'] + 1, str(actual['faultstring']), result)

    @classmethod
    def tearDownClass(cls):
        Do_Mysql(database=None).close()