#!/usr/bin/python

'''
ZetCode Advanced wxPython tutorial

This program creates a
waiting effect in cairo.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
'''

import wx
import wx.lib.wxcairo
import cairo
import math


class cv(object):

    trs = (
        ( 0.0, 0.15, 0.30, 0.5, 0.65, 0.80, 0.9, 1.0 ),
        ( 1.0, 0.0,  0.15, 0.30, 0.5, 0.65, 0.8, 0.9 ),
        ( 0.9, 1.0,  0.0,  0.15, 0.3, 0.5, 0.65, 0.8 ),
        ( 0.8, 0.9,  1.0,  0.0,  0.15, 0.3, 0.5, 0.65 ),
        ( 0.65, 0.8, 0.9,  1.0,  0.0,  0.15, 0.3, 0.5 ),
        ( 0.5, 0.65, 0.8, 0.9, 1.0,  0.0,  0.15, 0.3 ),
        ( 0.3, 0.5, 0.65, 0.8, 0.9, 1.0,  0.0,  0.15 ),
        ( 0.15, 0.3, 0.5, 0.65, 0.8, 0.9, 1.0,  0.0, )
    )

    TIMER_ID = 1
    SPEED = 100
    CLIMIT = 1000
    NLINES = 8


class Board(wx.Panel):

        def __init__(self, *args, **kw):
            super(Board, self).__init__(*args, **kw)

            self.SetDoubleBuffered(True)
            self.Bind(wx.EVT_PAINT, self.OnPaint)

            self.InitBoard()


        def InitBoard(self):

            self.count = 0
            self.timer = wx.Timer(self, cv.TIMER_ID)
            self.timer.Start(cv.SPEED)

            self.Bind(wx.EVT_PAINT, self.OnPaint)
            self.Bind(wx.EVT_TIMER, self.OnTimer,
                id=cv.TIMER_ID)

            self.Centre()
            self.Show()


        def OnTimer(self, e):

            self.count = self.count + 1

            if self.count >= cv.CLIMIT:
                self.count = 0

            self.Refresh()


        def OnPaint(self, e):

            dc = wx.PaintDC(self)
            cr = wx.lib.wxcairo.ContextFromDC(dc)

            self.DoDrawing(cr)


        def DoDrawing(self, cr):

            w, h = self.GetClientSize()

            cr.set_line_width(3)
            cr.set_line_cap(cairo.LINE_CAP_ROUND)

            cr.translate(w/2, h/2)

            for i in range(cv.NLINES):

                cr.set_source_rgba(0, 0, 0,
                    cv.trs[self.count % cv.NLINES][i])
                cr.move_to(0.0, -10.0)
                cr.line_to(0.0, -40.0)
                cr.rotate(math.pi/4)
                cr.stroke()


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((250, 150))
        self.SetTitle("Waiting")
        self.Centre()
        self.Show()


    def InitUI(self):

        Board(self)


def main():

    app = wx.App()
    Example(None)
    app.MainLoop()


if __name__ == '__main__':
    main()
    
