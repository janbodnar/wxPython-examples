#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

This program draws a line on the
frame window after a while.

author: Jan Bodnar
website: zetcode.com
last edited: April 28 2018
"""

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(350, 250))

        wx.CallLater(2000, self.DrawLine)

        self.Centre()

    def DrawLine(self):
        dc = wx.ClientDC(self)
        dc.DrawLine(50, 60, 190, 60)

if __name__ == '__main__':

    app = wx.App()
    ex = Example(None, 'Line')
    ex.Show()
    app.MainLoop()
