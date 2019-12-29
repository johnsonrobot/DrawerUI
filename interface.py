import wx
import os
import webbrowser

class UIFrame(wx.Frame):
    autoid = wx.NewId()
    def __init__(self, *args, **argv):
        super().__init__(None,title="Form")
        self.textIsChange = False
        self.fileIsOpen = False
        self.fileName = "Untitled"
        self.filePath = ""
        self.wildcard = "*"
        self.InitUI()

    def InitUI(self):
        self.UIBar()
        self.StatBar()    
        self.MainWin()
        self.adjustWin()

    def adjustWin(self):
        self.SetSize((1000, 500))
        self.Center()
        self.Show()

    def StatBar(self):
        self.statbar = wx.StatusBar(self, -1)
        self.statbar.SetFieldsCount(2)
        self.statbar.SetStatusWidths([-2, -1])
        self.statbar.SetStatusText("row:1, col:1", 1)
        self.SetStatusBar(self.statbar)
        self.statbar.Show()
    
    def MainWin(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.text = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE | wx.NO_BORDER)
        self.text.Bind(wx.EVT_TEXT, self.eventtext)
        vbox.Add(self.text, proportion=1, flag = wx.EXPAND | wx.ALL)
        panel.SetSizer(vbox)

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

        filemenu.AppendSeparator()

        exititem = wx.MenuItem(filemenu, wx.ID_EXIT, text="Exit", kind=wx.ITEM_NORMAL)
        filemenu.AppendItem(exititem)

        menubar.Append(filemenu, "File")

        editmenu = wx.Menu()
        
        self.revid = wx.NewId()
        recoveritem = wx.MenuItem(editmenu, self.revid, text="undo", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(recoveritem)

        editmenu.AppendSeparator()

        cutitem = wx.MenuItem(editmenu, wx.ID_CUT, text="cut", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(cutitem)

        copyitem = wx.MenuItem(editmenu, wx.ID_COPY, text="copy", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(copyitem)

        pasteitem = wx.MenuItem(editmenu, wx.ID_PASTE, text="paste", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(pasteitem)

        delitem = wx.MenuItem(editmenu, wx.ID_DELETE, text="Del", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(delitem)

        editmenu.AppendSeparator()
        
        finditem = wx.MenuItem(editmenu, wx.ID_FIND, text="find", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(finditem)

        self.nextid = wx.NewId()
        nextitem = wx.MenuItem(editmenu, self.nextid, text="Next", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(nextitem)

        repitem = wx.MenuItem(editmenu, wx.ID_REPLACE, text="Replace", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(repitem)

        self.traid = wx.NewId()
        traitem = wx.MenuItem(editmenu, self.traid, text="Transfer", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(traitem)

        editmenu.AppendSeparator()

        allitem = wx.MenuItem(editmenu, wx.ID_SELECTALL, text="All", kind=wx.ITEM_NORMAL)
        editmenu.AppendItem(allitem)

        self.timeid = wx.NewId()
        timeitem = wx.MenuItem(editmenu, self.timeid, text="Time/Date", kind=wx.ITEM_NORMAL)
        
        menubar.Append(editmenu, "Edit")

        formatMenu = wx.Menu()

        # self.autoid = wx.NewId()
        formatMenu.Append(id = self.autoid, item = "Auto" , kind = wx.ITEM_CHECK)
        formatMenu.Append(id = wx.ID_SELECT_FONT, item = "Font" )

        menubar.Append (formatMenu, title = "format" )
  
        seeMenu = wx.Menu()
        
        self.statusid = wx.NewId()
        seeMenu.Append(id = self.statusid, item = "Status" , kind = wx.ITEM_CHECK)
  
        menubar.Append(seeMenu, title = "Search" )
  
        helpMenu = wx.Menu()

        helpMenu.Append(id = wx.ID_HELP, item = "Help")
        helpMenu.Append(id = wx.ID_ABOUT, item = "About")

        menubar.Append(helpMenu, title = "Help")
        
        self.SetMenuBar(menubar)
        # self.text = wx.TextCtrl(self.panel, -1, size=self.GetSize(), style= wx.TE_MULTILINE | wx.NO_BORDER)
        # self.text.Refresh()
        self.Bind(wx.EVT_MENU, self.menuhandler)
        # self.Bind(wx.EVT_MAXIMIZE, self.formhandler)
        
    def menuhandler(self, event):
        id = event.GetId()
        if(id == wx.ID_EXIT):
            self.Close()
        elif(id == wx.ID_NEW):
            if(self.textIsChange):
                if(self.text.GetValue() == "" and self.fileIsOpen == False):
                    pass
                else:
                    dialog = wx.MessageDialog(self, "Save as " + self.fileName + "?", "TextBook", wx.CANCEL | wx.YES_NO)
                    ans = dialog.ShowModal()
                    if(ans == wx.ID_OK):
                        self.saveFile()
                    elif(ans == wx.ID_CANCEL):
                        return None
                    else:
                        pass
            self.fileIsOpen = False
            self.filePath = ""
            self.fileName = "Untitled"
            self.text.SetValue("")
            self.textIsChange = False

        elif(id == wx.ID_OPEN):
            if (self.textIsChange):
                dialog = wx.MessageDialog(self, "Save as " + self.fileName + "?", "TextBook", wx.CANCEL | wx.YES_NO)
                ans = dialog.ShowModal()
                if(ans == wx.ID_NO):
                    self.openFile()
                elif(ans == wx.ID_CANCEL):
                    pass
                else:
                    self.saveFile()
            else:
                self.openFile()

        elif(id == wx.ID_SAVE):
            self.saveFile()
            # filedig = wx.FileDialog(self, "Save", os.getcwd(), "", style=wx.FD_SAVE)
            # if(filedig.ShowModal() == wx.ID_OK):
            #     file = open(filedig.GetPath(), "w")
            #     file.write(self.text.GetValue())
            #     file.close()
            # filedig.Destroy()
        
        elif(id == wx.ID_ABOUT):
            aboutdig = wx.MessageDialog(parent=None, message="hihi", caption="about textbook", style=wx.OK)
            aboutdig.ShowModal()
        
        elif(id == wx.ID_HELP):
            url = "https://www.google.com.tw/"
            webbrowser.open(url)

        elif(id == self.autoid):
            if(not event.IsChecked()):
                self.text.SetWindowStyleFlag(style=wx.TE_MULTILINE | wx.HSCROLL)
                self.statbar.Show(True)
                self.SetSize((self.GetSize()[0], (self.GetSize()[1] + 1)))
            
            else:
                self.text.SetWindowStyleFlag(style=wx.TE_MULTILINE)
                self.statbar.Show(False)
                self.SetSize((self.GetSize()[0], (self.GetSize()[1] - 1)))
        
        elif(id == self.statusid):
            if(not event.IsChecked()):
                self.statbar.Show(True)
                self.SetSize(self.GetSize()[0], (self.GetSize()[1] + 1))
            else:
                self.statbar.Show(False)
                self.SetSize(self.GetSize()[0], (self.GetSize()[1] - 1))


        elif(id == wx.ID_SELECTALL):
            self.text.SelectAll()

        elif(id == wx.ID_CUT):
            self.text.Cut()

        elif(id == wx.ID_COPY):
            self.text.Copy()

        elif(id == wx.ID_PASTE):
            self.text.Paste()

        elif(id == wx.ID_SELECT_FONT):
            dialog = wx.FontDialog(self, wx.FontData())
            if(dialog.ShowModal() == wx.ID_OK):
                data = dialog.GetFontData()
                font = data.GetChosenFont()
                color = data.GetColour()
                self.text.SetFont(font)
                self.text.SetForegroundColour(color)
            dialog.Destroy()
        
    def formhandler(self, event):
        #id = event.GetId()
        if(self.IsMaximized()):
            self.text = wx.TextCtrl(self.panel, -1, size=(1920, 1080), style= wx.TE_MULTILINE | wx.NO_BORDER)
            self.text.Refresh()

    def eventtext(self, event):
        self.textIsChange = True

    def saveFile(self):
        if not self.fileIsOpen:
            wildcard = self.wildcard
            dlg = wx.FileDialog(self, "Save", wildcard=wildcard, style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
            if dlg.ShowModal() == wx.ID_OK:
                filePath = dlg.GetPath()
            else:
                return False
        else:
            filePath = self.filePath
        with open(filePath, "w") as f:
            f.write(self.text.GetValue())
            self.textIsChange = False
        return True

    def openFile(self):
        wildcard = self.wildcard
        dialog = wx.FileDialog(self, "Open", style=wx.FD_OPEN, wildcard=wildcard)
        if(dialog.ShowModal() == wx.ID_OK):
            filePath = dialog.GetPath()
            with open(filePath, "r") as f:
                self.text.SetValue(f.read())
                self.fileIsOpen = True
                self.filePath = filePath
                self.fileName = f.name
                self.textIsChange = False
                self.changeTitle()
        else:
            pass

    def changeTitle(self):
        self.SetTitle(self.fileName + "- TextBook")

def main():
    app = wx.App()
    UIFrame(wx.Frame)
    app.MainLoop()

main()

