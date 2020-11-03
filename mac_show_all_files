#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020, doudoudzj
# All rights reserved.
#
# InPanel is distributed under the terms of the (new) BSD License.
# The full license can be found in 'LICENSE'.
'''显示系统所有文件 for Mac'''

__author__ = 'doudoudzj'
__version__ = '0.0.1'
__license__ = 'BSD'

from os import system as cmd
from tkinter import Button, Tk, messagebox


def set_win_center(win, w, h):
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    win.geometry('%dx%d+%d+%d' % (w, h, (sw - w) / 2, (sh - h) / 2 - 50))
    win.update()


class App:
    def __init__(self):
        root = Tk()
        root.title('显示系统所有文件')
        set_win_center(root, 250, 150)
        # 窗口大小禁止拖拽
        root.resizable(False, False)

        Button(root, text='显示所有文件', command=self.show).pack(expand='yes')
        Button(root, text='不显示隐藏文件', command=self.hide).pack(expand='yes')
        Button(root, text='关于', command=self.about).pack(expand='yes')
        Button(root, text='退出', command=self.close).pack(expand='yes')

        self.root = root
        root.mainloop()

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
        messagebox.showinfo('关于', txt)

    def close(self):
        self.root.quit()
        exit()


if __name__ == '__main__':
    App()
