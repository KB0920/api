import unittest
from python_单元测试1.python_excel import DoExcel
from python_单元测试1.python_代码 import Add
from ddt import ddt,data
from python_单元测试1.python_config import Config

mode=Config().config('case.config','FLAG','mode')
case_id=eval(Config().config('case.config','FLAG','case_id'))
test_data=DoExcel('testdata.xlsx','testdata').read(mode,case_id)

print(test_data)
@ddt
class TestAdd(unittest.TestCase):
    def setUp(self):
        self.t=Add()
    @data(*test_data)
    def test_add(self,item):
        print('正在执行的是：', item['title'])
        print('a的值是：', item['param_a'])
        print('b的值是：', item['param_b'])
        print('expected的值是：', item['expected'])
        res=self.t.add(item['param_a'],item['param_b'])

        try:
            self.assertEqual(item['expected'],res)
            result='pass'
        except AssertionError as e:
            result='fail'
            print('出错了，错误是：',e)
            raise e
        finally:
            DoExcel('testdata.xlsx','testdata').write(item['id']+1,res,result)
