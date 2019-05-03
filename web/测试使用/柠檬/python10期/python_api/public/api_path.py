#获取绝对路径
import os
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置文件路径
config_path=os.path.join(project_path,'config','case.config')

#测试用例路径
data_path=os.path.join(project_path,'test_data','API.xlsx')

#测试报告路径
report_path=os.path.join(project_path,'test_result','report','test.html')

#日志路径
log_path=os.path.join(project_path,'test_result','logs','logs.txt')

#数据库路径
sql_path=os.path.join(project_path,'config','db.config')