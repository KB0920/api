# -*- coding:utf-8 -*-
import HTMLTestRunnerNew
import unittest
from webservice.Common import path
import sys

sys.path.append('./')
print(sys.path)
# discover=unittest.defaultTestLoader.discover(path.case_path,'*_case.py')
#
# with open(path.report_path,'wb+') as file:
#     runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='webservice测试',description=None,tester='KB')
#     runner.run(discover)