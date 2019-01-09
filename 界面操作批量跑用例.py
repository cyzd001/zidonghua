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
import os
import time
import HTMLTestRunner




class Yongli(unittest.TestCase):

    def test_001(self):
        print("执行用例test_001成功")
    def test_002(self):
        print("执行用例test_002成功")
    def test_003(self):
        print("执行用例test_003成功")
    def test_004(self):
        print("执行用例test_004成功")
    def test_005(self):
        print("执行用例test_005成功")
    def test_006(self):
        print("执行用例test_006成功")
    def test_007(self):
        print("执行用例test_007成功")
    def test_008(self):
        print("执行用例test_008成功")
    def test_009(self):
        print("执行用例test_009成功")
    def test_010(self):
        print("执行用例test_010成功")
    def test_011(self):
        print("执行用例test_011成功")
    def test_012(self):
        print("执行用例test_012成功")
    def test_013(self):
        print("执行用例test_013成功")
def quanxuan():
    num = listb.size()  #返回当前listbox总个数
    listb.selection_set(0,num)   #全部选中
def quxiao():
    num = listb.size()  # 返回当前listbox总个数
    listb.selection_clear(0, num)  # 取消所有选中

def button1():
    suite = unittest.TestSuite()
    num = listb.size()
    result = []
    for i in range(0, num):
        if listb.selection_includes(i) == True:
            result.append(listb.get(i))
    for j in result:
        suite.addTest(Yongli(j))
    # unittest.TextTestRunner().run(suite) #此行要放在循环外面
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = "E:\\python-jiaoben\\baogao\\" + now + ".html"
    fp = open(filename, "wb+")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="用例集合", description="用例执行情况:")
    runner.run(suite)
    fp.close()
    listba.insert(END, now)
def button2():
    num001 = listba.size()
    for i in range(0, num001):
        if listba.selection_includes(i) == True:
            driver = webdriver.Chrome()
            driver.get('E:\\python-jiaoben\\baogao\\%s.html'%listba.get(i))
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
label = Label(jiemian, text='选择自动化用例')
label.grid(row=1, column=3, stick=W+E,pady=5)
labela = Label(jiemian, text='测试报告')
labela.grid(row=1, column=5, stick=W+E,pady=5)

listb=Listbox(jiemian, width=60,height=41,selectmode=MULTIPLE)
listb.grid(row=2, column=3,sticky=E+W, padx=10,pady=5,ipady=100, ipadx=80)
yscrollbar = tk.Scrollbar(listb, command=listb.yview)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listb.config(yscrollcommand=yscrollbar.set)
listba=Listbox(jiemian, width=60,height=41)   #多选标志：selectmode=MULTIPLE
listba.grid(row=2, column=5,sticky=E+W, padx=180,pady=5,ipady=100, ipadx=80)
yscrollbar = tk.Scrollbar(listba, command=listb.yview)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listba.config(yscrollcommand=yscrollbar.set)
li = ['test_001', 'test_002', 'test_003', 'test_004', 'test_005', 'test_006', 'test_007', 'test_008', 'test_009',\
       'test_010', 'test_011', 'test_012', 'test_013']

def getfilename(path):
    """根据路径获取特定格式的文件"""
    file = os.listdir(path)
    # print(file)
    for i in file:
        # print(os.path.splitext(i))
        if os.path.splitext(i)[1] == ".py":
            print(i.replace('.py', ''))
            li.append(i.replace('.py', ''))
baogao=[]
def htmlbg(path):
    file = os.listdir(path)
    # print(file)
    for i in file:
        # print(os.path.splitext(i))
        if os.path.splitext(i)[1] == ".html":
            print(i.replace('.html', ''))
            baogao.append(i.replace('.html', ''))
getfilename('E:\python-jiaoben')
htmlbg('E:\\python-jiaoben\\baogao')
for item in li:
    listb.insert(END, item)
for itema in baogao:
    listba.insert(END, itema)
Button(jiemian, text="执行", width=8,command=button1).place(x=230,y=140)  #, command=self.button1 .grid(row=1,column=0,stick=W+E, padx=30)
Button(jiemian, text="全选", width=8,command=quanxuan).place(x=230,y=80)
Button(jiemian, text="取消",width=8,command=quxiao).place(x=300,y=80)
Button(jiemian, text="打开报告",width=8,command=button2).place(x=300,y=140)

jiemian.mainloop()

