from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocator.index_locator import Index_Locator as IL

class IndexPage:

    def __init__(self,driver):
        self.driver=driver
    # 判断用户昵称是否存在
    def is_user_link_exist(self):
        try:
            # 如果存在就返回ture
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(IL.user_link))
            return True
        except:
            # 如果不存在就返回false
            return False

    # 退出按钮点击
    def logout_button(self):
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(IL.logout))
        self.driver.find_element(*IL.logout).click()

    # 登录按钮点击
    def login_button(self):
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(IL.login))
        self.driver.find_element(*IL.login).click()

    # 点击强投标按钮
    def bid_button_click(self):
        WebDriverWait(self.driver,10,0.2).until(EC.visibility_of_element_located(IL.bid_button))
        # 页面滚动到元素可见的底部
        element=self.driver.find_element_by_xpath(IL.bid_button[1])
        self.driver.execute_script("arguments[0].scrollIntoView(false);",element)
        self.driver.find_element(*IL.bid_button).click()