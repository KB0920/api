# -*- coding:utf-8 -*-
import os

file_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


excel_path=os.path.join(file_path,'Testdata','api.xlsx')

log_path=os.path.join(file_path,'Output','logs','log.txt')

report_path=os.path.join(file_path,'Output','reports','report.html')

conf_path=os.path.join(file_path,'Testconf','conf.config')

case_path=os.path.join(file_path,'Testcase')