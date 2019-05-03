#coding=utf-8
__author__ = 'Administrator'
# def data_read():
#     a=[]
#     c=[]
#     try:
#         file=open('test.txt','r+',encoding='utf-8')
#     except Exception as e:
#         print('报错了')
#     x=file.readlines()
#     for l in x:
#         h=l.split('\n')
#         a.append(h)
#     a[0].pop(1)
#     for i in a:
#         for s in i:
#             h=s.split('@')
#             for j in h:
#                 try:
#                     b={}
#                 except Exception as e:
#                     print('出错了')
#                 k=j.split(':',1)
#                 b[k[0]]=k[1]
#                 c.append(b)
#     print(c)
#
# data_read()











# 一个足球队在寻找年龄在m岁到n岁的男生or女生
# （包括m岁和n岁，到底是找男生还是女生，可指定性别）加入
# 编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
# 然后显示一条消息指出这个人是否可以加入球队，询问k次后，输出满足条件的总人数



def join(m,n,h,k):
    a=0
    for i in range(1,k+1):
        age=int(input('请输入你的年龄：'))
        sex=input('请输入你的性别：')
        if m<=age<=n and sex==h:
            a=a+1
            print('符合条件，可以加入球队')
        elif age<=m or age>=n or sex!=h:
            print('年龄不符合条件，无法加入球队')
    print('满足条件的总人数{}'.format(a))

join(10,12,'boy',3)