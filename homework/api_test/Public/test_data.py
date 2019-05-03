# -*- coding:utf-8 -*-
from api_test.Public.test_excel import Do_Excel
import random
from api_test.Public.test_config import Config
from api_test.Public import test_path
from api_test.Public.test_sql import Do_Sql

class Test_Data:

    def test_data(self,sheet_name):

        number=Config(test_path.config_path).config_get('CASE','number')
        number_list=[number+str(random.randint(1000,9999)) for i in range(1,5)]

        test_data=Do_Excel(test_path.excel_path).read(sheet_name)


        for item in test_data:
            data=item['param']

            if data.find('tel_1')!=-1:
                item['param']=data.replace('tel_1',number_list[0])

            elif data.find('tel_2')!=-1:
                item['param']=data.replace('tel_2',number_list[1])

            elif data.find('tel_3')!=-1:
                item['param']=data.replace('tel_3',number_list[2])

            elif data.find('tel_4')!=-1:
                item['param']=data.replace('tel_4',number_list[3])

            elif data.find('tel_admin')!=-1:
                mobilephone=Config(test_path.config_path).config_get('DATA','mobliephone')
                item['param']=data.replace('tel_admin',mobilephone)

            elif data.find('memberid_1')!=-1:
                mobilephone=Config(test_path.config_path).config_get('DATA','mobliephone')
                result=Do_Sql().fetchone("select id from member where mobilephone={}".format(mobilephone))
                memberid=str(result[0])
                item['param']=data.replace('memberid_1',memberid)

            else:
                item['param']=data

        return test_data

if __name__ == '__main__':

    result=Test_Data().test_data('invest')
    for i  in result:
        print(i)


