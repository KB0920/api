__author__ = 'Administrator'
import unittest
from python单元测试包.class_ddt.class_算数 import MathMethod
from python单元测试包.class_ddt.class_14 import DoExcel
from python单元测试包.class_ddt import ReadConfig
from ddt import ddt,data
mode=ReadConfig().readconfig('case.config','FLAG','mode')
case_id_list=eval(ReadConfig().readconfig('case.config','FLAG','case_id_list'))
test_data=DoExcel('testdata.xlsx','testdata').read(mode,case_id_list)


@ddt
class TestAdd(unittest.TestCase):
    def setUp(self):
        self.t=MathMethod()
        self.excel=DoExcel('testdata.xlsx','testdata')

    @data(*test_data)


    def test_add(self,item):
        print('正在执行的是：',item['title'])
        print('a的值是：',item['param_a'])
        print('b的值是：',item['param_b'])
        print('expected的值是：',item['expected'])

        res=self.t.add(item['param_a'],item['param_b'])
        try:
            self.assertEqual(item['expected'],res)
            result='pass'

        except AssertionError as e:
            result='fail'
            print('测试出错了，错误是：',e)
            raise e
        finally:
            self.excel.write(self.case_id+1,res,result)

# if __name__ == '__main__':
#     unittest.main()
