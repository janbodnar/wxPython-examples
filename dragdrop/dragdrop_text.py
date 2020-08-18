#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this example, we drag and drop text data.

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

from pathlib import Path
import os
import wx

class MyTextDropTarget(wx.TextDropTarget):

    def __init__(self, object):

        wx.TextDropTarget.__init__(self)
        self.object = object

    def OnDropText(self, x, y, data):

        self.object.InsertItem(0, data)
        return True


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        splitter1 = wx.SplitterWindow(self, style=wx.SP_3D)
        splitter2 = wx.SplitterWindow(splitter1,  style=wx.SP_3D)

        home_dir = str(Path.home())

        self.dirWid = wx.GenericDirCtrl(splitter1, dir=home_dir, style=wx.DIRCTRL_DIR_ONLY)
        self.lc1 = wx.ListCtrl(splitter2, style=wx.LC_LIST)
        self.lc2 = wx.ListCtrl(splitter2, style=wx.LC_LIST)

        dt = MyTextDropTarget(self.lc2)
        self.lc2.SetDropTarget(dt)
        self.Bind(wx.EVT_LIST_BEGIN_DRAG, self.OnDragInit, id=self.lc1.GetId())

        tree = self.dirWid.GetTreeCtrl()

        splitter2.SplitHorizontally(self.lc1, self.lc2, 150)
        splitter1.SplitVertically(self.dirWid, splitter2, 200)

        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelect, id=tree.GetId())

        self.OnSelect(0)

        self.SetTitle('Drag and drop text')
        self.Centre()

    def OnSelect(self, event):

        list = os.listdir(self.dirWid.GetPath())

        self.lc1.ClearAll()
        self.lc2.ClearAll()

        for i in range(len(list)):

            if list[i][0] != '.':
                self.lc1.InsertItem(0, list[i])

    def OnDragInit(self, event):

        text = self.lc1.GetItemText(event.GetIndex())
        tdo = wx.TextDataObject(text)
        tds = wx.DropSource(self.lc1)

        tds.SetData(tdo)
        tds.DoDragDrop(True)


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
