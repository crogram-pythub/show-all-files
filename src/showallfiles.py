#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020-present, Jackson Dou
# All rights reserved.
#

'''显示系统所有文件'''

__author__ = 'Jackson Dou'
__version__ = '0.0.2'

from os import system as cmd
from tkinter import Button, Tk, Menu, messagebox


def set_win_center(win, w, h):
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    win.geometry('%dx%d+%d+%d' % (w, h, (sw - w) / 2, (sh - h) / 2 - 50))
    win.update()


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('显示所有文件')
        set_win_center(self, 250, 150)
        # 窗口大小禁止拖拽
        self.resizable(False, False)
        self.createcommand('tk::mac::ShowPreferences', self.about)
        menubar = Menu(self)

        # 关于 系统内置菜单：name='apple'，针对 Mac
        m_app = Menu(menubar, name='apple')
        m_app.add_command(label='关于 显示所有文件', command=self.about)
        m_app.add_separator()
        # 将下拉菜单加到菜单栏
        menubar.add_cascade(label="显示所有文件", menu=m_app)
        self.config(menu=menubar)

        Button(self, text='显示所有文件', command=self.show).pack(expand='yes')
        Button(self, text='不显示隐藏文件', command=self.hide).pack(expand='yes')
        Button(self, text='关于', command=self.about).pack(expand='yes')
        Button(self, text='退出', command=self.close).pack(expand='yes')

    def show(self):
        # 显示所有文件
        # defaults write com.apple.finder AppleShowAllFiles -bool true
        # defaults write com.apple.finder AppleShowAllFiles YES
        status = cmd('defaults write com.apple.finder AppleShowAllFiles YES')
        if status == 0:
            self.reload_finder()
        else:
            messagebox.showerror('提示', '设置失败')

    def hide(self):
        # 隐藏
        # defaults write com.apple.finder AppleShowAllFiles -bool true
        # defaults write com.apple.finder AppleShowAllFiles NO
        status = cmd('defaults write com.apple.finder AppleShowAllFiles NO')
        if status == 0:
            self.reload_finder()
        else:
            messagebox.showerror('提示', '设置失败')

    def reload_finder(self):
        # 重启文件管理器
        res = cmd('killall Finder')
        if res == 0:
            messagebox.showinfo('提示', '设置成功\n文件管理器重启成功')
        else:
            messagebox.showerror('提示', '设置成功\n但是文件管理器重启失败\n请手动重启或者再试一次')

    def about(self):
        # 关于
        txt = '作者：%s\n版本：%s' % (__author__, __version__)
        messagebox.showinfo(title='关于', message=txt, parent=self)

    def close(self):
        self.quit()
        exit()


if __name__ == '__main__':
    app = App()
    app.mainloop()
