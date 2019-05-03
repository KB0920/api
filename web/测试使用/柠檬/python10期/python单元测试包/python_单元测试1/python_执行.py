import unittest
from python_单元测试1.python_case import TestAdd
import HTMLTestRunnerNew

suite=unittest.TestSuite()

loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestAdd))

with open('test.html','wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='单元测试',description='加法测试',tester='南兆佳')
    runner.run(suite)