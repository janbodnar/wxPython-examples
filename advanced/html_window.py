#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

In this example, we create a wx.html.HtmlWindow widget.

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

import wx
import wx.html

# page = '<html><body bgcolor="#8e8e95"><table cellspacing="5" border="0" width="250"> \
# <tr width="200" align="left"> \
# <td bgcolor="#e7e7e7">&nbsp;&nbsp;Maximum</td> \
# <td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>9000</b></td> \
# </tr> \
# <tr align="left"> \
# <td bgcolor="#e7e7e7">&nbsp;&nbsp;Mean</td> \
# <td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>6076</b></td> \
# </tr> \
# <tr align="left"> \
# <td bgcolor="#e7e7e7">&nbsp;&nbsp;Minimum</td> \
# <td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>3800</b></td> \
# </tr> \
# <tr align="left"> \
# <td bgcolor="#e7e7e7">&nbsp;&nbsp;Median</td> \
# <td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>6000</b></td> \
# </tr> \
# <tr align="left"> \
# <td bgcolor="#e7e7e7">&nbsp;&nbsp;Standard Deviation</td> \
# <td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>6076</b></td> \
# </tr> \
# </body></table></html>'


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        htmlwin = wx.html.HtmlWindow(panel, wx.ID_ANY, style=wx.NO_BORDER)
        # htmlwin.SetBackgroundColour(wx.RED)
        htmlwin.SetStandardFonts()
        htmlwin.LoadPage("page.html")

        vbox.Add((-1, 10), 0)
        vbox.Add(htmlwin, 1, wx.EXPAND | wx.ALL, 9)

        bitmap = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap('newt.png'))
        hbox.Add(bitmap, 0, wx.LEFT | wx.BOTTOM | wx.TOP, 10)
        btnOk = wx.Button(panel, wx.ID_ANY, 'Ok')

        self.Bind(wx.EVT_BUTTON, self.OnClose, id=btnOk.GetId())

        hbox.Add((100, -1), 1, wx.EXPAND | wx.ALIGN_RIGHT)
        hbox.Add(btnOk, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox, 0, wx.EXPAND)

        panel.SetSizer(vbox)

        self.SetTitle('Basic statistics')
        self.Centre()

    def OnClose(self, event):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
