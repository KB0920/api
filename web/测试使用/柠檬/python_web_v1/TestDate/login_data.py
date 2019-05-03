# 正确登录
success_data={'user':'18684720553','password':'python'}
# 异常登录 用户名为空，密码为空,用户名密码都为空,手机号码格式不正确
error_data=[{'user':'','password':'python','check':'请输入手机号'},
            {'user':'18684720553','password':'','check':'请输入密码'},
            {'user':'','password':'','check':'请输入手机号'},
            {'user': '181231233', 'password': 'python', 'check': '请输入正确的手机号'},
            {'user': '181231233123125', 'password': 'python', 'check': '请输入正确的手机号'}]

# 手机号为注册，密码错误
wrong_data=[{'user': '18123123311', 'password': 'python', 'check': '此账号没有经过授权，请联系管理员!'},
            {'user': '18684720553', 'password': 'python1', 'check': '帐号或密码错误!'}]