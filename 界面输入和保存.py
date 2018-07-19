import tkinter as tk
from tkinter import messagebox
import xlwt
import xlrd
import os
from time import sleep
from selenium import webdriver
# 设置窗口居中
def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 400
    y = (hs / 2) - 400
    print("%d,%d" % (ws, hs))
    return x, y

# 设置窗口属性
jiemian = tk.Tk()
jiemian.title("自动化测试数据采集器")
a, b = jiemian_info()
jiemian.geometry("650x500+%d+%d" % (a, b))
'''设置背景图片'''


'''设置标签'''
tk.Label(jiemian, text="账号：").place(x=120, y=150)
tk.Label(jiemian, text="密码：").place(x=120, y=190)
tk.Label(jiemian, text="验证码：").place(x=120, y=230)
tk.Label(jiemian, text="金钱：").place(x=120, y=270)
'''设置文本框'''
var_usr_name = tk.StringVar()
usr_name = tk.Entry(jiemian, textvariable=var_usr_name)
usr_name.place(x=190, y=150)
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(jiemian, textvariable=var_usr_pwd)
entry_usr_pwd.place(x=190, y=190)
var_usr = tk.StringVar()
entry_usr = tk.Entry(jiemian, textvariable=var_usr)
entry_usr.place(x=190, y=230)
rmb = tk.StringVar()
entry_rmb = tk.Entry(jiemian, textvariable=rmb)
entry_rmb.place(x=190, y=270)
'''江苏'''
def touzhu():
    username = usr_name.get()
    password = entry_usr_pwd.get()
    yanzhengma = entry_usr.get()
    money = entry_rmb.get()
    print(username,password,yanzhengma,money)
    driver = webdriver.Firefox()
    driver.get("http://lb-test.com/#/passport/login")
    # 输入账号和密码
    driver.find_element_by_xpath('//*[@placeholder="请输入账号"]').send_keys(username)
    driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys(password)
    driver.find_element_by_xpath('//*[@placeholder="请输入验证码"]').send_keys(yanzhengma)
    # 点击登录
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    sleep(1)
    '''点击购彩大厅'''
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div/div/div/dl/dd[2]').click()
    '''快3'''
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div/div/div/dl/dd[2]/div/div/ul[1]/li[1]/a').click()
    # '''江苏快3'''
    # driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[5]/div[2]/ul[5]/li[1]/a').click()
    sleep(1)
    '''默认点数玩法'''
    driver.find_element_by_xpath('//*[@id="17_13"]/span[3]/div/input').send_keys(money)
    # 点击提交投注
    driver.find_element_by_xpath(
        '//*[@id="[object Object]"]/div/div[2]/div[1]/div[2]/div[1]/div/div[2]/div[3]/a[1]').click()
    sleep(2)
    # 确认投注弹框出现
    driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
    sleep(1)
    # 投注成功弹框出现
    driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
    driver.quit()

'''设置按钮功能'''
def button1():
    a = tk.messagebox.askokcancel('提示', '真的要执行吗？')
    print(a)
    if a == True:
        print("开始执行任务吧：", a)
        touzhu()
    # os.system("python 幸运28投注.py")
'''设置按钮2事件'''
def button2():
     quit = tk.messagebox.askokcancel('提示', '真的要退出吗？')
     if quit == True:
         jiemian.destroy()
         print("确定要退出：",quit)
'''设置按钮'''
tk.Button(jiemian,text="  启动  ",bg = "purple",fg = "orange",command = button1).place(x=190, y=320)
tk.Button(jiemian,text="  退出  ",bg = "purple",fg = "orange",command = button2).place(x=260, y=320)

jiemian.mainloop()

# try:
#     if driver.find_element_by_link_text("你好，欢迎来到49彩票网!"):
#         driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[3]/div/div/div/div/dl/dd[2]').click()
#         sleep(1)
#         '''江苏快3'''
#         driver.find_element_by_xpath(
#             '//*[@id="app"]/div[2]/div[3]/div/div/div/div/dl/dd[2]/div/div/ul[1]/li[1]/a').click()
#         '''默认点数玩法'''
#         driver.find_element_by_xpath('//*[@id="17_13"]/span[3]/div/input').send_keys(money)
#         # 点击确认投注
#         driver.find_element_by_xpath(
#             '//*[@id="content"]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[7]/a[1]').click()
#         sleep(2)
#         # 确认投注弹框出现
#         driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
#         sleep(1)
#         # 投注成功弹框出现
#         driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
#         driver.quit()
# except:
#     print("未成功打开49彩票网站")


