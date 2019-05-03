import unittest
from python空白.class_13 import TestAdd
import HTMLTestRunnerNew
from python空白 import class_13
suite=unittest.TestSuite()
test_data=[
    [0,0,0,'两个零相加'],
    [1,1,2,'两个正数相加'],
    [-1,-1,-2,'两个负数相加']]
for item in test_data:
    suite.addTest(TestAdd(item[0],item[1],item[2],item[3],'test_add'))
#loader=unittest.TestLoader()
#suite.addTest(loader.loadTestsFromModule(class_13))

with open('test.html','wb+') as file:#规定必须要二进制进行打开
    #runner=unittest.TextTestRunner(file,verbosity=2)
    runner=HTMLTestRunnerNew.HTMLTestRunner(file,title='python10',description='加法测试',tester='空白')
    runner.run(suite)
