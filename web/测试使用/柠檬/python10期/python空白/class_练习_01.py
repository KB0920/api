__author__ = 'Administrator'
#3、
# a=int(input('请输入价格：'))
# if 50<=a<=100:
#     print('折扣是10%，最后的金额是：',a-a*0.1)
# elif a>100:
#     print('折扣是20%，最后的金额是：',a-a*0.2)
# else:
#     print('无折扣，最后的金额是：',a)
#
#1、

# a=0
# for i in range(10):
#     sex=input("请问你的性别是：")
#     age=int(input('请问你的年龄是：'))
#     if sex=='f' and 10<=age<=12:
#         a+=1
#         print('可以加入球队')
#     if sex=='m' or age<10 or age>12:
#         print('不可以加入球队')
# print('满足条件的总人数：',a)

# 4、
# import random
# a=random.randint(1,9)
# b=int(input('请输入数字：'))
# if b>a:
#     print('bigger')
# elif b<a:
#     print('less')
# else:
#     print('equal')

# 2、
# num=input('请输入四位数字：')
# b=''
# c=''
# for i in num:
#     a=str(((int(i)+5)%10))
#     b=b+a
# for i in range(-1,-5,-1):
#     c=c+b[i]
# print(c)

# 输出99乘法表
# for i in range(1,10):
#     for n in range(1,i+1):
#         print(str(i)+'*'+str(n)+'='+str(i*n))

# 自动贩卖机： 只接受1元、5元、10元的纸币或硬币，
# 可以1块，5元，10元。最多不超过10块钱。
# 饮料只有橙汁、椰汁、矿泉水、早餐奶，售价分别是3.5，4，2，4.5
# 写一个函数用来表示贩卖机的功能： 用户投钱和选择饮料，
# 并通过判断之后，给用户吐出饮料和找零。

def sell(water,*args):
    b=0
    for a in args:
        if a==1 or a==5 or a==10:
            b+=a
            if b<=10:
                c=b
    if water=='橙汁':
        n=3.5
    elif water=='椰汁':
        n=4
    elif water=='矿泉水':
        n=2
    elif water=='早餐奶':
        n=4.5
    x=c-n
    print('你选择的是{0}，找零{1}'.format(water,x))

sell('橙汁',1,1,5,10)


