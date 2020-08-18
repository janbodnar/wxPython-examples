#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program creates a Player UI.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.CreateMenuBar()

        panel = wx.Panel(self)

        pnl1 = wx.Panel(self)
        pnl1.SetBackgroundColour(wx.BLACK)
        pnl2 = wx.Panel(self)

        slider1 = wx.Slider(pnl2, value=18, minValue=0, maxValue=1000)
        pause = wx.BitmapButton(pnl2, bitmap=wx.Bitmap('images/pause.png'))
        play  = wx.BitmapButton(pnl2, bitmap=wx.Bitmap('images/play.png'))
        forw  = wx.BitmapButton(pnl2, bitmap=wx.Bitmap('images/forw.png'))
        back  = wx.BitmapButton(pnl2, bitmap=wx.Bitmap('images/back.png'))
        vol = wx.BitmapButton(pnl2, bitmap=wx.Bitmap('images/volume.png'))
        slider2 = wx.Slider(pnl2, value=1, minValue=0, maxValue=100,
            size=(120, -1))

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        hbox1.Add(slider1, proportion=1)
        hbox2.Add(pause)
        hbox2.Add(play, flag=wx.RIGHT, border=5)
        hbox2.Add(forw, flag=wx.LEFT, border=5)
        hbox2.Add(back)
        hbox2.Add((-1, -1), proportion=1)
        hbox2.Add(vol)
        hbox2.Add(slider2, flag=wx.TOP|wx.LEFT, border=5)

        vbox.Add(hbox1, flag=wx.EXPAND|wx.BOTTOM, border=10)
        vbox.Add(hbox2, proportion=1, flag=wx.EXPAND)
        pnl2.SetSizer(vbox)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(pnl1, proportion=1, flag=wx.EXPAND)
        sizer.Add(pnl2, flag=wx.EXPAND|wx.BOTTOM|wx.TOP, border=10)

        self.SetMinSize((350, 300))
        self.CreateStatusBar()
        self.SetSizer(sizer)

        self.SetSize((350, 200))
        self.SetTitle('Player')
        self.Centre()

    def CreateMenuBar(self):

        menubar = wx.MenuBar()
        filem = wx.Menu()
        play = wx.Menu()
        view = wx.Menu()
        tools = wx.Menu()
        favorites = wx.Menu()
        help = wx.Menu()

        filem.Append(wx.ID_ANY, '&quit', 'Quit application')

        menubar.Append(filem, '&File')
        menubar.Append(play, '&Play')
        menubar.Append(view, '&View')
        menubar.Append(tools, '&Tools')
        menubar.Append(favorites, 'F&avorites')
        menubar.Append(help, '&Help')

        self.SetMenuBar(menubar)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
