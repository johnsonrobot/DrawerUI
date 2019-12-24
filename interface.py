import wx
import os

class UIFrame(wx.Frame):
    def __init__(self, *args, **argv):
        super().__init__(None, size=(1000,500),title="Form")
        self.panel = wx.Panel(self)
        self.UIBar()
        self.Show()

    def UIBar(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()

        newitem = wx.MenuItem(filemenu, wx.ID_NEW, text="New", kind=wx.ITEM_NORMAL)
        filemenu.AppendItem(newitem)

        filemenu.AppendSeparator()

        openmenu = wx.MenuItem(filemenu, wx.ID_OPEN, text="Open", kind=wx.ITEM_NORMAL)
        filemenu.AppendItem(openmenu)

        savemenu = wx.MenuItem(filemenu, wx.ID_SAVE, text="Save", kind=wx.ITEM_NORMAL)
        filemenu.AppendItem(savemenu)

        exititem = wx.MenuItem(filemenu, wx.ID_EXIT, text="Exit", kind=wx.ITEM_NORMAL)
        filemenu.AppendItem(exititem)

        menubar.Append(filemenu, "File")
        self.SetMenuBar(menubar)
        self.text = wx.TextCtrl(self.panel, -1, size=self.GetSize(), style=wx.EXPAND | wx.TE_MULTILINE | wx.NO_BORDER)
        self.Bind(wx.EVT_MENU, self.menuhandler)
        self.Bind(wx.EVT_MAXIMIZE, self.formhandler)
        
    def menuhandler(self, event):
        id = event.GetId()
        if(id == wx.ID_EXIT):
            self.Close()
        elif(id == wx.ID_NEW):
            self.text.AppendText("You click the new item on the menubar\n")
        elif(id == wx.ID_OPEN):
            filedig = wx.FileDialog(self, "Open", os.getcwd(), "", style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
            if(filedig.ShowModal() == wx.ID_OK):
                file = open(filedig.GetPath())
                self.text.SetValue(file.read())
                file.close()
            filedig.Destroy()
        elif(id == wx.ID_SAVE):
            filedig = wx.FileDialog(self, "Save", os.getcwd(), "", style=wx.FD_SAVE)
            if(filedig.ShowModal() == wx.ID_OK):
                file = open(filedig.GetPath(), "w")
                file.write(self.text.GetValue())
                file.close()
            filedig.Destroy()

    def formhandler(self, event):
        #id = event.GetId()
        if(self.IsMaximized()):
            self.text = wx.TextCtrl(self.panel, -1, size=(1920, 1080), style=wx.EXPAND | wx.TE_MULTILINE | wx.NO_BORDER)
def main():
    app = wx.App()
    UIFrame(wx.Frame)
    app.MainLoop()

main()

