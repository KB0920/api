__author__ = 'Administrator'
import unittest
from python空白.class_算数 import MathMethod
from python空白.class_14 import DoExcel
class TestAdd(unittest.TestCase):
    def setUp(self):
        self.t=MathMethod()
        self.excel=DoExcel('testdata.xlsx','testdata')


    def __init__(self,a,b,expected,title,case_id,methodname):
        super(TestAdd,self).__init__(methodname)
        self.a=a
        self.b=b
        self.expected=expected
        self.title=title
        self.case_id=case_id

    def test_add(self):
        print('正在执行的是：',self.title)
        print('a的值是：',self.a)
        print('b的值是：',self.b)
        print('expected的值是：',self.expected)

        res=self.t.add(self.a,self.b)
        try:
            self.assertEqual(self.expected,res)
            result='pass'

        except AssertionError as e:
            result='fail'
            print('测试出错了，错误是：',e)
            raise e
        # DoExcel.write(self.case_id+1,res,result)
        finally:
            self.excel.write(self.case_id+1,res,result)
    # def test_add_zero(self):
    #     res=self.t.add(0,0)
    #     try:
    #         self.assertEqual(0,res)#断言函数的应用，判断前后是否一样
    #     except AssertionError as e:
    #         print('测试出错了，错误是：',e)#try 只处理错误，不中断测试，但是要抛出错误
    #         raise e #抛出错误  代码必然要加try 进行错误处理
    #     # assert 判断 Equal 相等
    #     # 一般期望值放在前面，期望值可以是任何类型，值判断左右是否相等
    #
    # def test_add_positive(self):
    #     res=self.t.add(1,2)
    #     try:
    #         self.assertEqual(3,res)
    #     except AssertionError as e:
    #         print('测试出错了，错误是：',e)
    #         raise e
    #
    # def test_add_negative(self):
    #     res=self.t.add(-1,-2)
    #     try:
    #         self.assertEqual(-3,res)
    #     except AssertionError as e:
    #         print('测试出错了，错误是：',e)
    #         raise e
# if __name__ == '__main__':
#     unittest.main()
