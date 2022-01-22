"""被enter键激活的显示部分程序"""
import wx

import picture_operate


class Frame(wx.Frame):
    """窗体类"""
    def __init__(self):
        """生成窗体"""
        # 从剪切板生成图片
        picture_operate.get_pic()
        # 读取本地图片为wxImage，之后转换生成bitmap对象
        img3 = wx.Image('picture.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        # 清理图片
        picture_operate.del_pic()
        # 初始化展示图片，None表示没有父节点，style通过参数调节没有边框
        # 框架的size通过图片的尺寸来自适应，位置用center函数取屏幕中央
        size = img3.GetSize()
        super().__init__(None, style=wx.SIMPLE_BORDER | wx.STAY_ON_TOP | wx.TRANSPARENT_WINDOW, size=size)
        self.Center(dir=wx.BOTH)
        # 显示图片，parent为self，图片自适应大小，填满Frame
        show3 = wx.StaticBitmap(self, bitmap=img3, size=size)
        # 关联事件，移动窗口，注意我们是用BitMap填满了Frame，所以要对BitMap绑定
        show3.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        show3.Bind(wx.EVT_MOTION, self.on_drag)
        show3.Bind(wx.EVT_LEFT_UP, self.on_left_up)

    def on_left_down(self, event):
        """左键按下"""
        pos = event.GetPosition()
        x, y = self.ClientToScreen(event.GetPosition())
        ox, oy = self.GetPosition()
        dx = x - ox
        dy = y - oy
        self.delta = ((dx, dy))

    def on_drag(self, event):
        """鼠标拖动"""
        if event.Dragging() and event.LeftIsDown():
            mouse = wx.GetMousePosition()
            self.Move((mouse.x - self.delta[0], mouse.y - self.delta[1]))

    def on_left_up(self, event):
        """左键放开"""
        if self.HasCapture():
            self.ReleaseMouse()


def main():
    app = wx.App()  # 创建app
    Frame().Show()  # 生成我的窗体类
    app.MainLoop()  # 循环

