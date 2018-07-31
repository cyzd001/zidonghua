from tkinter import messagebox
from tkinter import *
import xlwt
import requests
from tkinter import scrolledtext
import json
from tkinter import ttk
# 设置窗口居中
def jiemian_info():
    ws = jiemian.winfo_screenwidth()
    hs = jiemian.winfo_screenheight()
    x = (ws / 2) - 400
    y = (hs / 2) - 400
    print("%d,%d" % (ws, hs))
    return x, y
def readjson():
    wb = xlwt.Workbook('json-shuju.xls')
    ws = wb.add_sheet("caipiaopeilv")
    lb = url.get()
    data = datain.get("0.0", "end").strip()
    if data == "":
        ws.write(0, 0, "url")
        ws.write(1, 0, lb)
    elif data != "":
        data001=eval(datain.get("0.0", "end").strip())
        ws.write(0, 0, "url")
        ws.write(1, 0, lb)
        num = [a for a in data001]
        for b in range(len(num)):
            ws.write(0, b + 1, num[b])
        for c in range(len(num)):
            ws.write(1, c + 1, data001[num[c]])

    wb.save('json-shuju.xls')
def renwu001():
    """根据入参获取出参"""
    data = datain.get("0.0", "end").strip()
    if data == "":
        """入参为空"""
        return renwu004(data)
    elif data != "":
        """入参不为空"""
        return renwu003(data)
    # print(m.url)
    # print(data001)
def renwu002():
    """出参展示在文本框"""
    dataout.insert("0.0",renwu001())
def renwu003(data):
    """输出数据能够直接格式化"""
    data001=eval(data)#将str类型字符串字典化eval()
    if numberChosen.get() == "post":
        m = requests.post(url=url.get(), data=data001)
        json_str = json.dumps(eval(m.text), sort_keys=True, indent=2)
    elif numberChosen.get() == "get":
        m = requests.get(url=url.get(), data=data001)
        json_str = json.dumps(eval(m.text), sort_keys=True, indent=2)
    elif numberChosen.get() == "put":
        m = requests.put(url=url.get(), data=data001)
        json_str = json.dumps(eval(m.text), sort_keys=True, indent=2)
    elif numberChosen.get() == "delete":
        m = requests.put(url=url.get(), data=data001)
        json_str = json.dumps(eval(m.text), sort_keys=True, indent=2)
    else:
        json_str = "很明显有问题，没选方式"
    return json_str
def renwu004(data):
    """输出数据不能直接格式化"""
    m = requests.post(url=url.get(), data=data)
    if numberChosen.get() == "post":
        try:
            json_str = json.dumps(eval(m.text), sort_keys=True, indent=2)
        except:
            json_str = m.text
    elif numberChosen.get() == "get":
        try:
            json_str = json.dumps(eval(m.text), sort_keys=True, indent=2)
        except:
            json_str = m.text
    elif numberChosen.get() == "put":
        try:
            json_str = json.dumps(eval(m.text), sort_keys=True, indent=2)
        except:
            json_str = m.text
    elif numberChosen.get() == "delete":
        try:
            json_str = json.dumps(eval(m.text), sort_keys=True, indent=2)
        except:
            json_str = m.text
    else:
        json_str = "很明显有问题，没选方式"
    return json_str
# 设置窗口属性
jiemian = Tk()
jiemian.title("接口测试工具")
a, b = jiemian_info()
jiemian.geometry("1200x800+%d+%d" % (a, b))
'''设置标签'''
Label(jiemian, text="URL：").place(x=30, y=20)
Label(jiemian, text="方式：").place(x=880, y=20)
# numberChosen = ttk.Combobox(jiemian,width=10,textvariable=name).place(x=890, y=20)
# numberChosen.append("post")
Label(jiemian, text="入参").place(x=100, y=70)
Label(jiemian, text="出参").place(x=750, y=70)

'''设置文本框'''
var_url = StringVar()
url = Entry(jiemian, textvariable=var_url, font=('微软雅黑',10),width=100)
url.place(x=70, y=20)
# var_fangshi = StringVar()
# fangshi = Entry(jiemian, textvariable=var_fangshi,width=10)
# fangshi.place(x=890, y=20)
"""设置参数输入框"""
datain = scrolledtext.ScrolledText(jiemian, font=('微软雅黑',10),width=60, height=30, wrap=WORD)
datain.place(x=20,y=100)
dataout = scrolledtext.ScrolledText(jiemian, font=('微软雅黑',10),width=60, height=30, wrap=WORD)
dataout.place(x=680,y=100)
"""设置请求方式下拉框"""
number = StringVar()
numberChosen = ttk.Combobox(jiemian, width=12,font=('微软雅黑',10) ,textvariable=number)
numberChosen['values'] = ("post", "get", "put","delete")     # 设置下拉列表的值
numberChosen.place(x=930, y=20)      # 设置其在界面中出现的位置  column代表列   row 代表行
numberChosen.current(0)
def button1():
    # a = messagebox.askokcancel('提示', '真的要执行吗？')
    # print(a)
    # if a == True:
    #     print("开始执行任务吧：", a)
    #     # readjson()
    dataout.delete("0.0", "end")
    renwu001()
    renwu002()
    readjson()
def button2():
    dataout.delete("0.0", "end")
def button3():
    datain.delete("0.0", "end")
def button4():
    try:
        data002 = eval(dataout.get("0.0", "end").strip())
        json_str = json.dumps(data002, sort_keys=True, indent=2)
        dataout.delete("0.0", "end")
        dataout.insert("0.0", json_str)
    except:
        data002 = dataout.get("0.0", "end").strip()
        dataout.delete("0.0", "end")
        dataout.insert("0.0", "数据格式不标准，无法格式化")


'''设置按钮'''
Button(jiemian,text="提交",width=8,command = button1).place(x=549, y=190)
Button(jiemian,text="清空出参",width=9,command = button2).place(x=548, y=280)
Button(jiemian,text="清空入参",width=9,command = button3).place(x=548, y=370)
Button(jiemian,text="格式化",width=9,command = button4).place(x=760, y=690)


jiemian.mainloop()