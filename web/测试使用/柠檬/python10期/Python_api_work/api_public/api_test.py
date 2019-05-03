import unittest
import time
from Python_api_work.api_public.api_telephone import Telephone
from ddt import ddt,data
from Python_api_work.api_public import api_path
from Python_api_work.api_public.api_webservice import Suds
from Python_api_work.api_public.api_excel import Do_Excel
from Python_api_work.api_public.api_log import Logger
from Python_api_work.api_public.api_mysql import DoMysql
#读取测试数据
telephone=Telephone().telephone()

log=Logger()


@ddt
class TestData(unittest.TestCase):
    def setUp(self):
        self.excel=Do_Excel(api_path.excel_path)

    @data(*telephone,)
    def test_case(self,item):

        log.info('正在执行第{}条测试用例'.format(item['id']))
        log.info('正在执行的用例是{}'.format(item['description']))
        #判断是否需要验证码
        if item['param'].find('yzm_1')!=-1:
            #查询到手机号码，查询数据库
            mobile=eval(item['param'])['mobile']
            db=str(mobile)[9:11]
            t=str(mobile)[8]
            database='sms_db_{}'.format(db)
            sqlname='select Fverify_code from t_mvcode_info_{} where Fmobile_no = {}'.format(t,mobile)
            yzm=DoMysql().do_mysql(database,sqlname)
            data=item['param'].replace('yzm_1',str(yzm[0][0]))
            #判断是否需要uid（有的地方需要替换两个数据，所以做了双重判断）
            if data.find('uid_1')!=-1:
                database = 'user_db'
                sqlname = 'SELECT MAX(Fuid) FROM t_user_info'
                uid = DoMysql().do_mysql(database, sqlname)
                param = data.replace('uid_1', str(uid[0][0]))
            else:
                param=data

        #判断延时获取验证码的时效性（120s均有效）
        elif item['param'].find('yzm_2')!=-1:
            mobile=eval(item['param'])['mobile']
            db=str(mobile)[9:11]
            t=str(mobile)[8]
            database='sms_db_{}'.format(db)
            sqlname='select Fverify_code from t_mvcode_info_{} where Fmobile_no = {}'.format(t,mobile)
            yzm=DoMysql().do_mysql(database,sqlname)
            time.sleep(120)
            param=item['param'].replace('yzm_2',str(yzm[0][0]))

        #判断是否存在uid，存在就从数据库中获取替换
        elif item['param'].find('uid_1')!=-1:
            database='user_db'
            sqlname='SELECT MAX(Fuid) FROM t_user_info'
            uid=DoMysql().do_mysql(database,sqlname)
            param=item['param'].replace('uid_1',str(uid[0][0]))

        else:
            param=item['param']


        log.info('测试数据是{}'.format(param))
        log.info('预期结果是{}'.format(item['expected']))

        #发送请求
        actual=Suds().suds(item['method'],item['module'],eval(param))

        log.info('实际结果是{}'.format(actual))

        #判断如果发现返回时retcode形式进行处理
        if str(actual[1]).find('retCode')!=-1:
            try:
                self.assertEqual(str([actual[1]['retInfo']]),str(item['expected']))
                test_result='pass'
            except AssertionError as error:
                test_result='fail'
                raise error
                log.error('出现错误{}'.format(error))
            finally:
                self.excel.write(item['sheet'],item['id']+1,actual[1]['retInfo'],test_result)
        #判断如果返回时是faultstring 那么只要不是ok 那就是正确的用例
        else:
            try:
                self.assertNotEqual(str(actual[1]['faultstring']),str(item['expected']))
                test_result='pass'
            except AssertionError as error:
                test_result='fail'
                raise error
                log.error('出现错误{}'.format(error))
            finally:
                self.excel.write(item['sheet'],item['id']+1,actual[1]['faultstring'],test_result)


