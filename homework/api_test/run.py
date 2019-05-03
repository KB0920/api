# -*- coding:utf-8 -*-


import unittest
from api_test.Public import test_path
from api_test.test_case.register_case import TestRegister
from api_test.test_case.recharge_case import TestRecharge

from api_test.Public import test_path
import HTMLTestRunnerNew


suite=unittest.TestSuite()

loader=unittest.TestLoader()

discover=unittest.defaultTestLoader.discover(test_path.case_path,'*_case.py')

# suite.addTest(loader.loadTestsFromTestCase(TestInvest))


with open(test_path.report_path,mode='wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='接口测试',description=None,tester='KB')
    runner.run(discover)