#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

In this example we create buttons with standard ids.

author: Jan Bodnar
website: www.zetcode.com
last modified: April 2018
"""

import wx

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        pnl = wx.Panel(self)
        grid = wx.GridSizer(3, 2)

        grid.AddMany([(wx.Button(pnl, wx.ID_CANCEL), 0, wx.TOP | wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_DELETE), 0, wx.TOP, 9),
            (wx.Button(pnl, wx.ID_SAVE), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_EXIT)),
            (wx.Button(pnl, wx.ID_STOP), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_NEW))])

        self.Bind(wx.EVT_BUTTON, self.OnQuitApp, id=wx.ID_EXIT)

        pnl.SetSizer(grid)

        self.SetTitle("Standard ids")
        self.Centre()

    def OnQuitApp(self, event):

        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
