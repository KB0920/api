# -*- coding:utf-8 -*-
import os

real_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

excel_path=os.path.join(real_path,'test_data','API.xlsx')

log_path=os.path.join(real_path,'Output','logs','logs.txt')

report_path=os.path.join(real_path,'Output','report','report.html')

config_path=os.path.join(real_path,'test_config','conf.config')

case_path=os.path.join(real_path,'test_case')
