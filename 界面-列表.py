from tkinter import messagebox
from tkinter import *
import xlwt
import xlrd
from tkinter import scrolledtext
import time
from xlutils.copy import copy
import tkinter as tk
from selenium import webdriver
def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 400
    y = (hs / 2) - 300
    print("%d,%d" % (ws, hs))
    return x, y
jiemian = Tk()
jiemian.title("工具小助手")
a, b = jiemian_info()
jiemian.geometry("500x300+%d+%d" % (a, b))
li  = ['aus-bank','aus-nk-pjcore','aus-unionpay','aus-nk-bank','aus-merchant','aus-hcapp',\
       'aus-web','aus-wechat','aus-wechat-mp','boc-clear','aus-qrcode']
listb  = Listbox(jiemian,selectmode = MULTIPLE)
listb.place(x=150,y=60,relwidth=0.3,relheight=0.5)
yscrollbar = tk.Scrollbar(listb, command=listb.yview)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listb.config(yscrollcommand=yscrollbar.set)
for item in li:
    listb.insert(0, item)
# yscroll["command"] = listb.yview
def goujian(result):
    driver = webdriver.Chrome()
    driver.get("http://192.168.55.10:8080/jenkins/login?from=%2Fjenkins%2F")
    driver.find_element_by_id("j_username").send_keys('caiyong')
    driver.find_element_by_name("j_password").send_keys('Qwaszx12')
    driver.find_element_by_id("yui-gen1-button").click()
    time.sleep(1)
    for i in result:
        driver.find_element_by_xpath('//*[@title="Schedule a Build for %s"]'%i).click()

def button1():
    num = listb.size()
    result = []
    for i in range(0, num):
        if listb.selection_includes(i) == True:
            result.append(listb.get(i))
    print(result)
    goujian(result)

'''设置按钮'''
Button(jiemian, text="构建", width=8, command=button1).place(x=190, y=240)



jiemian.mainloop()