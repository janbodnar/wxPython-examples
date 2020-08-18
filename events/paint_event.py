#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this example we count paint events.

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

        self.count = 0
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle('Paint events')
        self.SetSize((350, 250))
        self.Centre()

    def OnPaint(self, e):

        self.count += 1
        dc = wx.PaintDC(self)
        text = "Number of paint events: {0}".format(self.count)
        dc.DrawText(text, 20, 20)


def main():

    app = wx.App()
    ex  = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
