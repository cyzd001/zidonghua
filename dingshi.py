import datetime
import tkinter as tk
from tkinter import messagebox
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
jiemian.title("设置每天运行任务时间点")
a, b = jiemian_info()
jiemian.geometry("500x500+%d+%d" % (a, b))
'''设置标签'''
tk.Label(jiemian, text="时：").place(x=120, y=150)
tk.Label(jiemian, text="分：").place(x=120, y=190)
'''设置文本框'''
var_usr_name = tk.StringVar()
hr = tk.Entry(jiemian, textvariable=var_usr_name)
hr.place(x=160, y=150)
var_usr_pwd = tk.StringVar()
min = tk.Entry(jiemian, textvariable=var_usr_pwd)
min.place(x=160, y=190)
'''获取前台传入值'''
def mokuai():
    h = int(hr.get())
    m = int(min.get())
    main(h,m)
'''设置任务'''

def renwu():
    a = datetime.datetime.now()
    print("执行任务开始时间：",a)
    try:
        driver = webdriver.Firefox()
        driver.get("http://lb-test.com/#/passport/login")
        # 输入账号和密码
        driver.find_element_by_xpath('//*[@placeholder="请输入账号"]').send_keys("sb001")
        driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys("qwaszx")
        driver.find_element_by_xpath('//*[@placeholder="请输入验证码"]').send_keys("8888")
        # 点击登录
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        sleep(1)
        '''点击购彩大厅'''
        driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[2]/a').click()
        sleep(1)
        '''快3'''
        driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/ul/li[2]/div/div/ul[1]/li[1]/a').click()
        sleep(1)
        '''默认点数玩法'''
        driver.find_element_by_xpath('//*[@id="17_13"]/span[3]/div/input').send_keys(1)
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
    except:
        print("执行任务失败")
    b=datetime.datetime.now()
    print("执行任务结束时间：",b)
'''设置执行任务时间点'''

def main(h,m):
    print(h,m)
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m:
                break
            sleep(5)
        renwu()
'''设置按钮功能'''
def button1():
    a = tk.messagebox.askokcancel('提示', '真的要执行吗？')
    if a == True:
        print("开始执行任务吧：", a)
        mokuai()
        jiemian.destroy()
def button2():
    quit = tk.messagebox.askokcancel('提示', '真的要退出吗？')
    if quit == True:
        jiemian.destroy()
        print("确定要退出：", quit)
'''设置按钮'''
tk.Button(jiemian,text="  启 动  ",bg = "purple",fg = "orange",command = button1).place(x=160, y=230)
tk.Button(jiemian,text="  退 出  ",bg = "purple",fg = "orange",command = button2).place(x=230, y=230)

jiemian.mainloop()
