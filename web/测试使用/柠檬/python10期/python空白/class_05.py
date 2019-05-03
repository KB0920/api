__author__ = 'Administrator'
# str_1='param:{"phone":"18688773467","pwd":"123456"}@url:"http://119.23.241.154:8080/futureloan/mvc/api/member/register\nparam:{"phone":"18688773467","pwd":"123456"}@url:"http://119.23.241.154:8080/futureloan/mvc/api/member/login'
# list=[]
#
# list_1=str_1.split('\n')
# print('第一次切割：',list_1)
# for i in list_1:
#     list_2=i.split('@')
#     print('第二次切割：',list_2)
#     dict={}
#     for h in list_2:
#         list_3=h.split(':',1)
#         print('第三次切割：',list_3)
#         dict[list_3[0]]=list_3[1]
#     list.append(dict)
# print(list)
a=0
for i in range(1,101):
    a+=i
print(a)

a=0
b=0
while b<101:
    a+=b
    b+=1
print(a)