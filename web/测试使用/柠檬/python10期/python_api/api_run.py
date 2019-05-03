import unittest
from python_api.public.api_test import TestApi
import HTMLTestRunnerNew
from python_api.public import api_path
suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestApi))

with open(api_path.report_path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='接口测试',description='注册接口',tester='白白')
    runner.run(suite)