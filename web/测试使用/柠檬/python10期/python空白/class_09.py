__author__ = 'Administrator'
try:
    print(a)
    print('你好6662')
except NameError as e :
    print('出错了',e)
    raise e
# else:
#     print('你好6661')
finally:
    print('你好6661')

# file=open('test_data.txt','a')
# print(file.closed)
# file.close()
# print(file.closed)
# with open('test.txt','a+') as file:
#     file.write('66666')
# print('file的状态是',file.closed)

# from python空白.class_07 import add
#
# add(99)