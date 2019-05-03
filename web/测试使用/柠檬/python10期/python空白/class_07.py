__author__ = 'Administrator'
# def print_msg(**kwargs):
#     print("kwargs的值是：{0}".format(kwargs))
#
# d=[1,2,3,4]
# # d={"name":'空白','age':'23'}
# print_msg(**d)

# def print_msg(*args):
#     print('args的数据是：{}'.format(args))
#
# a=[1,2,3,4,5]
# print_msg(*a)


a=10      #全局变量
def add(b):
    a=5   #局部变量
    #global a
    #a+=10
    print('函数内a的值：',a)
    print('b的值：',b)

if __name__ == '__main__':#代码的执行入口，只有当右键点击
                        #的时候才会执行下面的代码
    add(99)
    print('函数外a的值：',a)