#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode wxPython tutorial

In this example, we drag and drop files.

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

import wx

class FileDrop(wx.FileDropTarget):

    def __init__(self, window):

        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):

        for name in filenames:

            try:
                file = open(name, 'r')
                text = file.read()
                self.window.WriteText(text)

            except IOError as error:

                dlg = wx.MessageDialog(None, 'Error opening file\n' + str(error))
                dlg.ShowModal()

                return False

            except UnicodeDecodeError as error:

                dlg = wx.MessageDialog(None, 'Cannot open non ascii files\n' + str(error))
                dlg.ShowModal()

                return False

            finally:
                print("I am here")
                file.close()

        return True

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.text = wx.TextCtrl(self, style = wx.TE_MULTILINE)
        dt = FileDrop(self.text)

        self.text.SetDropTarget(dt)

        self.SetTitle('File drag and drop')
        self.Centre()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
