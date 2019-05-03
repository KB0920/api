# 控件处理的问题
# 输入框有两种
# 一种是可以输入的，直接手动输入即可
# 一种是只可以选择的，要先把属性删除，然后在进行输入



from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
# driver.get("http://www.12306.cn")
# # 选择起始城市
# # 选择终点城市
# # 保证稳定性，至少要在本地运行5次，一定要自己调试通过才可以
# # 如果调来调去总有不稳定，用js进行
#
# # 准备js语句
# js='var a=document.getElementById("train_date");' \
#    'a.readOnly=false;' \
#    'a.value="2019-02-01";'
# # 调用webdriver里的方法去执行js
# driver.execute_script(js)

# js滚动条
driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_id('kw').send_keys("柠檬班",Keys.ENTER)
# 等待
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="】_腾讯课堂"]')))
# 找到元素
element=driver.find_elements_by_xpath('//a[text()="】_腾讯课堂"]')
# 滚动到元素可见区域
driver.execute_script("arguments[0].scrollIntoView();",element[0])
# 滚动到元素可见底部
driver.execute_script("arguments[0].scrollIntoView(false);",element[0])
# 滚动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 滚动到页面顶部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight,0)")