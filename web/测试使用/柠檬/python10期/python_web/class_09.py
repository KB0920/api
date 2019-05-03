# 键盘操作
# selenium中有key类来模拟键盘操作
# 在实际中按键操作并不多
# 组合键
# send_keys(Keys.CONTROL,'a')       全选
# send_keys(Keys.CONTROL,'c')       复制
# send_keys(Keys.CONTROL,'x')       剪切
# send_keys(Keys.CONTROL,'v')       粘贴

# 非组合键
# Keys.ENTER                        回车键
# Keys.BACK_SPACE                   后退键
# Keys.SPACE                        空格键
# Keys.TAB                          制表键
# Keys.F5                           刷新键

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

