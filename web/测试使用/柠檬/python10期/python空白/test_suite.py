#-*- coding: utf-8 -*-
__author__ = 'Administrator'
#加载测试用例
import unittest
from python空白.class_12 import TestAdd
#from python空白.class_12 import TestSub
from python空白 import class_12
suite=unittest.TestSuite() #测试套件 就是创建一个实例
#怎么把用例放进去
#方法1
#suite.addTest(TestAdd('test_add_zero'))#添加参数必须是测试用例实例
#suite.addTest(TestAdd('test_add_positive'))
#suite.addTest(TestAdd('test_add_negative'))
#方法2
loader=unittest.TestLoader()
#suite.addTest(loader.loadTestsFromTestCase(TestAdd))
#suite.addTest(loader.loadTestsFromTestCase(TestSub))
#方法3
suite.addTest(loader.loadTestsFromModule(class_12))#调用什么 就要引入什么模块
#执行用例 TextTestRunner 专门执行suite里面的用例
with open('test_Test.txt','w+') as baibai:
    runner=unittest.TextTestRunner(baibai,verbosity=3)
    runner.run(suite)

#写报告
#file=open('test_Test.txt','w+')
