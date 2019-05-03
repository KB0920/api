import random
import string
from Python_api_work.api_public.api_config import Config
from Python_api_work.api_public import api_path
from Python_api_work.api_public.api_excel import Do_Excel
#生成数据的模块
class Telephone:
    def telephone(self):
        #读取电话号码前8位
        tel=Config().config(api_path.config_path,'CASECONFIG','telephone')
        #电话号码第九位
        last_1 = random.randint(0, 9)
        #电话号码第十位
        last_2 = random.randint(0, 9)
        #电话号码第十一位
        last_3 = random.randint(0, 9)
        last_4 = last_1+1
        last_5 = last_2+2
        #从上述五个里面选择三个生成三个电话号码
        telephone_1 = tel + str(last_1) + str(last_2) + str(last_3)
        telephone_2= tel+str(last_4)+str(last_2)+str(last_1)
        telephone_3=tel+str(last_1)+str(last_2)+str(last_5)
        #生成随机用户名
        usr_1= ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5))
        usr_2= ''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 4))
        #生成随机真实姓名，如果用过了可以手动更改需要用的字
        true_name=''.join(random.sample(['李','我','佳','飞','唉','拜','去','服','莫','愁'],3))
        #读取测试数据
        test_data=Do_Excel(api_path.excel_path).read()

        #如果存在就替换数据
        for item in test_data:
            data=item['param']
            if data.find('tel_1')!=-1:
                param=data.replace('tel_1',telephone_1)
                item['param']=param

            elif data.find('tel_2')!=-1:
                param=data.replace('tel_2',telephone_2)
                item['param']=param

            elif data.find('tel_3')!=-1:
                param=data.replace('tel_3',telephone_3)
                item['param']=param



        for item in test_data:
            data=item['param']

            if data.find('usr_1')!=-1:
                param=data.replace('usr_1',usr_1)
                item['param']=param

            elif data.find('usr_2')!=-1:
                param=data.replace('usr_2',usr_2)
                item['param']=param

        for item in test_data:
            data=item['param']
            if data.find('truename_1')!=-1:
                param=data.replace('truename_1',true_name)
                item['param']=param
        return test_data



