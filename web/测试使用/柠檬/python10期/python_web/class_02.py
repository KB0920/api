from selenium import webdriver

driver= webdriver.Chrome()
# 元素操作
# 1.浏览器操作
driver.get("https://www.baidu.com")
# driver.get("https://www.taobao.com")
# 浏览器全屏操作
driver.maximize_window()

# 输入操作
# driver.find_element_by_id('kw').send_keys("双十一")
# 按钮操作
# driver.find_element_by_id('su').click()
# 获取属性
# driver.find_element_by_id('su').get_attribute('type')
# 获取文本内容
# driver.find_element_by_id('su').text



# 设置浏览器的长宽高
# driver.set_window_size()
# # 前进
# driver.forward()
# # 后退
# driver.back()
# # 刷新
# driver.refresh()
# # 获取窗口标题
# print(driver.title)
# # 获取当前窗口的url
# print(driver.current_url)
# # 获取当前窗口的句柄
# print(driver.current_window_handle)
#
# # 关闭浏览器当前正在使用的窗口
driver.close()
# # 关闭整个浏览器会话，用代码主动杀掉浏览器
driver.quit()