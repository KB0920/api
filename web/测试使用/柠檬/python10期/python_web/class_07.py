# 下拉框操作
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.maximize_window()
# 暂时用点击操作代替鼠标悬浮操作
# 点击设置
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_settingicon"]').click()

# 等待元素可见
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

# 先等待
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//select[@name="ft"]')))

# select option 在selenium提供了Select类处理select/option
# 通过Select的方式就不用等元素可见和点击，直接选中元素即可
# 先实例化
select_element=driver.find_element_by_xpath('//select[@name="ft"]')
select=Select(select_element)
# 1.通过下标选择 从0开始
select.select_by_index(2) #这是第三个元素
time.sleep(4)
# 2.通过value属性选择
select.select_by_value('rtf') #通过元素的value属性来获取
time.sleep(4)
# 3.通过文本内容选择
select.select_by_visible_text('微软 Excel (.xls)')