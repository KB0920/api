from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# 切换操作 driver.switch_to
# 1.窗口切换
# 代码不会主动跳转到新的html页面，只会在自己的窗口中进行操作
# 想在新的页面中进行操作，就要主动将当前页面换为新打开的页面
# 目前只能通过句柄来进行页面切换，还没有通过title进行切换

driver= webdriver.Chrome()

# driver.implicitly_wait(30)

driver.get("https://www.baidu.com")
driver.maximize_window()
# get 之后的是不需要等待的
driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()

# 点击百度贴吧
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@tpl="tieba_general"]//a[text()="吧_百度贴吧"]')))
driver.find_element_by_xpath('//div[@tpl="tieba_general"]//a[text()="吧_百度贴吧"]').click()

# 切换到新的窗口
# 第一种方式
# 1.获取所有的窗口
windows= driver.window_handles
print("目前所有的窗口：",windows)

# 2.打印当前的窗口
current_handle=driver.current_window_handle
print("当前的窗口：",current_handle)

# 3.切换到最新出现的窗口
driver.switch_to.window(windows[-1])

# 4.打印切换后的窗口
current_handle=driver.current_window_handle
print("切换后的窗口：",current_handle)

# 第二种方式
# 通过EC函数中的等待新窗口打开操作
# 点击百度贴吧
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//div[@tpl="tieba_general"]//a[text()="吧_百度贴吧"]')))
# 1.获取所有的窗口
windows = driver.window_handles
print("目前所有的窗口：", windows)

driver.find_element_by_xpath('//div[@tpl="tieba_general"]//a[text()="吧_百度贴吧"]').click()
# 等待新窗口的出现
WebDriverWait(driver,10).until(EC.new_window_is_opened(windows))

# 新窗口增加之后的所有窗口
windows=driver.window_handles
# 切换窗口
driver.switch_to.window(windows[-1])
# 点击关注操作
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"j_head_focus_btn")))
driver.find_element_by_id("j_head_focus_btn").click()




# driver.quit()