import unittest
from selenium import webdriver
from PageObject.login_page import LoginPage
from PageObject.index_page import IndexPage
from TestDate import common_data as CD
from TestDate import login_data as LD
from ddt import ddt,data


@ddt
class testlogin(unittest.TestCase):
    # 整个类里面只执行一次
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.url)
        cls.lp = LoginPage(cls.driver)
        cls.ip=IndexPage(cls.driver)

    def setUp(self):
        pass


    def tearDown(self):
        if self.driver.current_url!=CD.url:
            self.ip.logout_button()
            self.ip.login_button()
            self.driver.refresh()
        else:
            self.driver.refresh()

    # 这个类里只执行一次
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 正常登陆
    def test_login_success(self):
        self.lp.login(LD.success_data['user'],LD.success_data['password'])
        self.assertTrue(self.ip.is_user_link_exist())

    # 断言 是否进入了主页
    # 异常登陆，用户名为空
    @data(*LD.error_data)
    def test_page_error(self,item):
        self.lp.login(item['user'],item['password'])
        self.assertEqual(item['check'],self.lp.page_error())

    # 异常登录，密码为空
    @data(*LD.wrong_data)
    def test_layer_error(self,item):
        self.lp.login(item['user'],item['password'])
        self.assertEqual(item['check'],self.lp.layer_error())

