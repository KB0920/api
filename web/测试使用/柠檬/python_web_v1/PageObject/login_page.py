from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocator.login_locator import Login_Locator as LL

class LoginPage:
    # 页面对象内部要分层，把定位也分出来，与功能分开
    def __init__(self,driver):
        self.driver=driver

    #登录操作
    def login(self,username,password):
        # 输入手机号
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(LL.user_input))
        self.driver.find_element(*LL.user_input).clear()
        self.driver.find_element(*LL.user_input).send_keys(username)
        # 输入密码
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(LL.password_input))
        self.driver.find_element(*LL.password_input).clear()
        self.driver.find_element(*LL.password_input).send_keys(password)
        # 点击登录
        self.driver.find_element(*LL.login_button).click()

    # 在密码下面的错误
    def page_error(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(LL.from_error_info))
        return self.driver.find_element(*LL.from_error_info).text

    # 在页面中心的错误
    def layer_error(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(LL.layer_connect))
        return self.driver.find_element(*LL.layer_connect).text

    # 等待登录按钮出现
    def wait_login(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(LL.login_button))
