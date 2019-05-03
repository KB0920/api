# alert 弹框操作
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# alter操作
driver=webdriver.Chrome()
# 第一种方法
alert=driver.switch_to.alert
# 关闭弹框，接受弹框
alert.accept()
# 打印弹框文本
print(alert.text)
# 关闭弹窗，拒绝弹框
alert.dismiss()
# 弹出框输入操作
alert.send_keys()

# 第二种方法
WebDriverWait(driver,20).until(EC.alert_is_present())
# 自己之后要再一次切换，因为要有一个返回值进行接受
alert = driver.switch_to.alert

