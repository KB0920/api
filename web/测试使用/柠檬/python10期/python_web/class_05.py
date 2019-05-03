# iframe操作
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# 在一代一代中看到iframe，绝对要进行切换
# 在不切换的时候一样可以进行定位，但是在代码层面中一定要进行切换

driver=webdriver.Chrome()

driver.get("https://ke.qq.com")

# 第一种方法
# 切换
# 先等待，然后进行切换
# 可以通过index，name，webelement
driver.switch_to.frame("login_frame_qq")
driver.switch_to.frame(4)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='login_frame_qq']"))

# 之后操作iframe里面的html元素

# 操作之后，退出iframe页面，回到默认的html页面
driver.switch_to.default_content()
# 返回到上一级iframe页面,如果没有上一级，就保留自己
driver.switch_to.parent_frame()

# 第二种方法
# 等待和切换一期进行
# iframe可用并切换进去
# EC.frame_to_be_available_and_switch_to_it()
WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it('4'))
driver.find_element_by_xpath("XXX")
# 第二种方法可以提高代码的稳定性
