import wx

class ToolBar(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(500,500))

        menubar = wx.MenuBar()
        file = wx.Menu()
        help = wx.Menu()
        file.Append(101, '&Test', 'Run a Test')
        file.AppendSeparator()
        quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')
        file.AppendItem(quit)
        help.Append(201, '&Install', 'Install Required Tools')
        help.Append(202, '&Tutorials', 'Link to Tutorials')

        menubar.Append(file, '&File')
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)
        self.CreateStatusBar()

class AutomationApp(wx.App):
    def OnInit(self):
        frame = ToolBar(None, -1, 'Healthx Automation GUI')
        frame.Show(True)
        return True

app = AutomationApp(0)
app.MainLoop()