#coding:utf-8
import wx
class Client(wx.Frame):
    def __init__(self,client_name):
        #调用父类初始化
        #id为窗体编号，pos为窗体打开位置，size是窗体大小单位为像素
        wx.Frame.__init__(self,None,id=1001,title=client_name+'的客户端',pos=wx.DefaultPosition,size=(400,500))
        #创建面板对象
        pl=wx.Panel(self)
        #在面板上放置盒子
        box=wx.BoxSizer(wx.VERTICAL)#垂直方向布局
        #可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL)#水平方向布局

        #创建两个按钮
        conn_btn=wx.Button(pl,size=(200,40),label='连接')
        disconn_btn = wx.Button(pl, size=(200, 40), label='断开')

        #把两个按钮放到可伸缩的网络布局
        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(disconn_btn, 1, wx.TOP | wx.RIGHT)

        #可伸缩网络布局添加到BOX,并居中对齐
        box.Add(fgz1,1,wx.ALIGN_CENTRE)

        #只读文本框，显示聊天内容
        self.show_text=wx.TextCtrl(pl,size=(400,210),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTRE)

        #创建聊天内容文本框
        self.chat_text=wx.TextCtrl(pl,size=(400,120),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.chat_text,1,wx.ALIGN_CENTRE)

        #可伸缩的网格布局
        fgz2=wx.FlexGridSizer(wx.HSCROLL)#水平方向布局
        #创建两个按钮
        reset_btn=wx.Button(pl,size=(200,40),label='重置')
        send_btn=wx.Button(pl,size=(200,40),label='发送')

        fgz2.Add(reset_btn, 1, wx.TOP | wx.LEFT)
        fgz2.Add(send_btn, 1, wx.TOP | wx.LEFT)

        box.Add(fgz2, 1, wx.ALIGN_CENTRE)
        #将盒子放置在面板中
        pl.SetSizer(box)

if __name__ == '__main__':
    #初始化APP
    app=wx.App()
    #创建自己的客户端界面对象
    client=Client('FRIST_APP')
    client.Show()
    app.MainLoop()



