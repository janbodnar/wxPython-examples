#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode Advanced wxPython tutorial

This program creates a puff
effect.

author: Jan Bodnar
website: zetcode.com
last edited: May 2012
"""

import wx
import wx.lib.wxcairo
#import cairo
import cairocffi as cairo

class cv(object):

    TIMER_ID = 1
    SPEED = 10


class Board(wx.Panel):

        def __init__(self, *args, **kw):
            super(Board, self).__init__(*args, **kw)

            self.InitExample()


        def InitExample(self):

            self.SetDoubleBuffered(True)

            self.alpha = 1.0
            self.font_size = 1.0

            self.timer = wx.Timer(self, cv.TIMER_ID)
            self.timer.Start(cv.SPEED)
            self.Bind(wx.EVT_TIMER,
                self.OnTimer, id=cv.TIMER_ID)

            self.Bind(wx.EVT_PAINT, self.OnPaint)


        def OnTimer(self, e):

            self.font_size = self.font_size + 0.8

            if self.font_size > 20:
                self.alpha = self.alpha - 0.01

            if self.alpha <= 0:
                self.timer.Stop()

            self.Refresh()


        def OnPaint(self, e):

            dc = wx.PaintDC(self)
            cr = wx.lib.wxcairo.ContextFromDC(dc)

            self.DoDrawing(cr)


        def DoDrawing(self, cr):

            w, h = self.GetClientSize()

            cr.set_source_rgb(0.5, 0, 0)
            cr.paint()

            cr.select_font_face("Sans",
                cairo.FONT_SLANT_NORMAL,
                cairo.FONT_WEIGHT_BOLD)

            cr.set_font_size(self.font_size)
            cr.set_source_rgb(1, 1, 1)

            _, _, width, _, _, _ = cr.text_extents("ZetCode")

            cr.move_to(w/2 - width/2, h/2)
            cr.text_path("ZetCode")
            cr.clip()
            cr.paint_with_alpha(self.alpha)


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()
        self.SetSize((340, 390))
        self.SetTitle("Puff")
        self.Centre()


    def InitUI(self):

        Board(self)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
