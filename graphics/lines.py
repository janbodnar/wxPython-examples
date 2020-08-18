#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program draws various shapes on
the window.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

import wx
from math import hypot, sin, cos, pi

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.SetTitle('Lines')
        self.Centre()

    def OnPaint(self, e):

        dc = wx.PaintDC(self)
        size_x, size_y = self.GetClientSize()
        dc.SetDeviceOrigin(size_x/2, size_y/2)

        radius = hypot(size_x/2, size_y/2)
        angle = 0

        while (angle < 2*pi):

            x = radius*cos(angle)
            y = radius*sin(angle)
            dc.DrawLine((0, 0), (x, y))

            angle = angle + 2*pi/360

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
