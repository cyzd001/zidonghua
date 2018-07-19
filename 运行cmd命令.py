import os
import sys
import random
# os.system("cmd")
# # os.system("")
# os.system(r"cd E:\Users\admin\AppData\Local\Programs\Python\Python36\Scripts")


mystr=os.popen("tasklist")  #popen与system可以执行指令,popen可以接受返回对象
mystr=mystr.read() #读取输出
print("hello",mystr)
if mystr.find("QQ.exe") !=-1:
    print("发现QQ")
else:
    print("QQ已死有事请烧纸")

os.popen("cd \AppData\Local\Programs\Python\Python36\Scripts")
my = os.popen("pyinstaller -F -w dycshuchubaogao.py")
print(my.read())

result = os.popen("ipconfig")
print(result.read())

m = 2712410.392 - 2703719.527- 2601420.75-30051.5

print(m)
def suiji(num):
    result =[]
    total = 1
    while total <= num:
        temp = random.randint(0, 9)
        if temp not in result:
            result.append(temp)
            total = total + 1
    print(result)
    return result
for i in suiji(5):
    print(i)

resultList=random.sample(range(1,10),5)
print(resultList)