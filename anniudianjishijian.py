import tkinter as tk
import os
import sys
from selenium import webdriver
import tkinter.messagebox

# 设置窗口居中
def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y
# 设置登陆窗口属性
jiemian = tk.Tk()
jiemian.title("自动化测试数据采集器")
a, b = jiemian_info()
jiemian.geometry("450x300+%d+%d" % (a, b))
#设置按钮1事件
def button1():
    a = tkinter.messagebox.askokcancel('提示', '真的要执行吗？')
    print(a)
    if a == True:
        print("开始执行任务吧：", a)
        os.system("python 幸运28投注.py")

#设置按钮2事件
def button2():
     quit = tkinter.messagebox.askokcancel('提示', '真的要退出吗？')
     if quit == True:
         jiemian.destroy()
         print("确定要退出：",quit)
#设置按钮 Red, yellow, green, orange, brown, purple
tk.Button(jiemian,text="  启动  ",bg = "purple",fg = "orange",command = button1).place(x=190, y=100)
tk.Button(jiemian,text="  退出  ",bg = "purple",fg = "orange",command = button2).place(x=190, y=150)


jiemian.mainloop()