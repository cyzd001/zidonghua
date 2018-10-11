from tkinter import *
import tkinter as tk
import json
import requests
from tkinter import messagebox

def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y
jiemian = Tk()
jiemian.title("￥￥")
a, b = jiemian_info()
jiemian.geometry("300x150+%d+%d" % (a, b))
urll = 'http://192.168.18.38:8073/login'
def button1():
    datain = {'SJH':url.get(),'PWD':pwd.get()}
    num = int(url.get())
    print(type(num))
    print(datain)
    m = requests.get(url=urll,data=datain)
    print(m.text)
    print(type(eval(m.text)))
    msg = eval(m.text)
    if msg['msg_code'] == '200':
        a = messagebox.showinfo('提示', '成功登录')
        print(a)
    elif msg['msg_code'] == '204':
        messagebox.showinfo('提示', '密码和用户名错误')
    # a = messagebox.askokcancel('提示', '真的要退出吗？')     #弹框
    # print(a)
    # if a == True:
    #     jiemian.quit()  # 关闭窗口
    #     jiemian.destroy()  # 将所有的窗口小部件进行销毁，应该有内存回收的意思

    print(m.headers)
    print(m.status_code)
Label(jiemian, text="用户：").place(x=55, y=20)
Label(jiemian, text="账号：").place(x=55, y=60)
'''设置文本框'''
url = Entry(jiemian,font=('微软雅黑',10),width=15)
url.place(x=95, y=20)
var_pwd = StringVar()
pwd = Entry(jiemian, font=('微软雅黑',10),width=15)
pwd.place(x=95, y=60)
'''设置按钮'''
Button(jiemian,text="登录",width=10,command=button1).place(x=105, y=95)

jiemian.mainloop()