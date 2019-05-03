__author__ = 'Administrator'

import unittest
#导入了unittest的时候自动变成单元测试的模式
from python空白.class_算数 import MathMethod#导入被测试类
#写用例，每一条用例都是一个函数
#用例：def test_后缀（self）
class TestAdd(unittest.TestCase):#测试类 继承unittest.TestCase类
    def setUp(self):#测试环境的搭建
        self.t=MathMethod()#把实例变为全局变量

    def tearDown(self):#测试环境的销毁
        print('测试完成')

    def test_add_zero(self):#测试两个0相加
        #t=MathMethod() 创建实例
        res=self.t.add(0,0)
        print('测试的结果是：',res)

    def test_add_positive(self):#测试两个正数相加

        res=self.t.add(4,5)
        print('测试的结果是：',res)

    def test_add_negative(self):#测试两个负数相加

        res=self.t.add(-4,-5)
        print('测试的结果是：',res)

# class TestSub(unittest.TestCase):#测试类 继承unittest.TestCase类
#     def test_sub_zero(self):#测试两个0相加
#         t=MathMethod()#创建实例
#         res=t.sub(0,0)
#         print('测试的结果是：',res)
#
#     def test_sub_positive(self):#测试两个正数相加
#         t=MathMethod()
#         res=t.sub(4,5)
#         print('测试的结果是：',res)
#
#     def test_sub_negative(self):#测试两个负数相加
#         t=MathMethod()
#         res=t.sub(-4,-5)
#         print('测试的结果是：',res)

if __name__ == '__main__':
    unittest.main()#用一个main函数 全部执行用例
