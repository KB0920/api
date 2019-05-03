__author__ = 'Administrator'
#ddt框架 结合单元测试来做的
#帮我们拆分数据，传递参数给测试用例

import unittest
from ddt import ddt,data,unpack
testdata=[[1,2,3],[3,4,5]]
@ddt
class Mathod(unittest.TestCase):
    @data(*testdata) #把testdata的数据进行拆分
    #如果是列表就按索引取值，如果是字典就按key值取值
    @unpack#进一步的拆分,一般不用,因为字典取值的时候不一定都有用
    def test_add(self,a,b,c):
        # a=item[0]
        # b=item[1]
        print('\na+b+c的和是：',a+b+c)

