import unittest
from Python_api_work.api_public.api_test import TestData
from Python_api_work.api_public import api_path
import HTMLTestRunnerNew


suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestData))
#生成html文件
#执行用例
with open(api_path.report_path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='接口测试',description='接口',tester='空白')
    runner.run(suite)