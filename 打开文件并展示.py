from tkinter import *
import qrcode
from tkinter.filedialog import askopenfilename,asksaveasfilename
from tkinter import scrolledtext
import hashlib
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
jiemian.geometry("600x750+%d+%d" % (a, b))
text = scrolledtext.ScrolledText(jiemian,)
text.grid(row=1, column=1, columnspan=3,stick=E+W,pady=10,padx=5)
text1 = scrolledtext.ScrolledText(jiemian,)
text1.grid(row=2, column=1, columnspan=3,stick=E+W,pady=10,padx=5)
def choosepic():
    path_=askopenfilename()
    # path.set(path_)
    with open(path_) as file1:
        file2 = file1.read().split()    #.split()
    text.insert("0.0", file2)
def baocun():
    path = asksaveasfilename()
    path.save()
def jiami():
    neirong = text.get("0.0", "end")
    print(neirong)
    hl = hashlib.md5(neirong.encode(encoding='UTF-8')).hexdigest()  #upper() 字母转换为大写
    text1.delete("0.0", "end")
    text1.insert("0.0", hl)

Button(jiemian,text="打开",command=choosepic).grid(row=0, column=1,pady=10,padx=5,ipadx=20)  #stick=E+W
Button(jiemian,text="保存",command=baocun).grid(row=0, column=2,pady=10,padx=5,ipadx=20)  #stick=E+W
Button(jiemian,text="MD5加密",command=jiami).grid(row=0, column=3,pady=10,padx=5,ipadx=20)  #stick=E+W
jiemian.mainloop()