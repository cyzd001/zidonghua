from selenium import webdriver
from tkinter import *
from tkinter import ttk


def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 200
    y = (hs / 2) - 200
    print("%d,%d" % (ws, hs))
    return x, y
jiemian = Tk()
jiemian.title("登录小助手")
a, b = jiemian_info()
jiemian.geometry("400x230+%d+%d" % (a, b))

Label(jiemian, text="网站：").place(x=100, y=20)
Label(jiemian, text="用户：").place(x=100, y=60)
Label(jiemian, text="密码：").place(x=100, y=100)
Label(jiemian, text="提示：网站没有账号可以选好网站名点击登录直接打开").place(x=70, y=140)

'''设置文本框'''
# var_usr = StringVar()
usr = Entry(jiemian, font=('微软雅黑',10),width=12)
usr.place(x=150, y=60)
# var_pwd = StringVar()
pwd = Entry(jiemian, font=('微软雅黑',10),width=12)
pwd.place(x=150, y=100)
"""设置请求方式下拉框"""
numberChosen = ttk.Combobox(jiemian, width=10,font=('微软雅黑',10))
numberChosen['values'] = ("皮夹", "来聚财", "生意人", "jenkins","皮夹-电信", "来聚财-电信","生意人-电信","模拟银联支付")     # 设置下拉列表的值
numberChosen.place(x=150, y=20)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)
print(numberChosen.get())
url1 = "http://192.168.55.26:8080/aus-nk-bank/mainframe/login.jsp"
url2 = "http://192.168.55.16:8080/aus-nk-pjcore/mainframe/login.jsp"
url3 = "http://192.168.55.16:8080/aus-nk-business-m/mainframe/login.jsp"
url4 = "https://open.unionpay.com/ajweb/help/qrcodeFormPage/mainSweepReceiverApp"
url5 = "https://aus-nk-pjcore-dx.huiyinxun.com/aus-nk-pjcore/mainframe/login.jsp"
url6 = "https://aus-nk-bank-dx.huiyinxun.com/aus-nk-bank/mainframe/login.jsp"
url7 = "https://aus-nk-business-m-dx.huiyinxun.com/aus-nk-business-m/mainframe/login.jsp"
url8 = "http://192.168.55.10:8080/jenkins/login?from=%2Fjenkins%2F"
def denglu():
    wangzhan = numberChosen.get()
    username = usr.get()
    password = pwd.get()
    driver = webdriver.Chrome()
    driver.maximize_window()
    if wangzhan == "来聚财":
        driver.get(url1)
        driver.find_element_by_id("uname").send_keys(username)
        driver.find_element_by_id("pword").send_keys(password)
        driver.find_element_by_id("btn_login").click()
    elif wangzhan=="jenkins":
        driver.get(url8)
        driver.find_element_by_id("j_username").send_keys(username)
        driver.find_element_by_name("j_password").send_keys(password)
        driver.find_element_by_id("yui-gen1-button").click()
    elif wangzhan == "皮夹":
        driver.get(url2)
        driver.find_element_by_id("uname").send_keys(username)
        driver.find_element_by_id("pword").send_keys(password)
        driver.find_element_by_id("btn_login").click()
    elif wangzhan =="模拟银联支付":
        driver.get(url4)
        driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div[1]/div/div[2]/ul/li[1]/a').click()
    elif wangzhan == "皮夹-电信":
        driver.get(url5)
        driver.find_element_by_id("uname").send_keys(username)
        driver.find_element_by_id("pword").send_keys(password)
        driver.find_element_by_id("btn_login").click()
    elif wangzhan == "来聚财-电信":
        driver.get(url6)
        driver.find_element_by_id("uname").send_keys(username)
        driver.find_element_by_id("pword").send_keys(password)
        driver.find_element_by_id("btn_login").click()
    elif wangzhan == "生意人-电信":
        driver.get(url7)
        driver.find_element_by_id("uname").send_keys(username)
        driver.find_element_by_id("pword").send_keys(password)
        driver.find_element_by_id("btn_login").click()
    else:
        driver.get(url3)
        driver.find_element_by_id("uname").send_keys(username)
        driver.find_element_by_id("pword").send_keys(password)
        driver.find_element_by_id("btn_login").click()
def button1():
    denglu()

'''设置按钮'''
Button(jiemian,text="登录",width=8,command = button1).place(x=150, y=170)



jiemian.mainloop()