#!/usr/bin/python

"""
ZetCode wxPython tutorial

This program creates a SpreadSheet UI.

author: Jan Bodnar
website: zetcode.com
last edited: May 2018
"""

from wx.lib import sheet
import wx


class MySheet(wx.grid.Grid):

    def __init__(self, *args, **kw):
        super(MySheet, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        nOfRows = 55
        nOfCols = 25

        self.row = self.col = 0
        self.CreateGrid(nOfRows, nOfCols)

        self.SetColLabelSize(20)
        self.SetRowLabelSize(50)

        self.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.OnGridSelectCell)

        for i in range(nOfRows):
            self.SetRowSize(i, 20)

        for i in range(nOfCols):
            self.SetColSize(i, 75)

    def OnGridSelectCell(self, e):

        self.row, self.col = e.GetRow(), e.GetCol()

        control = self.GetParent().GetParent().position
        value =  self.GetColLabelValue(self.col) + self.GetRowLabelValue(self.row)
        control.SetValue(value)

        e.Skip()


class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        fonts = ['Times New Roman', 'Times', 'Courier', 'Courier New', 'Helvetica',
                'Sans', 'verdana', 'utkal', 'aakar', 'Arial']
        font_sizes = ['10', '11', '12', '14', '16']

        box = wx.BoxSizer(wx.VERTICAL)
        menuBar = wx.MenuBar()

        menu1 = wx.Menu()
        menuBar.Append(menu1, '&File')
        menu2 = wx.Menu()
        menuBar.Append(menu2, '&Edit')
        menu3 = wx.Menu()
        menuBar.Append(menu3, '&Edit')
        menu4 = wx.Menu()
        menuBar.Append(menu4, '&Insert')
        menu5 = wx.Menu()
        menuBar.Append(menu5, 'F&ormat')
        menu6 = wx.Menu()
        menuBar.Append(menu6, '&Tools')
        menu7 = wx.Menu()
        menuBar.Append(menu7, '&Data')
        menu8 = wx.Menu()
        menuBar.Append(menu8, '&Help')

        self.SetMenuBar(menuBar)

        toolbar1 = wx.ToolBar(self, style= wx.TB_HORIZONTAL)

        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/new.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/open.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/save.png'))

        toolbar1.AddSeparator()

        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/cut.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/copy.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/paste.png'))
        toolbar1.AddTool(wx.ID_ANY, '',  wx.Bitmap('images/delete.png'))

        toolbar1.AddSeparator()

        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/undo.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/redo.png'))

        toolbar1.AddSeparator()

        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/asc.png'))
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/desc.png'))

        toolbar1.AddSeparator()
        toolbar1.AddTool(wx.ID_ANY, '', wx.Bitmap('images/chart.png'))

        toolbar1.AddSeparator()
        toolbar1.AddTool(wx.ID_ANY, '',  wx.Bitmap('images/exit.png'))

        toolbar1.Realize()

        toolbar2 = wx.ToolBar(self, wx.TB_HORIZONTAL | wx.TB_TEXT)

        self.position = wx.TextCtrl(toolbar2)

        font = wx.ComboBox(toolbar2, value='Times', choices=fonts, size=(100, -1),
                style=wx.CB_DROPDOWN)

        font_height = wx.ComboBox(toolbar2, value='10', choices=font_sizes,
                size=(50, -1), style=wx.CB_DROPDOWN)

        toolbar2.AddControl(self.position)
        toolbar2.AddControl(font)
        toolbar2.AddControl(font_height)

        toolbar2.AddSeparator()

        toolbar2.AddCheckTool(wx.ID_ANY, '', wx.Bitmap('images/text-bold.png'))
        toolbar2.AddCheckTool(wx.ID_ANY, '', wx.Bitmap('images/text-italic.png'))
        toolbar2.AddCheckTool(wx.ID_ANY, '', wx.Bitmap('images/text-underline.png'))

        toolbar2.AddSeparator()

        toolbar2.AddTool(wx.ID_ANY, '', wx.Bitmap('images/align-left.png'))
        toolbar2.AddTool(wx.ID_ANY, '', wx.Bitmap('images/align-center.png'))
        toolbar2.AddTool(wx.ID_ANY, '', wx.Bitmap('images/align-right.png'))

        box.Add(toolbar1, border=5)
        box.Add((5,5) , 0)
        box.Add(toolbar2)
        box.Add((5,10) , 0)

        toolbar2.Realize()
        self.SetSizer(box)

        notebook = wx.Notebook(self, style=wx.RIGHT)

        sheet1 = MySheet(notebook)
        sheet2 = MySheet(notebook)
        sheet3 = MySheet(notebook)
        sheet1.SetFocus()

        notebook.AddPage(sheet1, 'Sheet1')
        notebook.AddPage(sheet2, 'Sheet2')
        notebook.AddPage(sheet3, 'Sheet3')

        box.Add(notebook, 1, wx.EXPAND)

        self.CreateStatusBar()

        self.SetSize((550, 550))
        self.SetTitle("SpreadSheet")
        self.Centre()

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
