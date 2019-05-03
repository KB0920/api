from selenium.webdriver.common.by import By

class Login_Locator:
    # 用户名定位
    user_input = (By.XPATH,'//input[@class="form-control username"]')
    # 密码定位
    password_input = (By.XPATH,'//input[@class="form-control"]')
    # 按钮定位
    login_button = (By.XPATH,'//button[@class="btn btn-special"]')
    # 表单错误提示--用户名为空
    from_error_info = (By.XPATH,"//div[@class='form-error-info']")
    # 页面中间错误提示
    layer_connect = (By.XPATH,"//div[@class='layui-layer-content']")