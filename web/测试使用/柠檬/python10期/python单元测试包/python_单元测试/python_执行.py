import unittest
from python_单元测试.python_testcase import TestAdd
import HTMLTestRunnerNew
from python_单元测试.python_config import Config
from python_单元测试.python_excel import DoExcel

mode=Config().config('case.config','FLAG','mode')
case_id=eval(Config().config('case.config','FLAG','case_id'))
test_case=DoExcel('testdata.xlsx','testdata').read(mode,case_id)


suite=unittest.TestSuite()
for item in test_case:
    suite.addTest(TestAdd(item['param_a'],item['param_b'],item['expected'],item['title'],item['id'],'test_add'))




with open('test.html','wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='单元测试',description='加法测试',tester='空白')
    runner.run(suite)

