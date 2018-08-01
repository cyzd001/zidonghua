import random
import datetime
from time import sleep
import unittest
import HTMLTestRunner
import time
import os
import sys

'''三个数相加和值，几种组合'''
def hezhi(num):
    import random
    n = 1
    result = {}
    while n <= 1000:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        if a + b + c == num:
            result[n] = (a, b, c)
            n = n + 1
    print(result)
    print(n)
    func = lambda z: dict([(x, y) for y, x in z.items()])
    print((func(func(result))))
    num = [a for a in func(func(result))]
    print(len(num))
hezhi(21)
''''''
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


