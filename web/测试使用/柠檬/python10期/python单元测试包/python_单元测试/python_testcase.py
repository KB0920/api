import unittest
from python单元测试包.python_单元测试.python_代码 import MathMethod
from python单元测试包.python_单元测试.python_config import Config
from python单元测试包.python_单元测试.python_excel import DoExcel


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.t=MathMethod()

    def __init__(self,a,b,expected,title,case_id,methodname):
        super(TestAdd,self).__init__(methodname)
        self.a=a
        self.b=b
        self.expected=expected
        self.title=title
        self.case_id=case_id

    def test_add(self):
        print('a的值是：',self.a)
        print('b的值是：', self.b)
        print('expected的值是：', self.expected)
        res=self.t.add(self.a,self.b)

        try:
            self.assertEqual(self.expected,res)
            result='pass'
        except AssertionError as e:
            result='fail'
            print('出错了，错误是：',e)
            raise e
        finally:
            DoExcel('testdata.xlsx','testdata').write(self.case_id+1,res,result)