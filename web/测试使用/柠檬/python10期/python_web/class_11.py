from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# PO模式 PageObject
# 分层设计，一个页面封装成为一个类，方便修改，为了大框架考虑
# 设计自动化测试用例
# 功能不能与测试用例混为一谈，在断言也要分层，用例就是行为调用或者输入测试数据
# 除了测试步骤和预期结果还要有前置条件，
# //input[@class="form-control username"]
# //input[@class="form-control"]
# //button[@class="btn btn-special"]

driver=webdriver.Chrome()
driver.maximize_window()

driver.get('http://120.79.176.157:8012/Index/login.html')

driver.find_element_by_xpath('//input[@class="form-control username"]').send_keys('18684720553')
driver.find_element_by_xpath('//input[@class="form-control"]').send_keys('python')
driver.find_element_by_xpath('//button[@class="btn btn-special"]').click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/Member/index.html']")))

