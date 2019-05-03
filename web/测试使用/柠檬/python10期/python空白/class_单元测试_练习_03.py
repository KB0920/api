__author__ = 'Administrator'
import unittest
from python空白.class_算数 import MathMethod

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.t=MathMethod()

    def __init__(self,a,b,expected,title,methodname):
        super(TestAdd,self).__init__(methodname)
        self.a=a
        self.b=b
        self.expected=expected
        self.title=title

    def test_add(self):
        print('正在执行的是：',self.title)
        print('a的值是：',self.a)
        print('b的值是：',self.b)
        print('期望值是：',self.expected)
        res=self.t.add(self.a,self.b)
        try:
            self.assertEqual(self.expected,res)
        except AssertionError as e:
            print('出现的错误是：',e)
            raise e

if __name__ == '__main__':
    unittest.main()