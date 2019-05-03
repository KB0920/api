from python_接口测试.excel import DoExcel
from python_接口测试.request import HttpRequest

case=DoExcel('API.xlsx','API').read()
for item in case:
    res=HttpRequest().httprequest(item['module'],eval(item['param']),item['method'])

    if str(res['code'])==str(item['expected']):
        result='PASS'
    else:
        result='FAIL'
    DoExcel('API.xlsx','API').write(item['id']+1,res['code'],result)
