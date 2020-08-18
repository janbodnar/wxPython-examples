#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program performs set operations on regions.

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

         self.SetTitle("Regions")
         self.Centre()

    def OnPaint(self, e):

         dc = wx.PaintDC(self)
         dc.SetPen(wx.Pen('#d4d4d4'))

         dc.DrawRectangle(20, 20, 50, 50)
         dc.DrawRectangle(30, 40, 50, 50)

         dc.SetBrush(wx.Brush('#ffffff'))
         dc.DrawRectangle(100, 20, 50, 50)
         dc.DrawRectangle(110, 40, 50, 50)

         region1 = wx.Region(100, 20, 50, 50)
         region2 = wx.Region(110, 40, 50, 50)
         region1.Intersect(region2)

         rect = region1.GetBox()
         dc.SetDeviceClippingRegion(region1)
         dc.SetBrush(wx.Brush('#ff0000'))
         dc.DrawRectangle(rect)
         dc.DestroyClippingRegion()

         dc.SetBrush(wx.Brush('#ffffff'))
         dc.DrawRectangle(180, 20, 50, 50)
         dc.DrawRectangle(190, 40, 50, 50)

         region1 = wx.Region(180, 20, 50, 50)
         region2 = wx.Region(190, 40, 50, 50)
         region1.Union(region2)
         dc.SetDeviceClippingRegion(region1)

         rect = region1.GetBox()
         dc.SetBrush(wx.Brush('#fa8e00'))
         dc.DrawRectangle(rect)
         dc.DestroyClippingRegion()

         dc.SetBrush(wx.Brush('#ffffff'))
         dc.DrawRectangle(20, 120, 50, 50)
         dc.DrawRectangle(30, 140, 50, 50)
         region1 = wx.Region(20, 120, 50, 50)
         region2 = wx.Region(30, 140, 50, 50)
         region1.Xor(region2)

         rect = region1.GetBox()
         dc.SetDeviceClippingRegion(region1)
         dc.SetBrush(wx.Brush('#619e1b'))
         dc.DrawRectangle(rect)
         dc.DestroyClippingRegion()

         dc.SetBrush(wx.Brush('#ffffff'))
         dc.DrawRectangle(100, 120, 50, 50)
         dc.DrawRectangle(110, 140, 50, 50)
         region1 = wx.Region(100, 120, 50, 50)
         region2 = wx.Region(110, 140, 50, 50)
         region1.Subtract(region2)

         rect = region1.GetBox()
         dc.SetDeviceClippingRegion(region1)
         dc.SetBrush(wx.Brush('#715b33'))
         dc.DrawRectangle(rect)
         dc.DestroyClippingRegion()

         dc.SetBrush(wx.Brush('#ffffff'))
         dc.DrawRectangle(180, 120, 50, 50)
         dc.DrawRectangle(190, 140, 50, 50)
         region1 = wx.Region(180, 120, 50, 50)
         region2 = wx.Region(190, 140, 50, 50)
         region2.Subtract(region1)

         rect = region2.GetBox()
         dc.SetDeviceClippingRegion(region2)
         dc.SetBrush(wx.Brush('#0d0060'))
         dc.DrawRectangle(rect)
         dc.DestroyClippingRegion()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
