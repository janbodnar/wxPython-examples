#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program draws a line in
a paint event.

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

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle("Line")
        self.Centre()

    def OnPaint(self, e):

        dc = wx.PaintDC(self)
        dc.DrawLine(50, 60, 190, 60)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
