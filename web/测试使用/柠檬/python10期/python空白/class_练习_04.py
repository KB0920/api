__author__ = 'Administrator'
# 1 :写一个软件测试工程师类，具有的属性和技能,你们自己去定。
# class SoftwareTestingEngineer:
#     age=25
#     sex='boy'
#     def skill(self,*args):
#         for item in args:
#             print('能够书写{}'.format(item))
#     def jkcs(self):
#         print('会接口测试')
#     def zdhcs(self,language):
#         print('会使用{}语言做自动化测试'.format(language))

# 2:创建一个名为User的类:
# 1 )其中包含属性first. name和last_ name ,还有用户简介通常会存储的其他几个属性
# 均是自定义，请放在初始化函数里面。
# 2)在类User中定义一一个名为describe_ user0的方法,它打印用户信息摘要;
# 3)再定义一个名为greet _user(的方法,它向用户发出个性化的问候。
#请创建多个表示不同用户的实例,并对每个实例都调用上述两个方法。
# class User:
#     def __init__(self,first_name,last_name):
#         self.first_name=first_name
#         self.last_name=last_name
#     def describe_uesr(self):
#         print('第一个使用者是：{}'.format(self.first_name))
#         print('最后一个使用者：{}'.format(self.last_name))
#     def greet_user(self,syz,why='你好'):
#         print('{},{}'.format(syz,why))

# 4:定义一个学生类。
# 1 )有下面的类属性: 1姓名2年龄3成绩(语文,数学,英语)
# [每课成绩的类型为整数] ,均放在初始化函数里面。
# 2)类方法:
# a)获取学生的姓名: get name(返回类型:str
# b)获取学生的年龄: get_ age0返回类型int
# c)返回3门科目中最高的分数。
# get_ course0返回类型:int
# 写好类以后,可以定义2个同学测试下:
# zm = Student( zhangming',20,[69,88,100])
# 返回结果: zhangming 20 100
# class Student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def get_course(self):
#         if self.grade[0]>self.grade[1] and self.grade[0]>self.grade[2]:
#             return self.grade[0]
#
#         elif self.grade[1]>self.grade[0] and self.grade[1]>self.grade[2]:
#             return self.grade[1]
#
#         else:
#             return self.grade[2]
#
#     def zj(self):
#         age1=self.get_age()
#         name1=self.get_name()
#         grade1=self.get_course()
#         print(name1,age1,grade1)
#
#
# zm=Student('zhangming',20,[69,88,100])
# zm.zj()
#

# 5人和机器猜拳游戏写成一个类,有如下几个函数:
# 1)函数1:选择角色1曹操2张飞3刘备
# 2)函数2 :角色猜拳1剪刀2石头3布玩家输入一一个1-3的数字
# 3)函数3 :电脑出拳随机产生1个1-3的数字,提示电脑出拳结果
# 4)函数4 :角色和机器出拳对战,对战结束后最后出示本局对战结果..赢..输
# 然后提示用户是否继续?按y继续,按n退出。
# 5)最后结束的时候输出结果角色赢几局电脑赢几局,平局几次游戏结束
import random
# class Caiquan:
#
#     def choose(self):
#         x=input('请选择角色：1.曹操、2.张飞、3.刘备：')
#         dict1={'1':'曹操','2':'张飞','3':'刘备'}
#         return dict1[x]
#
#     def player(self):
#         a=input('请选择出拳：1.剪刀、2.石头、3.布：')
#         return a
#
#     def comp(self):
#         b=random.randint(1,3)
#         return b
#
#     def pk(self):
#
#         dict2={1:'剪子',2:'石头',3:'步'}
#         f=0
#         g=0
#         h=0
#         while True:
#
#             c=int(self.player())
#             d=self.comp()
#             e=dict2[c]-dict2[d]
#
#
#             if e==1 or e==-2:
#                 print('恭喜您，您赢了')
#                 f+=1
#             elif e!=1 or e!=-2:
#                 print('对不起，您输了')
#                 g+=1
#             elif e==0:
#                 print('打平了')
#                 h+=1
    #             i=input('是否继续?按y继续,按n退出:')
#             if i=='y':
#                 continue
#             elif i=='n':
#                 print('您赢了{}局，输了{}局，平{}局'.format(f,g,h))
#                 break
#
#
#
#
# Caiquan.pk(1)


#  class Cq:
#     def change(self,js):
#         if js==1:
#             return '曹操'
#         elif js==2:
#             return '张飞'
#         elif js==3:
#             return '刘备'
#     def cq1(self):
#         return int(input('请玩家输入：'))
#
#     def cq2(self):
#         return random.randint(1,3)
#
#     def dz(self):
#         x=self.cq1()
#         y=self.cq2()
#         if x-y>0 or x-y==-2:
#             print('赢')
#         elif x-y<0 or x-y!=-2:
#             print('输')
#
