import random
import datetime
from time import sleep
import unittest
import HTMLTestRunner
import time
import os
import sys

"""猜数字游戏"""
a = random.randint(1,10)
c = 1
while c == 1:
    b = int(input("请输入一个数："))
    if a == b:
        print("恭喜你猜对了")
        c = 0
        print ("正确数字：",a)
        # break
    elif a < b:
        print("对不起猜错了，请再输入小一点数")
        c = 1
    else:
        print("对不起猜错了，请再输入大一点数")
        c = 1

"""随机数"""
def suiji(num):
    """生成num个随机数功能函数"""
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
''''''
def renwu():
    """设置任务"""
    for i in range(1,10):
        print(i)
def main(h,m):
    """设置定时任务函数"""
    print(h,m)
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m:
                break
            sleep(5)
        renwu()   #定时跑的任务
''''''
"""确定时间"""
starttime=datetime.datetime.now()
print("程序开始时间：",starttime)
endtime=datetime.datetime.now()
print("程序结束时间：",starttime)
second=(endtime-starttime).seconds
print("执行完程序用时",second,"s")

''''''
"""无限循环"""
def xuhuan(num): #num代表循环次数
    c = 1
    while c:
        os.system("python shifencaishuangmian.py")
        c = c + 1
        print("执行循环次数：", c - 1)
        if c > num:
            sys.exit(0)

''''''
"""组合数"""
def zuhe(m,n):
    c = 1
    b = 1
    d = 1
    num2 = 1
    num1 = 1
    num3 = 1
    while c <= m:
        if c <= m:
            num1 = num1 * c
            c = c +1
    while b <= n:
        if b <= n:
            num2 = num2 * b
            b = b + 1
    while d <= m-n:
        if d <= m-n:
            num3 = num3 * d
            d = d + 1
    print(num1,num2,num3)
    num = int(num1 /(num2*num3))
    print(num)
    return num
zuhe(11,9)
"""排列数"""
def pailei(m,n):
    c = 1
    b = 1
    num2 = 1
    num1 = 1
    while c <= m-n:
        if c <= m-n:
            num1 = num1*c
            c = c + 1
    while b <= m:
        if b <= m:
            num2 = num2*b
            b = b + 1
    print(num2,num1)
    num = int(num2/num1)
    print(num)
    return num
pailei(9,2)

"""读取和写入xls数据"""
'''往xls表格写入数据'''
import xlwt
import xlrd
wb = xlwt.Workbook()
ws = wb.add_sheet('excel.xls')
lb = [('username','password','money'),('sb001','qwaszx',3),('sb002','qwaszx1',1),('sb003','qwaszx12',2),('tt001','qwaszx12',1)]
c = 1
m = 0
for i in lb:
        num1 = i[0]
        num2 = i[1]
        num3 = i[2]
        if c > 0:
            ws.write(m, 0, num1)
            ws.write(m, 1, num2)
            ws.write(m, 2, num3)
            m = m + 1
wb.save('excel.xls')
'''读取excel表格数据'''
excel = xlrd.open_workbook('excel.xls')
nums = excel.sheet_by_index(0)
for n in range(1,5):
    for m in range(0,1):
        data = nums.cell(n, m).value
        da = nums.cell(n,m+1).value
        rmb = int(nums.cell(n,m+2).value)
        print (data,da,rmb)
        # print(data,end="")
        # print(da,end="")
        # print(rmb)

"""带框架跑自动化"""
class mytest(unittest.TestCase):
    def mukai001(self):
    def mukai002(self):

test = unittest.TestSuite()
test.addTest(mytest("mukuai001"))
test.addTest(mytest("mukuai002"))
now=time.strftime("%Y-%m-%d %H-%M-%S")
filename = "E:\\xuexi\\zdhbaogao\\"+now+".html"
fp = open(filename, "wb+")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="PC端自动化测试报告", description="用例执行情况:")
runner.run(test)
fp.close()

''''''


