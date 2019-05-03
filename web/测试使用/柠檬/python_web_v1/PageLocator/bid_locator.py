from selenium.webdriver.common.by import By

class Bid_Locator:
    # 获取投资金额输入框
    invest_input=(By.XPATH,"//input[contains(@class,'invest-unit-investinput')]")
    # 投标按钮
    invest_button=(By.XPATH,"//button[@class='btn btn-special height_style']")
    # 投资成功弹出框，查看并激活
    success_invest=(By.XPATH,"//div[@class='layui-layer-content']//button[text()='查看并激活']")
