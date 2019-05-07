# -*- coding:utf-8 -*-
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)



import HTMLTestRunnerNew
import unittest
from webservice.Common import path


discover=unittest.defaultTestLoader.discover(path.case_path,'*_case.py')

with open(path.report_path,'wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='webservice测试',description=None,tester='KB')
    runner.run(discover)