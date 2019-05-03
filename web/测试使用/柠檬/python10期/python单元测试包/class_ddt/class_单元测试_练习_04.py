__author__ = 'Administrator'
import unittest
import HTMLTestRunnerNew
from python单元测试包.class_ddt import class_13

suite=unittest.TestSuite()


loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(class_13))

with open('test.html','wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(file)
    runner.run(suite)

