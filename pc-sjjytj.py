from selenium import webdriver
from time import sleep
import time
import HTMLTestRunner
import unittest
import cx_Oracle as oracle
import os
import operator

"""皮夹平台-大数据-商家交易统计"""
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
driver = webdriver.Chrome()
db = oracle.connect('pj_rep', 'pj_rep', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
def denglu():
    driver.get("http://192.168.55.16:8080/aus-nk-pjcore/mainframe/login.jsp")
    driver.maximize_window()
    driver.find_element_by_id("uname").send_keys("admin")
    driver.find_element_by_id("pword").send_keys(123456)
    driver.find_element_by_id("btn_login").click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="hctb11_8"]').click()
    driver.find_element_by_xpath('//*[@id="menudiv"]/div[1]/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="menudiv"]/div[1]/div[4]/div/div').click()
    str3 = driver.find_element_by_xpath('//*[@id="tabpage1_pf1"]').is_displayed()
    print(str3)
    driver.switch_to.frame("tabpage1_pf1")
class sjjytj(unittest.TestCase):
    def richaxun(self):
        denglu()
        result = []
        driver.find_element_by_id('hfv10_dayDate').send_keys("2018-08-21")
        driver.find_element_by_id('hfv10_mobile').send_keys('18551698733')
        driver.find_element_by_xpath('//*[@id="btn_query"]/span[2]').click()
        sleep(1)
        for i in range(2, 4):
            num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[%r]/div' % i).text
            result.append(num1)
        for j in range(1, 13):
            if j == 1:
                num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % j)
                result.append(num2)
            else:
                num2 = float(driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % j).text.replace("￥", ""))
                result.append('%.2f' % num2)
        for k in range(13, 19):
            num3 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % k).text
            result.append(num3)
        result[2] = '1'
        """交易主体日汇总表"""
        cur.execute(
            "select * from BUS_JYZTRHZ where SYR_SJRWJBXX_YYZZMC='smart超市' and TJRQ=to_date('2018-08-21','YYYY-MM-DD')")
        row1 = cur.fetchone()
        print(row1)
        """商家收银主体情况表"""
        cur.execute("select * from BUS_SJSYZTQK where SYR_SYZTJC_ID='06c6dbd2-446b-48b9-b16e-42f4e5201d6a'")
        row2 = cur.fetchone()
        """拓展机构参数表"""
        k = row1[1]
        cur.execute("select * from BAS_TZJGCS where ID=%r" % k)
        row3 = cur.fetchone()
        print(row3)
        row = []
        row.append(row2[17])
        row.append(row1[4])
        row.append(row1[6])
        row.append('%.2f' % row1[13])
        row.append('%.2f' % row1[14])
        row.append('%.2f' % row1[34])
        row.append('%.2f' % row1[35])
        row.append('%.2f' % row1[30])
        row.append('%.2f' % row1[31])
        row.append('%.2f' % row1[26])
        row.append('%.2f' % row1[27])
        row.append('%.2f' % row1[39])
        row.append('%.2f' % row1[40])
        row.append('%.2f' % row1[25])
        row.append(row1[5])
        row.append(row2[5])
        row.append(row2[6])
        row.append(row2[8])
        row.append(row3[4])
        row.append(row3[10])
        print(row)
        print(result)
        if operator.eq(result, row) == True:
            print("按日查询展示数据正确")
        else:
            print("按日查询展示数据错误")
    def zhouchaxun(self):
        denglu()
        driver.find_element_by_xpath('//*[@id="hfv10_tjfs"]').click()
        driver.find_element_by_xpath('//*[@id="hfv10_tjfs"]/option[2]').click()
        driver.find_element_by_id('hfv10_weekDate').send_keys("2018-08-21")
        driver.find_element_by_id('hfv10_mobile').send_keys('18551698733')
        driver.find_element_by_xpath('//*[@id="btn_query"]/span[2]').click()
        sleep(1)
        result = []
        for i in range(2, 4):
            num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[%r]/div' % i).text
            result.append(num1)
        for j in range(1, 13):
            if j == 1:
                num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % j)
                result.append(num2)
            else:
                num2 = float(driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % j).text.replace("￥", ""))
                result.append('%.2f' % num2)
        for k in range(13, 19):
            num3 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % k).text
            result.append(num3)
        result[2] = '1'
        print(result)
        """交易主体周汇总表"""
        cur.execute(
            "select * from BUS_JYZTZHZ where SYR_SYZTJC_ID='06c6dbd2-446b-48b9-b16e-42f4e5201d6a' and Z='34' order by CJRQ desc")
        row1 = cur.fetchone()
        print(row1)
        """商家收银主体情况表"""
        cur.execute("select * from BUS_SJSYZTQK where SYR_SYZTJC_ID='06c6dbd2-446b-48b9-b16e-42f4e5201d6a'")
        row2 = cur.fetchone()
        """拓展机构参数表"""
        k = row1[1]
        cur.execute("select * from BAS_TZJGCS where ID=%r" % k)
        row3 = cur.fetchone()
        print(row3)
        row = []
        row.append(row2[17])
        row.append(row1[5])
        row.append(row1[7])
        row.append('%.2f' % row1[12])
        row.append('%.2f' % row1[13])
        row.append('%.2f' % row1[33])
        row.append('%.2f' % row1[34])
        row.append('%.2f' % row1[29])
        row.append('%.2f' % row1[30])
        row.append('%.2f' % row1[25])
        row.append('%.2f' % row1[26])
        row.append('%.2f' % row1[38])
        row.append('%.2f' % row1[39])
        row.append('%.2f' % row1[24])
        row.append(row1[5])
        row.append(row2[5])
        row.append(row2[6])
        row.append(row2[8])
        row.append(row3[4])
        row.append(row3[10])
        print(row)
        print(result)
        if operator.eq(result, row) == True:
            print("按周查询展示数据正确")
        else:
            print("按周查询展示数据错误")
    def yuechaxun(self):
        denglu()
        result = []
        driver.find_element_by_xpath('//*[@id="hfv10_tjfs"]').click()
        driver.find_element_by_xpath('//*[@id="hfv10_tjfs"]/option[3]').click()
        driver.find_element_by_id('hfv10_monthDate').send_keys("2018-06")
        driver.find_element_by_id('hfv10_mobile').send_keys('13582087709')
        driver.find_element_by_xpath('//*[@id="btn_query"]/span[2]').click()
        sleep(1)
        for i in range(2, 4):
            num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[%r]/div' % i).text
            result.append(num1)
        for j in range(1, 13):
            if j == 1:
                num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % j)
                result.append(num2)
            else:
                num2 = float(driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % j).text.replace("￥", ""))
                result.append('%.2f' % num2)
        for k in range(13, 19):
            num3 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % k).text
            result.append(num3)
        result[2] = '2'
        """交易主体月汇总表"""
        cur.execute("select * from BUS_JYZTYHZ where SYR_SJRWJBXX_YYZZMC='华丰超市' and TJYF=to_date('2018-06','YYYY-MM')")
        row1 = cur.fetchone()
        print(row1)
        """商家收银主体情况表"""
        cur.execute("select * from BUS_SJSYZTQK where SYR_SYZTJC_ID='59d589d6-0735-4782-b4e6-9de7616bb5ab'")
        row2 = cur.fetchone()
        """拓展机构参数表"""
        k = row1[1]
        cur.execute("select * from BAS_TZJGCS where ID=%r" % k)
        row3 = cur.fetchone()
        print(row3)
        row = []
        row.append(row2[17])
        row.append(row1[5])
        row.append(row1[6])
        row.append('%.2f' % row1[9])
        row.append('%.2f' % row1[10])
        row.append('%.2f' % row1[30])
        row.append('%.2f' % row1[31])
        row.append('%.2f' % row1[26])
        row.append('%.2f' % row1[27])
        row.append('%.2f' % row1[22])
        row.append('%.2f' % row1[23])
        row.append('%.2f' % row1[35])
        row.append('%.2f' % row1[36])
        row.append('%.2f' % row1[21])
        row.append(row1[5])
        row.append(row2[5])
        row.append(row2[6])
        row.append(row2[8])
        row.append('')
        row.append('')
        print(row)
        if operator.eq(result, row) == True:
            print("按月查询展示数据正确")
        else:
            print("按月查询展示数据错误")
    def leijiyue(self):
        denglu()
        result = []
        driver.find_element_by_xpath('//*[@id="hfv10_tjfs"]').click()
        driver.find_element_by_xpath('//*[@id="hfv10_tjfs"]/option[4]').click()
        driver.find_element_by_id('hfv10_monthAccDate').send_keys("2018-07")
        driver.find_element_by_id('hfv10_mobile').send_keys('18957516227')
        driver.find_element_by_xpath('//*[@id="btn_query"]/span[2]').click()
        sleep(1)
        for i in range(2, 4):
            num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[%r]/div' % i).text
            result.append(num1)
        for j in range(1, 13):
            if j == 1:
                num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % j)
                result.append(num2)
            else:
                num2 = float(driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % j).text.replace("￥", ""))
                result.append('%.2f' % num2)
        for k in range(13, 19):
            num3 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%r]/div' % k).text
            result.append(num3)
        result[2] = '2'
        """交易主体月累计汇总表"""
        cur.execute(
            "select * from BUS_JYZTYLJHZ where SYR_SYZTJC_ID = 'aaf7d6e7-efdb-46d3-a18e-fd79d6b3d98e' and TJNY = '201807'")
        row1 = cur.fetchone()
        print(row1)
        """商家收银主体情况表"""
        cur.execute("select * from BUS_SJSYZTQK where SYR_SYZTJC_ID='aaf7d6e7-efdb-46d3-a18e-fd79d6b3d98e'")
        row2 = cur.fetchone()
        """拓展机构参数表"""
        k = row1[1]
        cur.execute("select * from BAS_TZJGCS where ID=%r" % k)
        row3 = cur.fetchone()
        print(row3)
        row = []
        row.append(row2[17])
        row.append(row1[5])
        row.append(row1[6])
        row.append('%.2f' % row1[9])
        row.append('%.2f' % row1[10])
        row.append('%.2f' % row1[28])
        row.append('%.2f' % row1[29])
        row.append('%.2f' % row1[24])
        row.append('%.2f' % row1[25])
        row.append('%.2f' % row1[20])
        row.append('%.2f' % row1[21])
        row.append('%.2f' % row1[33])
        row.append('%.2f' % row1[34])
        row.append('%.2f' % row1[19])
        row.append(row1[5])
        row.append(row2[5])
        row.append(row2[6])
        row.append(row2[8])
        row.append(row3[4])
        row.append(row3[10])
        print(row)
        print(result)
        if operator.eq(result, row) == True:
            print("按累计月查询展示数据正确")
        else:
            print("按累计月查询展示数据错误")


test = unittest.TestSuite()
test.addTest(sjjytj("richaxun"))
test.addTest(sjjytj("zhouchaxun"))
test.addTest(sjjytj("yuechaxun"))
test.addTest(sjjytj("leijiyue"))

now = time.strftime("%Y-%m-%d %H-%M-%S")
filename = "D:\\zidonghua\\zdhbg\\"+now+".html"
fp = open(filename, "wb+")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="皮夹平台-大数据中心-商家交易统计", description="用例执行情况:")
runner.run(test)
fp.close()

