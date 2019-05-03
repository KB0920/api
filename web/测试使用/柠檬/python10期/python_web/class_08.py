# 鼠标操作
# 鼠标操作可以通过selenuim的ActionChains类完成模拟鼠标操作
# 可以单个操作可以连续操作

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.maximize_window()

# 鼠标悬浮到设置
# 1.先实例化ActionChains类
actionchains=ActionChains(driver)
# 2.鼠标行为
# 要先找到元素
element=driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_settingicon"]')
# 鼠标行为
actionchains.move_to_element(element).perform()
# 等待元素出现
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
# 单击操作
actionchains.click(driver.find_element_by_xpath('//a[text()="高级搜索"]')).perform()

# 等待元素可见
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
# driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

# 先等待
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//select[@name="ft"]')))
