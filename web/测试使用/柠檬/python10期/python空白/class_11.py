__author__ = 'Administrator'
class Chinese:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def skill(self,msg):
        print(self.name+"会看{}".format(msg))

    def ah(self,*args):
        for item in args:
            print('爱好玩{}'.format(item))

    def smoke(self):
        print('喜欢抽烟')


class Math:
    def __init__(self,name):
        self.name=name

    def skill(self,msg):
        print(self.name+"会做{}".format(msg))

    def fc(self,*args):
        for item in args:
            print('能够写{}方程'.format(item))
    def xh(self):
        print('爱好唱歌')

# class Student(Chinese):
#
#     def skill(self,msg,*args):
#         super(Student,self).skill(msg)
#         skill=''
#         for item in args:
#             skill+=item
#             skill+='、'
#         print('能看懂{}这些文章'.format(skill))
#
# nan=Student('南同学',24)
# nan.skill('白话文','古文','文言文','古诗文')
# nan=Student('南同学',24)
# nan.smoke()
# nan.skill('白话文')
# nan.xh()


class Student(Chinese):
    def nl(self,lg='python'):
        print('我能够书写{}代码，我叫{}，今年{}岁'.format(lg,self.name,self.age))

x=Student('瓜同学',10)
x.nl()