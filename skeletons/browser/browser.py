#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program creates a browser UI.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

import wx
from wx.lib.buttons import GenBitmapTextButton

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.CreateMenuBar()

        panel = wx.Panel(self)
        # panel.SetBackgroundColour('white')

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        line1 = wx.StaticLine(panel)
        vbox.Add(line1, 0, wx.EXPAND)

        toolbar1 = wx.Panel(panel, size=(-1, 30))

        back = wx.BitmapButton(toolbar1, bitmap=wx.Bitmap('images/back.png'),
                style=wx.NO_BORDER)
        forward = wx.BitmapButton(toolbar1, bitmap=wx.Bitmap('images/forw.png'),
                style=wx.NO_BORDER)
        refresh = wx.BitmapButton(toolbar1, bitmap=wx.Bitmap('images/refresh.png'),
                style=wx.NO_BORDER)
        stop = wx.BitmapButton(toolbar1, bitmap=wx.Bitmap('images/stop.png'),
                style=wx.NO_BORDER)
        home = wx.BitmapButton(toolbar1, bitmap=wx.Bitmap('images/home.png'),
                style=wx.NO_BORDER)
        address = wx.ComboBox(toolbar1, size=(50, -1))
        go = wx.BitmapButton(toolbar1, bitmap=wx.Bitmap('images/play.png'),
                style=wx.NO_BORDER)
        text = wx.TextCtrl(toolbar1, size=(150, -1))

        hbox1.Add(back)
        hbox1.Add(forward)
        hbox1.Add(refresh)
        hbox1.Add(stop)
        hbox1.Add(home)
        hbox1.Add(address, 1, wx.TOP, 3)
        hbox1.Add(go, 0, wx.TOP | wx.LEFT, 3)
        hbox1.Add(text, 0, wx.TOP | wx.RIGHT, 3)

        toolbar1.SetSizer(hbox1)
        vbox.Add(toolbar1, 0, wx.EXPAND)
        line = wx.StaticLine(panel)
        vbox.Add(line, 0, wx.EXPAND)

        toolbar2 = wx.Panel(panel, size=(-1, 30))
        bookmark1 = wx.BitmapButton(toolbar2, bitmap=wx.Bitmap('images/love.png'),
                style=wx.NO_BORDER)
        bookmark2 = wx.BitmapButton(toolbar2, bitmap=wx.Bitmap('images/book.png'),
                style=wx.NO_BORDER)
        bookmark3 = wx.BitmapButton(toolbar2, bitmap=wx.Bitmap('images/sound.png'),
                style=wx.NO_BORDER)

        hbox2.Add(bookmark1, flag=wx.RIGHT, border=5)
        hbox2.Add(bookmark2, flag=wx.RIGHT, border=5)
        hbox2.Add(bookmark3)

        toolbar2.SetSizer(hbox2)
        vbox.Add(toolbar2, 0, wx.EXPAND)

        line2 = wx.StaticLine(panel)
        vbox.Add(line2, 0, wx.EXPAND)

        panel.SetSizer(vbox)

        self.CreateStatusBar()

        self.SetTitle("Browser")
        self.Centre()

    def CreateMenuBar(self):

        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(wx.ID_ANY, '&Quit', '')
        edit = wx.Menu()
        view = wx.Menu()
        go = wx.Menu()
        bookmarks = wx.Menu()
        tools = wx.Menu()
        help = wx.Menu()

        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(view, '&View')
        menubar.Append(go, '&Go')
        menubar.Append(bookmarks, '&Bookmarks')
        menubar.Append(tools, '&Tools')
        menubar.Append(help, '&Help')

        self.SetMenuBar(menubar)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
