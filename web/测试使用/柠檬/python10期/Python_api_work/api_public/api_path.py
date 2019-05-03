import os
#生成地址的模块
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置文件地址
config_path=os.path.join(project_path,'config','case_config')

#测试用例地址
excel_path=os.path.join(project_path,'test_data','api.xlsx')

#日志地址
log_path=os.path.join(project_path,'test_result','mylog','mylog.txt')

#测试报告地址
report_path=os.path.join(project_path,'test_result','report','test.html')

#数据库配置文件地址
mysql_path=os.path.join(project_path,'config','db.config')