#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program creates a skeleton
of a file manager UI.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

import wx
import os
import time

ID_BUTTON=100
ID_EXIT=200
ID_SPLITTER=300


class MyListCtrl(wx.ListCtrl):

    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, style=wx.LC_REPORT)

        images = ['images/empty.png', 'images/folder.png', 'images/source-py.png',
		      'images/image.png', 'images/pdf.png', 'images/up16.png']

        self.InsertColumn(0, 'Name')
        self.InsertColumn(1, 'Ext')
        self.InsertColumn(2, 'Size', wx.LIST_FORMAT_RIGHT)
        self.InsertColumn(3, 'Modified')

        self.SetColumnWidth(0, 220)
        self.SetColumnWidth(1, 70)
        self.SetColumnWidth(2, 100)
        self.SetColumnWidth(3, 420)

        self.il = wx.ImageList(16, 16)

        for i in images:

            self.il.Add(wx.Bitmap(i))

        self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)

        j = 1

        self.InsertItem(0, '..')
        self.SetItemImage(0, 5)

        files = os.listdir('.')

        for i in files:

            (name, ext) = os.path.splitext(i)
            ex = ext[1:]
            size = os.path.getsize(i)
            sec = os.path.getmtime(i)

            self.InsertItem(j, name)
            self.SetItem(j, 1, ex)
            self.SetItem(j, 2, str(size) + ' B')
            self.SetItem(j, 3, time.strftime('%Y-%m-%d %H:%M', time.localtime(sec)))

            if os.path.isdir(i):
                self.SetItemImage(j, 1)
            elif ex == 'py':
                self.SetItemImage(j, 2)
            elif ex == 'jpg':
                self.SetItemImage(j, 3)
            elif ex == 'pdf':
                self.SetItemImage(j, 4)
            else:
                self.SetItemImage(j, 0)

            if (j % 2) == 0:

                self.SetItemBackgroundColour(j, '#e6f1f5')

            j = j + 1


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.splitter = wx.SplitterWindow(self, ID_SPLITTER, style=wx.SP_BORDER)
        self.splitter.SetMinimumPaneSize(50)

        p1 = MyListCtrl(self.splitter)
        p2 = MyListCtrl(self.splitter)
        self.splitter.SplitVertically(p1, p2)

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SPLITTER_DCLICK, self.OnDoubleClick, id=ID_SPLITTER)

        filemenu= wx.Menu()
        filemenu.Append(ID_EXIT, "E&xit"," Terminate the program")
        editmenu = wx.Menu()
        netmenu = wx.Menu()
        showmenu = wx.Menu()
        configmenu = wx.Menu()
        helpmenu = wx.Menu()

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        menuBar.Append(editmenu, "&Edit")
        menuBar.Append(netmenu, "&Net")
        menuBar.Append(showmenu, "&Show")
        menuBar.Append(configmenu, "&Config")
        menuBar.Append(helpmenu, "&Help")
        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_EXIT)

        tb = self.CreateToolBar( wx.TB_HORIZONTAL | wx.NO_BORDER |
		      wx.TB_FLAT)

        tb.AddTool(10, 'Previous', wx.Bitmap('images/previous.png'), shortHelp='Previous')
        tb.AddTool(20, 'Up', wx.Bitmap('images/up.png'), shortHelp='Up one directory')
        tb.AddTool(30, 'Home', wx.Bitmap('images/home.png'), shortHelp='Home')
        tb.AddTool(40, 'Refresh', wx.Bitmap('images/refresh.png'), shortHelp='Refresh')
        tb.AddSeparator()
        tb.AddTool(50, 'Edit text', wx.Bitmap('images/textedit.png'), shortHelp='Edit text')
        tb.AddTool(60, 'Terminal', wx.Bitmap('images/terminal.png'), shortHelp='Terminal')
        tb.AddSeparator()
        tb.AddTool(70, 'Help', wx.Bitmap('images/help.png'), shortHelp='Show help')
        tb.Realize()

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)

        button1 = wx.Button(self, ID_BUTTON + 1, "F3 View")
        button2 = wx.Button(self, ID_BUTTON + 2, "F4 Edit")
        button3 = wx.Button(self, ID_BUTTON + 3, "F5 Copy")
        button4 = wx.Button(self, ID_BUTTON + 4, "F6 Move")
        button5 = wx.Button(self, ID_BUTTON + 5, "F7 Mkdir")
        button6 = wx.Button(self, ID_BUTTON + 6, "F8 Delete")
        button7 = wx.Button(self, ID_BUTTON + 7, "F9 Rename")
        button8 = wx.Button(self, ID_EXIT, "F10 Quit")

        self.sizer2.Add(button1, 1, wx.EXPAND)
        self.sizer2.Add(button2, 1, wx.EXPAND)
        self.sizer2.Add(button3, 1, wx.EXPAND)
        self.sizer2.Add(button4, 1, wx.EXPAND)
        self.sizer2.Add(button5, 1, wx.EXPAND)
        self.sizer2.Add(button6, 1, wx.EXPAND)
        self.sizer2.Add(button7, 1, wx.EXPAND)
        self.sizer2.Add(button8, 1, wx.EXPAND)

        self.Bind(wx.EVT_BUTTON, self.OnExit, id=ID_EXIT)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.splitter,1,wx.EXPAND)
        self.sizer.Add(self.sizer2,0,wx.EXPAND)
        self.SetSizer(self.sizer)

        # size = wx.DisplaySize()
        # self.SetSize(size)

        sb = self.CreateStatusBar()
        sb.SetStatusText(os.getcwd())

        self.SetTitle("File Hunter")
        self.Center()


    def OnExit(self, e):

        self.Close(True)

    def OnSize(self, e):

        size = self.GetSize()
        self.splitter.SetSashPosition(size.x / 2)

        e.Skip()


    def OnDoubleClick(self, e):

        size = self.GetSize()
        self.splitter.SetSashPosition(size.x / 2)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
