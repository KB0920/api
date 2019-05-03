__author__ = 'Administrator'
import unittest
import HTMLTestRunnerNew
from python空白.class_算数 import MathMethod
from python空白.class_15 import ReadConfig
from python空白.class_13 import TestAdd
from python空白.class_14 import DoExcel
#test_data=[[0,0,0,'两个零相加'],[1,1,2,'两个正数相加'],[-1,-1,-2,'两个负数相加']]

mode=ReadConfig().readconfig('case.config','FLAG','mode')
case_id_list=eval(ReadConfig().readconfig('case.config','FLAG','case_id_list'))
test_data=DoExcel('testdata.xlsx','testdata').read(mode,case_id_list)
suite=unittest.TestSuite()


for item in test_data:
    suite.addTest(TestAdd(item['param_a'],item['param_b'],item['expected'],item['title'],item['id'],'test_add'))
    # row=item['id']+1
    # actual=item['param_a']+item['param_b']
    # if actual==item['expected']:
    #     result='PASS'
    # else:
    #     result='FAIL'
    # wr=DoExcel().write(row,actual,result)

with open('test.html','wb+') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='python10',description='单元测试',tester='空白')
    runner.run(suite)

