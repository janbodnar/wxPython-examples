#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

This is a complex wx.ListCtrl example.

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

import wx

articles = [['Mozilla rocks', 'The year of the Mozilla', 'Earth on Fire'],
  ['Gnome is leading', 'Gnome, KDE, Icewm, XFCE', 'Where is Gnome heading?'],
  ['Java number one language', 'Compiled languages, intrepreted Languages',
  'Java on Desktop?']]


class ListCtrlLeft(wx.ListCtrl):

    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT | wx.LC_HRULES |
	        	wx.LC_NO_HEADER | wx.LC_SINGLE_SEL)
        images = ['java.png', 'gnome.png', 'firefox.png']

        self.parent = parent

        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelect)

        self.il = wx.ImageList(80, 80)

        for i in images:
            self.il.Add(wx.Bitmap(i))

        self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        self.InsertColumn(0, '')

        for i in range(3):

            self.InsertItem(0, '')
            self.SetItemImage(0, i)

    def OnSize(self, event):

        size = self.parent.GetSize()
        self.SetColumnWidth(0, size.x-5)
        event.Skip()

    def OnSelect(self, event):

        window = self.parent.GetGrandParent().FindWindowByName('ListControlOnRight')
        index = event.GetIndex()
        window.LoadData(index)

    def OnDeSelect(self, event):

        index = event.GetIndex()
        self.SetItemBackgroundColour(index, 'WHITE')

    def OnFocus(self, event):
        self.SetItemBackgroundColour(0, 'red')

class ListCtrlRight(wx.ListCtrl):

    def __init__(self, parent):

        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT |
                wx.LC_HRULES | 	wx.LC_NO_HEADER | wx.LC_SINGLE_SEL)

        self.parent = parent

        self.Bind(wx.EVT_SIZE, self.OnSize)

        self.InsertColumn(0, '')


    def OnSize(self, event):

        size = self.parent.GetSize()
        self.SetColumnWidth(0, size.x-5)
        event.Skip()

    def LoadData(self, index):

        self.DeleteAllItems()

        for i in range(3):
            self.InsertItem(0, articles[index][i])


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        splitter = wx.SplitterWindow(self, style=wx.SP_LIVE_UPDATE | wx.SP_NOBORDER)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        panel1 = wx.Panel(splitter)
        panel11 = wx.Panel(panel1, size=(-1, 40))

        panel11.SetBackgroundColour('#53728c')
        st1 = wx.StaticText(panel11, wx.ID_ANY, 'Feeds', (5, 5))
        st1.SetForegroundColour('WHITE')

        panel12 = wx.Panel(panel1, style=wx.BORDER_SUNKEN)
        vbox = wx.BoxSizer(wx.VERTICAL)
        list1 = ListCtrlLeft(panel12)

        vbox.Add(list1, 1, wx.EXPAND)
        panel12.SetSizer(vbox)
        panel12.SetBackgroundColour('WHITE')

        vbox1.Add(panel11, 0, wx.EXPAND)
        vbox1.Add(panel12, 1, wx.EXPAND)

        panel1.SetSizer(vbox1)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        panel2 = wx.Panel(splitter)
        panel21 = wx.Panel(panel2, size=(-1, 40), style=wx.NO_BORDER)

        st2 = wx.StaticText(panel21, wx.ID_ANY, 'Articles', (5, 5))
        st2.SetForegroundColour('WHITE')

        panel21.SetBackgroundColour('#53728c')
        panel22 = wx.Panel(panel2, style=wx.BORDER_RAISED)
        vbox3 = wx.BoxSizer(wx.VERTICAL)

        list2 = ListCtrlRight(panel22)
        list2.SetName('ListControlOnRight')
        vbox3.Add(list2, 1, wx.EXPAND)
        panel22.SetSizer(vbox3)


        panel22.SetBackgroundColour('WHITE')
        vbox2.Add(panel21, 0, wx.EXPAND)
        vbox2.Add(panel22, 1, wx.EXPAND)

        panel2.SetSizer(vbox2)

        toolbar = self.CreateToolBar()
        toolbar.AddTool(1, 'Exit', wx.Bitmap('stock_exit.png'))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.ExitApp, id=1)

        hbox.Add(splitter, 1, wx.EXPAND | wx.TOP | wx.BOTTOM, 5)
        self.SetSizer(hbox)
        self.CreateStatusBar()
        splitter.SplitVertically(panel1, panel2, 100)

        self.SetTitle('Reader')
        self.Centre()


    def ExitApp(self, event):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
