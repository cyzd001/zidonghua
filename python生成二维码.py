from tkinter import *
import qrcode
from tkinter.filedialog import askopenfilename

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
jiemian.geometry("600x650+%d+%d" % (a, b))
Label(jiemian, text="输入：").grid(row=0, column=0, stick=E,pady=10)
'''设置文本框'''
url = Entry(jiemian,font=('微软雅黑',10),width=40)  #,width=40
url.grid(row=0, column=1, stick=E,pady=10,padx=5)
# image_frame = Frame(jiemian)
label_img = Label(jiemian, text="此处生成二维码")  # ,image=button()  ,image=path ,labelanchor=NW
label_img.grid(row=2, column=1, stick=E+W,pady=10) #, ipady=20, ipadx=20  row=3, column=1
# def choosepic():
#     path_=askopenfilename()
#     path.set(path_)
#     img_gif=PhotoImage(file='xxx.gif')
#     l1.config(image=img_gif)
#
# path=StringVar()
# Button(jiemian,text='选择图片',command=choosepic).pack()
# e1=Entry(jiemian,state='readonly',text=path)
# e1.pack()
# l1=Label(jiemian)
# l1.pack()
# path=PhotoImage(file='tupian.gif')
# label_img = Label(jiemian, image=path)
# label_img.place(x=120,y=110)
# image_frame.pack()
img,path,label=None,None,None
def button():
    global img, path, label
    img = qrcode.make(url.get())
    img.save("tupian.gif")
    path=PhotoImage(file='tupian.gif')
    label = Label(jiemian, image=path,width=340,height=340)  #,width=340,height=340
    label.grid(row=3, column=1, stick=E+W, pady=10, ipady=10, ipadx=10)
'''设置按钮'''
Button(jiemian,text="生成二维码",width=28,command=button).grid(row=1, column=1, stick=E+W,pady=10) #
jiemian.mainloop()

