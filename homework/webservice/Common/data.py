# -*- coding:utf-8 -*-

import random
from webservice.Common.excel import Do_Excel
from webservice.Common import path
from webservice.Common.config import Config


class Data:

    def data(self,sheetname):

        number=Config(path.conf_path).config_get('CASE','number')
        phone=[number+str(random.randint(1000,9999)) for i in range(0,4)]

        usr=[''.join(random.sample(Config(path.conf_path).config_get('CASE','usr'),3)) for i in range(0,4)]

        name=''.join(random.sample(Config(path.conf_path).config_get('CASE','name'),2))


        test_data=Do_Excel(path.excel_path).read(sheetname)

        for item in test_data:
            data=item['param']

            if data.find('tel_1')!=-1:
                item['param']=data.replace('tel_1',phone[0])

            elif data.find('tel_2')!=-1:
                item['param']=data.replace('tel_2',phone[1])

        for item in test_data:
            data = item['param']

            if data.find('usr_1')!=-1:
                item['param']=data.replace('usr_1',usr[0])

            elif data.find('usr_2')!=-1:
                item['param']=data.replace('usr_2',usr[1])

        for item in test_data:
            data = item['param']
            if data.find('truename_1')!=-1:
                item['param']=data.replace('truename_1',name)

        return test_data
















if __name__ == '__main__':

    result=Data().data('verifiedUserAuth')
    for i in result:
        print(i)
