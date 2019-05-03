import unittest
from selenium import webdriver
from TestDate import common_data as CD
from TestDate import invest_data as ID
from PageObject.login_page import LoginPage
from TestDate import login_data as LD
from PageObject.bid_page import BidPage
from PageObject.user_page import UserPage
from PageObject.index_page import IndexPage
# 投资前置
# 1.登录状态
# 2.又可以投资的标
# 3.账户余额足够

class Test_Invest(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get(CD.url)
        self.driver.maximize_window()
        self.bp= BidPage(self.driver)
        self.lp= LoginPage(self.driver)
        self.up=UserPage(self.driver)
        self.ip=IndexPage(self.driver)
        LoginPage(self.driver).login(LD.success_data['user'], LD.success_data['password'])


    def tearDown(self):
        self.driver.quit()

    def test_success(self):
        # 点击抢投标按钮
        self.ip.bid_button_click()
        # 获取可用余额
        user_money_old=self.bp.get_usermoney()
        # 输入投资金额
        self.bp.invest(ID.success_data['money'])
        # 点击查看并激活
        self.bp.success_invest_button()
        # 获取投资后的可用余额
        user_money_new=self.up.get_user_money()
        self.assertEqual(float(user_money_old)-ID.success_data['money'],float(user_money_new))

    def test_error(self):
        pass