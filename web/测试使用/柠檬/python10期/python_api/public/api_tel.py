import random
from python_api.public import api_path
from python_api.public.api_excel import Doexcel
from python_api.public.api_config import Config
from python_api.public.api_mysql import DoMysql












class Tel:
    def tel(self):
        number = Config().config(api_path.config_path, 'CASECONFIG', 'phone')
        tel=number
        i=random.randint(1000,9999) #生成1000到9999的四位随机数
        j=i+1
        k=i+2
        l=i+3

        tel_1=tel+str(i)
        tel_2=tel+str(j)
        tel_3=tel+str(k)
        tel_4=tel+str(l)


        test_data = Doexcel(api_path.data_path).read()
        if i in test_data:
            print(i)
        for item in test_data:
            data=item['param']
            if data.find('tel_1') != -1:
                param=data.replace('tel_1',tel_1)
                item['param'] = param

            elif data.find('tel_2') != -1:
                param=data.replace('tel_2',tel_2)
                item['param'] = param

            elif data.find('tel_3') != -1:
                param = data.replace('tel_3', tel_3)
                item['param'] = param


            elif data.find('tel_4') != -1:
                param = data.replace('tel_4', tel_4)
                item['param'] = param

            elif data.find('memberid_1')!=-1:
                sql_name=Config().config(api_path.sql_path,'DBCONFIG','sql_name_1')
                sql_name_1=DoMysql().read_mysql(sql_name)
                memberid=str(sql_name_1[0][0])
                param=data.replace('memberid_1',memberid)
                item['param']=param

            else:
                item['param']=data
        return test_data



if __name__ == '__main__':
    tel=Tel().tel()
    for i in tel:
        print(i)

