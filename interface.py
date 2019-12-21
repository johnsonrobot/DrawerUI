import wx

class UIFrame(wx.Frame):
    def __init__(self, *args, **argv):
        super().__init__(None, size=(1000,500),title="Form")
        self.UIBar()
        self.Show()

    def UIBar(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        newitem = wx.MenuItem(filemenu, wx.ID_NEW, text="New", kind=wx.ITEM_NORMAL)
        filemenu.AppendItem(newitem)

        filemenu.AppendSeparator()

        savemenu = wx.MenuItem(filemenu, wx.ID_SAVE, text="Save", kind=wx.ITEM_NORMAL)
        filemenu.AppendItem(savemenu)

        exititem = wx.MenuItem(filemenu, wx.ID_EXIT, text="Exit", kind=wx.ITEM_NORMAL)
        filemenu.AppendItem(exititem)

        menubar.Append(filemenu, "File")
        self.SetMenuBar(menubar)
        self.text = wx.TextCtrl(self, -1, style=wx.EXPAND | wx.TE_MULTILINE)
        self.Bind(wx.EVT_MENU, self.menuhandler)
        
    def menuhandler(self, event):
        id = event.GetId()
        if(id == wx.ID_EXIT):
            self.Close()
        elif(id == wx.ID_NEW):
            self.text.AppendText("You click the new item on the menubar\n")

def main():
    app = wx.App()
    UIFrame(wx.Frame)
    app.MainLoop()

main()

