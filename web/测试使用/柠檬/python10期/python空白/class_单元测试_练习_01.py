import unittest
from python空白.class_算数 import MathMethod

class TestAdd(unittest.TestCase):
    def setUp(self):
        self.t=MathMethod()

    def test_add_zero(self):
        res=self.t.add(0,0)
        print('最后的结果是：',res)

    def test_add_positive(self):
        res=self.t.add(1,2)
        print('最后的结果是：',res)

    def test_add_negative(self):
        res=self.t.add(-1,-2)
        print('最后的结果是：',res)

if __name__ == '__main__':
    unittest.main()