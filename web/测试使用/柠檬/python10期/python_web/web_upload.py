import win32gui
import win32con

class UpLoad():
    def __init__(self,filepath):
        self.filepath=filepath
    def upload(self):
        # 一级窗口
        dialog=win32gui.FindWindow("#32770","打开")
        # win32gui.FindWindow(IpClassName,IpWindowName)
        # IpClassName:类名，在spy++中能够看到
        # IpWindowName：窗口名，标题栏上能够看到的名字

        # 二级窗口
        ComboBoxEx32=win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
        # win32gui.FindWindowEx(hwndParent=0,hwndChildAfter=0,IpszClass=None,IpszWindow=None)
        # hwndParent：父亲的窗口名是什么
        # hwndChildAfter：0代表所有的后代中从第一个开始搜索，知道最后一个
        # IpszClass：class属性
        # IpszWindow：文本内容

        # 三级窗口
        ComboBox=win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)
        # 四级窗口
        Edit=win32gui.FindWindowEx(ComboBox,0,"Edit",None)

        # 打开按钮
        button=win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")

        # 输入路径
        # win32gui.SendMessage(hWnd,Msg,wParam,iParam)
        # hWnd：整型，接受消息的窗口的句柄
        # Msg：整型，要发送消息，这些消息都是windows预先定义好的
        # wParam：整型，消息的wParam参数
        # iParam：整型，消息的iParam参数
        win32gui.SendMessage(Edit,win32con.WM_SETTEXT,None,self.filepath) #发送文件路径
        win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button) #点击打开按钮


if __name__ == '__main__':

    ul=UpLoad("D:\\Fiddler2.rar").upload()