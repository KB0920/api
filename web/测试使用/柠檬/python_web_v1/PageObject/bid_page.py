from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocator.bid_locator import Bid_Locator as BL

class BidPage:
    def __init__(self,driver):
        self.driver=driver

    # 获取余额
    def get_usermoney(self):
        WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located(BL.invest_input))
        return self.driver.find_element(*BL.invest_input).get_attribute('data-amount')

    # 投资操作
    def invest(self,money):
        # 输入金钱
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(BL.invest_input))
        # 滚动到可见区域
        self.driver.find_element(*BL.invest_input).send_keys(money)
        # 点击投资按钮
        self.driver.find_element(*BL.invest_button).click()

    # 投资成功过弹出框 -查看并激活
    def success_invest_button(self):
        WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located(BL.success_invest))
        self.driver.find_element(*BL.success_invest).click()