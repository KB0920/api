#-*- coding: utf-8 -*-
__author__ = 'Administrator'
# class renzha:
#     #类属性
#     money='没钱'
#     home='没房'
#     car='没车'
#     #类方法
#     def xg(self,name):
#         print('{}性格很无耻'.format(name))
#     def ah(self,name):
#         print('{}爱好看女人'.format(name))
#     def zx(self,name='他'):
#         print('{}丑的一逼'.format(name))
#
# 三金=renzha()
# 三金.ah('三金')
# 三金.xg('三金')

# class BoyFriend:
#     #类属性
#     height=180
#     money='2000万'
#     #类函数
#     def cooking(self,dish1,dish2,dish3):#self没有任何作用，但是必须要有，类里面的函数必须要写
#         print('会下厨,做{},做{},做{}'.format(dish1,dish2,dish3))
#     def earn(self,money,job='IT'):
#         print('做{}，能赚{}'.format(job,money))
#     def sport(self,*args):
#         for item in args:
#             print('爱好{}运动'.format(item))
#     def skill(self,**kwargs):
#         for item in kwargs.items():
#             print(item)
#     def bf(self):
#         self.earn('20万')
# #创建对象
# p_1=BoyFriend()
# p_1.skill(job='IT',money='200万')
# # p_1.bf()
# # p_1.sport('篮球','排球','羽毛球')
# # p_1.earn('100万','测试')
# # p_1.cooking('蛋炒饭','鱼香肉丝','辣椒炒青椒')
# # p_1.cooking()
# # print('身高是{}'.format(p_1.height))


# class CS:
#     sex='boy'
#     age='25'
#     def skill(self,*args):
#         for item in args:
#             print('技能是{}'.format(item))
#     def auto(self,lg):
#         print('会{}语言，做自动化测试'.format(lg))
#     def jk(self):
#         print('会做接口测试')
#
# 空白=CS()
# 空白.jk()
# 空白.auto('python')
class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def cheng(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)
p=Math(4,8)
p.add()
p.sub()
p.cheng()
p.div()
# res=p.add()
# print('结果是:',res)

