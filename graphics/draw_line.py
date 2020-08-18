#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program draws a line on the
frame window after a while.

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

        wx.CallLater(2000, self.DrawLine)

        self.SetTitle("Line")
        self.Centre()

    def DrawLine(self):

        dc = wx.ClientDC(self)
        dc.DrawLine(50, 60, 190, 60)

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
