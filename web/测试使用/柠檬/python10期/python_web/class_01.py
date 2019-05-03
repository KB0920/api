# python selenium库
from selenium import webdriver
# 启动谷歌浏览器
driver=webdriver.Chrome()

# 访问一个网址
driver.get("http://www.baidu.com")

# id 定位
driver.find_element_by_id("kw")

# class_name 定位 只能选择一个class_name的值，不能有多个
driver.find_element_by_class_name('s_ipt')
# 只找一个元素的值（第一个）

# 找页面中所有匹配表达式的所有元素
driver.find_elements_by_class_name("s_ipt")
# 返回值应该是一个列表

# tag_name 定位
driver.find_element_by_tag_name("input")

# name 定位 有name属性可以通过那么进行定位
driver.find_element_by_name('wd')

# 查找（a元素）链接 精确和模糊查找 通过a元素的文本内容
driver.find_elements_by_link_text("更多产品")#（精确查找）
driver.find_element_by_partial_link_text("更多")#（模糊查找）
# 都是只通过元素的单一属性进行定位

# xpath定位
# 在实际的项目中
# 绝对定位，非常依赖于元素的位置的，如果位置有一点的变化就会很麻烦
# 在自己定位的时候一定不要用绝对定位 以单斜杠开头，从根节点开始，严格按照顺序和位置来表达
#
# 相对定位 相对于html的结尾
# 以双斜杠开头，不管元素的位置和顺序，在html中只管有没有，不管位置
# 在html页面中 Ctrl+f 弹出 可以寻找xpath css
# //标签名（*代表所有元素）[@属性=属性值] 如果找到不止一个的话可以用and 或者 or 进行逻辑查询 直到找到唯一的元素位置
# 不要去手写，用copy就好了
# 层级定位 先找到一个祖先节点，再在祖先后代中查找元素
# 函数使用
# text():元素的text内容
# 例：//div[@id='xx' and text()='文本内容']
# contains(@属性/text(),value) 包含函数
# //a[contains(@title,"html+dom")]
# 轴定位(万不得已就用轴定位)
# ancestor：祖先结点包括父结点
# parent：父结点
# preceding：当前元素结点标签之前的所有结点（html页面顺序）
# preceding-sibling：当前元素结点标签之前的所有兄弟结点
# following：当前元素结点标签之后的所有结点（html页面顺序）
# following-sibling：当前元素结点标签之后的所有兄弟结点
# //标签[@属性="XX"]/定位名::其他结点标签名[@属性="XX"]
# css_selector
# 可以简单了解一下
