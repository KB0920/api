from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocator.user_locator import User_Locator as UL

class UserPage:
    def __init__(self,driver):
        self.driver=driver

    def get_user_money(self):
        WebDriverWait(self.driver,20,0.5).until(EC.visibility_of_element_located(UL.user_leftmoney))
        money=self.driver.find_element(*UL.user_leftmoney).text
        return money.strip('元')