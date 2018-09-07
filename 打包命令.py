import os

"""将python程序打包"""
os.popen("D:")
os.popen("cd \gongju\Python\python\Scripts")
my = os.popen("pyinstaller -F -w  D:\zidonghua\wangzhan.py")
print(my.read())



# """执行cmd命令"""
# my = os.popen("pip install --upgrade pyinstaller")
# print(my.read())