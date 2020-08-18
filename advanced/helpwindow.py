#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this example, we create a help window window
with wx.html.HtmlWindow.

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

import wx
import wx.html as html

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        toolbar = self.CreateToolBar()
        toolbar.AddTool(1, 'Exit', wx.Bitmap('exit.png'))
        toolbar.AddTool(2, 'Help', wx.Bitmap('help.png'))
        toolbar.Realize()

        self.splitter = wx.SplitterWindow(self)
        self.panelLeft = wx.Panel(self.splitter, wx.ID_ANY, style=wx.BORDER_SUNKEN)

        self.panelRight = wx.Panel(self.splitter)
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        header = wx.Panel(self.panelRight, wx.ID_ANY)

        header.SetBackgroundColour('#6f6a59')
        header.SetForegroundColour('white')

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        st = wx.StaticText(header, wx.ID_ANY, 'Help')
        font = st.GetFont()
        font.SetFamily(wx.FONTFAMILY_ROMAN)
        font.SetPointSize(11)
        st.SetFont(font)

        hbox.Add(st, 1, wx.TOP | wx.BOTTOM | wx.LEFT, 8)

        closeBtn = wx.BitmapButton(header, wx.ID_ANY, wx.Bitmap('closebutton.png',
              wx.BITMAP_TYPE_PNG), style=wx.NO_BORDER)
        closeBtn.SetBackgroundColour('#6f6a59')

        hbox.Add(closeBtn, 0, wx.TOP|wx.BOTTOM, 8)
        header.SetSizer(hbox)

        vbox2.Add(header, 0, wx.EXPAND)

        helpWin = html.HtmlWindow(self.panelRight, style=wx.NO_BORDER)
        helpWin.LoadPage('help.html')

        vbox2.Add(helpWin, 1, wx.EXPAND)

        self.panelRight.SetSizer(vbox2)
        self.panelLeft.SetFocus()

        self.splitter.SplitVertically(self.panelLeft, self.panelRight)
        self.splitter.Unsplit()

        self.Bind(wx.EVT_BUTTON, self.CloseHelp, id=closeBtn.GetId())
        self.Bind(wx.EVT_TOOL, self.OnClose, id=1)
        self.Bind(wx.EVT_TOOL, self.OnHelp, id=2)

        self.panelLeft.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)
        self.panelLeft.SetFocus()

        self.CreateStatusBar()

        self.SetTitle('Help')
        self.Centre()

    def OnClose(self, e):
        self.Close()

    def OnHelp(self, e):

        self.splitter.SplitVertically(self.panelLeft, self.panelRight)
        self.panelLeft.SetFocus()

    def CloseHelp(self, e):

        self.splitter.Unsplit()
        self.panelLeft.SetFocus()

    def OnKeyPressed(self, e):

        keycode = e.GetKeyCode()
        print(keycode)

        if keycode == wx.WXK_F1:

            self.splitter.SplitVertically(self.panelLeft, self.panelRight)
            self.panelLeft.SetFocus()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
