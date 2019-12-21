import wx

class UIFrame(wx.Frame):
    def __init__(self, *args, **argv):
        super().__init__(None, size=(1000,500),title="Form")
        self.Show()

def main():
    app = wx.App()
    UIFrame(wx.Frame)
    app.MainLoop()

main()

