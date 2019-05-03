from selenium.webdriver.common.by import By

class Index_Locator:
    # 用户昵称定位
    user_link = (By.XPATH,"//a[@href='/Member/index.html']")
    # 退出按键定位
    logout = (By.XPATH,"//a[@href='/Index/logout.html']")
    # 登录按键定位
    login = (By.XPATH,"//a[@href='/Index/login.html']")
    # 抢投标按钮定位
    bid_button=(By.XPATH,'//a[@class="btn btn-special"]')
