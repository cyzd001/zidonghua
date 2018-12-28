from tkinter import *
from selenium import webdriver
import tkinter as tk
from tkinter import scrolledtext,messagebox
from time import sleep
from tkinter import ttk
import xlrd
import requests
import json
import qrcode
import unittest

class Yongli(unittest.TestCase):
    def test_001(self):
        print("执行用例test_001成功")
    def test_002(self):
        print("执行用例test_002成功")
    def test_003(self):
        print("执行用例test_003成功")
    def test_004(self):
        print("执行用例test_004成功")
def quanxuan():
    num = listb.size()  #返回当前listbox总个数
    listb.selection_set(0,num)   #全部选中
def quxiao():
    num = listb.size()  # 返回当前listbox总个数
    listb.selection_clear(0, num)  # 全部取消选中

def button1():
    suite = unittest.TestSuite()
    num = listb.size()
    result = []
    for i in range(0, num):
        if listb.selection_includes(i) == True:
            result.append(listb.get(i))
    for j in result:
        suite.addTest(Yongli(j))
    unittest.TextTestRunner().run(suite) #此行要放在循环外面
def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y
jiemian = Tk()
jiemian.title("自动化用例集合")
a, b = jiemian_info()
jiemian.geometry("600x400+%d+%d" % (a, b))
label = Label(jiemian, text='选择用例')
label.grid(row=1, column=3, stick=W+E,pady=5)
listb=Listbox(jiemian, width=60,height=41,selectmode=MULTIPLE)
listb.grid(row=2, column=3,sticky=E+W, pady=5,ipady=100, ipadx=80)
yscrollbar = tk.Scrollbar(listb, command=listb.yview)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listb.config(yscrollcommand=yscrollbar.set)
li = ['test_001', 'test_002', 'test_003', 'test_004']
for item in li:
    listb.insert(END, item)
Button(jiemian, text="执行", width=8,command=button1).grid(row=2,column=1,stick=W+E, padx=30)  #, command=self.button1
Button(jiemian, text="全选", width=8,command=quanxuan).place(x=360,y=80)
Button(jiemian, text="取消",width=8,command=quxiao).place(x=430,y=80)

jiemian.mainloop()