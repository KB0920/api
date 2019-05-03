# 等待
# 为了确保页面操作的稳定性
# 只要某一个操作导致页面发生了变化就需要等待
# sleep 强制等待 死等，很固话，很笨
# driver.implicitly_wait() 隐性等待
# 设置最长的等待时间，在这个时间内加载完成，则进行下一步
# 整个driver中设置一次即可，全局都可用 从webdriver.Chrome到quit
# 显性等待
# 明确等待某个条件满足后，再去执行下一步操作
# 程序每隔几秒看一下，如果条件成立就执行下一步，否则继续等待，知道超过设置的最长时间，然后抛出TimeoutException
# WebDriverWait类：显性等待类
# WebDriverWait(driver,等待时长,轮循周期).until()/until_not()
# driver：当前会话  until：直到达到条件就不等了  until_not：直到条件没有达到就不等了
# expected_conditions模块：提供了一系列期望发生的事件
# presence_of_element_located：元素存在
# visibility_of_element_located：元素可见
# element_to_be_clickable：元素可点击
# 以上三种均可以组合使用


import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



from selenium import webdriver

driver=webdriver.Chrome()
# driver.implicitly_wait(30)
driver.get("http://www.baidu.com")

driver.maximize_window()

driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_login']").click()

locator=(By.ID,'TANGRAM__PSP_10__footerULoginBtn')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))

driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

locator=(By.ID,'TANGRAM__PSP_10__userName')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))

driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys('1111111111111')
time.sleep(10)

driver.quit()