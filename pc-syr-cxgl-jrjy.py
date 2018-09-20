from selenium import webdriver
from time import sleep
import time
import HTMLTestRunner
import unittest
import cx_Oracle as oracle
import os
import operator
import datetime

"""生意人-查询管理-今日交易明细"""
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
driver = webdriver.Chrome()
db = oracle.connect('pj_trd', 'pj_trd', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
def jiaoyijieguo(num):

    if num == '00':
        num = "成功"
    elif num == "01":
        num ="失败"
    return num
def denglu():
    result = []
    driver.get("http://192.168.55.16:8080/aus-nk-business-m/mainframe/login.jsp")
    driver.find_element_by_id('uname').send_keys(15383840013)
    driver.find_element_by_id('pword').send_keys(123456)
    driver.find_element_by_id('btn_login').click()
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="menudiv"]/div[3]/div[1]/div').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="menudiv"]/div[3]/div[2]/div/div').click()
    driver.switch_to.frame("tabpage1_pf1")
    driver.find_element_by_id('hfv10_qdddh').send_keys('a861add9-32ae-4274-8335-a5390abc2ac1')
    driver.find_element_by_xpath('//*[@id="btn_query"]/span[2]').click()
    sleep(1)
    num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[2]/div').text
    result.append(num1)
    for i in range(1,12):
        num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]'%i).text.replace('￥','')
        result.append(num2)
    result[1] = 'C'
    print(result)
    """订单表"""
    cur.execute("select * from trd_dd where id='63bdf741-d0dc-4d6b-ac93-70f41bbe65ce'")
    row1 = cur.fetchone()
    """银行（来聚财）订单表"""
    cur.execute("select * from TRD_YHDD where TRD_DD_ID='63bdf741-d0dc-4d6b-ac93-70f41bbe65ce'")
    row2 = cur.fetchone()
    """扫码交易结果表"""
    cur.execute("select * from trd_smjyjg where TRD_DD_ID='63bdf741-d0dc-4d6b-ac93-70f41bbe65ce'")
    row3 = cur.fetchone()
    """券使用明细表"""
    cur.execute("select FFJE from TRD_JSYMX where TRD_DD_ID='63bdf741-d0dc-4d6b-ac93-70f41bbe65ce'")
    row4 = cur.fetchone()
    print(row3)
    print(row2)
    print(row1)
    row = []
    row.append(row1[8])
    row.append(row1[1])
    row.append('%0.2f'%row1[2])
    row.append('%0.2f'%row1[3])
    row.append('%0.2f'%row1[4])
    row.append(jiaoyijieguo(row3[4]))
    if row4[0] == row1[4]:
        row.append('券')
    row.append(row1[28])
    jytime = str(row3[1])
    row.append(jytime)
    row.append(row2[0])
    row.append(row1[0])
    row.append('')
    if operator.eq(result, row) == True:
        print("今日交易明细查询展示数据正确")
    else:
        print("今日交易明细查询展示数据错误")
class test02(unittest.TestCase):
    def jinrijiaoyi(self):
        denglu()
test = unittest.TestSuite()
test.addTest(test02("jinrijiaoyi"))


now = time.strftime("%Y-%m-%d %H-%M-%S")
filename = "D:\\zidonghua\\zdhbg\\"+now+".html"
fp = open(filename, "wb+")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="生意人-查询管理-今日交易明细", description="用例执行情况:")
runner.run(test)
fp.close()

