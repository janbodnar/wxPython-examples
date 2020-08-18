#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this example we create spin control.

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

        sizer = wx.GridBagSizer(5, 5)

        st1 = wx.StaticText(pnl, label='Convert Fahrenheit temperature to Celsius')
        sizer.Add(st1, pos=(0, 0), span=(1, 2), flag=wx.ALL, border=15)

        st2 = wx.StaticText(pnl, label='Fahrenheit:')
        sizer.Add(st2, pos=(1, 0), flag=wx.ALL | wx.ALIGN_CENTER, border=15)
        self.sc = wx.SpinCtrl(pnl, value='0')
        self.sc.SetRange(-459, 1000)

        sizer.Add(self.sc, pos=(1, 1), flag=wx.ALIGN_CENTER)

        st3 = wx.StaticText(pnl, label='Celsius:')
        sizer.Add(st3, pos=(2, 0), flag=wx.ALL|wx.ALIGN_RIGHT, border=15)

        self.celsius = wx.StaticText(pnl, label='')
        sizer.Add(self.celsius, pos=(2, 1), flag=wx.ALL, border=15)

        computeButton = wx.Button(pnl, label='Compute')
        computeButton.SetFocus()
        sizer.Add(computeButton, pos=(3, 0), flag=wx.ALIGN_RIGHT|wx.TOP, border=30)

        closeButton = wx.Button(pnl, label='Close')
        sizer.Add(closeButton, pos=(3, 1), flag=wx.ALIGN_LEFT|wx.TOP, border=30)

        computeButton.Bind(wx.EVT_BUTTON, self.OnCompute)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        pnl.SetSizer(sizer)

        self.SetTitle('wx.SpinCtrl')
        self.Centre()

    def OnClose(self, e):

        self.Close(True)

    def OnCompute(self, e):

        fahr = self.sc.GetValue()
        cels = round((fahr - 32) * 5 / 9.0, 2)
        self.celsius.SetLabel(str(cels))


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
