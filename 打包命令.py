import os

"""将python程序打包"""
# os.popen("D:")
# os.popen("cd \gongju\Python\python\Scripts")
# my = os.popen("pyinstaller -F -w  D:\zidonghua\denglu.py")
# print(my.read())

"""运行django"""
# os.system("D:")
# os.system("cd D:\zidonghua\mysite")
# os.system("python D:/zidonghua/mysite/manage.py runserver")



# """执行cmd命令"""
# my = os.popen("pip install --upgrade pyinstaller")
# print(my.read())
import hashlib
def jiami(pwd):
    hl = hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()
    return hl
str=jiami('123456').upper()
print(str)
