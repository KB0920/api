#反射

class PrintMsg:
    a=10
    b=20
    c=None

print(PrintMsg.c)
setattr(PrintMsg,'c',666)
#反射：如果没有属性名，就创建一个属性名然后赋值，如果属性名存在就直接赋值
print(PrintMsg.c)
setattr(PrintMsg,'d',888)
print(PrintMsg.d)#利用反射来进行数据的读取和存储 cookies和loan_id
#如果某个用例会用到上一个请求的响应结果或者数据
#1、都存到Excel
#2、利用全局变量
#3、反射
