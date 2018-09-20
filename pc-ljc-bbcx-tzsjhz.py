from selenium import webdriver
from time import sleep
import time
import HTMLTestRunner
import unittest
import cx_Oracle as oracle
import os
import operator
import datetime

"""来聚财-报表查询-拓展网点统计-拓展商家汇总"""
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
driver = webdriver.Chrome()
db = oracle.connect('pj_rep', 'pj_rep', '192.168.55.5:1521/ljcprd')
cur = db.cursor()
def denglu():
    driver.get("http://192.168.55.26:8080/aus-nk-bank/mainframe/login.jsp")
    driver.find_element_by_id('uname').send_keys('cs00001')
    driver.find_element_by_id('pword').send_keys('test123')
    driver.find_element_by_id('btn_login').click()
    driver.maximize_window()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="menudiv"]/div[7]/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="menudiv"]/div[7]/div[3]/div[1]/div').click()
    driver.find_element_by_xpath('//*[@id="menudiv"]/div[7]/div[3]/div[5]/div/div').click()
    driver.switch_to.frame("tabpage1_pf1")
    sleep(1)
def sanjiri():
    """三级分行查询"""
    denglu()
    result = []
    row = []
    driver.find_element_by_id('select2-hfv10_yjfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_yjfh"]/option[4]').click()
    driver.find_element_by_id('select2-hfv10_ejfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_ejfh"]/option[2]').click()
    driver.find_element_by_id('select2-hfv10_sjfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_sjfh"]/option[2]').click()
    driver.find_element_by_id('hfv10_dayDateStart').send_keys('2018-08-01')
    driver.find_element_by_id('hfv10_dayDateEnd').send_keys('2018-08-28')
    driver.find_element_by_id('btn_query').click()
    sleep(1)
    num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[2]/div').text
    result.append(num1)
    for i in range(1, 13):
        if i >= 2 and i <= 9:
            num2 = int(driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]/div' % i).text)
            result.append(num2)
        else:
            num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]/div' % i).text
            result.append(num2)
    """拓展机构参数表"""
    cur.execute("select * from BAS_TZJGCS where JGMC = %r" % result[0])
    row1 = cur.fetchone()
    row.append(row1[3])
    row.append('合计')
    """机构拓展日汇总表 """
    cur.execute(
        "select sum(TZS),sum(RWS),sum(BHS),sum(JHS),sum(DJHS),sum(JYSHS),sum(LJYSHS) from (select * from BUS_JGTZRHZ where SYR_TZJGCS_ID='0000003452') where TJRQ between to_date('2018-08-01','YYYY-MM-DD') and to_date('2018-08-28','YYYY-MM-DD')")
    row2 = cur.fetchone()
    cur.execute(
        "select sum(CLZS) from BUS_JGTZRHZ where SYR_TZJGCS_ID='0000003452' and  TJRQ=to_date('2018-08-28','YYYY-MM-DD')")
    row3 = cur.fetchone()
    row.append(row2[0])
    row.append(row2[1])
    row.append(row2[2])
    row.append(row2[3])
    row.append(row2[4])
    row.append(row3[0])
    row.append(row2[5])
    row.append(row2[6])
    row.append(row1[7])
    row.append(row1[8])
    row.append("2018-08-01至2018-08-28")
    print(row)
    if operator.eq(result, row) == True:
        print("展示数据正确")
    else:
        print("展示数据错误")
def erjiri():
    """二级分行查询"""
    denglu()
    result = []
    row = []
    driver.find_element_by_id('select2-hfv10_yjfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_yjfh"]/option[4]').click()
    driver.find_element_by_id('select2-hfv10_ejfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_ejfh"]/option[2]').click()
    driver.find_element_by_id('hfv10_dayDateStart').send_keys('2018-08-01')
    driver.find_element_by_id('hfv10_dayDateEnd').send_keys('2018-08-28')
    driver.find_element_by_id('btn_query').click()
    sleep(1)
    num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[2]/div').text
    result.append(num1)
    for i in range(1, 13):
        if i >= 2 and i <= 9:
            num2 = int(driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]/div' % i).text)
            result.append(num2)
        else:
            num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]/div' % i).text
            result.append(num2)
    """拓展机构参数表"""
    cur.execute("select * from BAS_TZJGCS where JGMC = %r" % result[0])
    row1 = cur.fetchone()
    row.append(row1[3])
    row.append('合计')
    """机构拓展日汇总表 """
    cur.execute(
        "select sum(TZS),sum(RWS),sum(BHS),sum(JHS),sum(DJHS),sum(JYSHS),sum(LJYSHS) from"
        " (select * from BUS_JGTZRHZ where SYR_TZJGCS_ID='0000003452') where TJRQ between to_date('2018-08-01','YYYY-MM-DD') and to_date('2018-08-28','YYYY-MM-DD')")
    row2 = cur.fetchone()
    cur.execute(
        "select sum(CLZS) from BUS_JGTZRHZ where SYR_TZJGCS_ID='0000003452' and  TJRQ=to_date('2018-08-28','YYYY-MM-DD')")
    row3 = cur.fetchone()
    row.append(row2[0])
    row.append(row2[1])
    row.append(row2[2])
    row.append(row2[3])
    row.append(row2[4])
    row.append(row3[0])
    row.append(row2[5])
    row.append(row2[6])
    row.append(row1[7])
    row.append(row1[8])
    row.append("2018-08-01至2018-08-28")
    print(row)
    if operator.eq(result, row) == True:
        print("展示数据正确")
    else:
        print("展示数据错误")
def yijiri():
    denglu()
    result = []
    row = []
    driver.find_element_by_id('select2-hfv10_yjfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_yjfh"]/option[4]').click()
    driver.find_element_by_id('hfv10_dayDateStart').send_keys('2018-08-01')
    driver.find_element_by_id('hfv10_dayDateEnd').send_keys('2018-08-28')
    driver.find_element_by_id('btn_query').click()
    sleep(1)
    num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[2]/div').text
    result.append(num1)
    for i in range(1, 13):
        if i >= 2 and i <= 9:
            num2 = int(driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]/div' % i).text)
            result.append(num2)
        else:
            num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]/div' % i).text
            result.append(num2)
    print(result)
    """拓展机构参数表"""
    cur.execute("select * from BAS_TZJGCS where JGMC = %r" % result[0])
    row1 = cur.fetchone()
    row.append(row1[3])
    row.append('合计')
    str = '00000-0000000001-0000000005-' + row1[0]
    """机构拓展日汇总表 """
    cur.execute("select sum(TZS),sum(RWS),sum(BHS),sum(JHS),sum(DJHS),sum(JYSHS),sum(LJYSHS) from "
                "(select * from BUS_JGTZRHZ where SYR_TZJGCS_ID in (select id from BAS_TZJGCS where SJJGQLJ = %r))"
                " where TJRQ between to_date('2018-08-01','YYYY-MM-DD') and to_date('2018-08-28','YYYY-MM-DD')" % str)
    row2 = cur.fetchone()
    cur.execute(
        "select sum(CLZS) from BUS_JGTZRHZ where SYR_TZJGCS_ID in (select id from BAS_TZJGCS where SJJGQLJ = %r) and  TJRQ=to_date('2018-08-28','YYYY-MM-DD')" % str)
    row3 = cur.fetchone()
    row.append(row2[0])
    row.append(row2[1])
    row.append(row2[2])
    row.append(row2[3])
    row.append(row2[4])
    row.append(row3[0])
    row.append(row2[5])
    row.append(row2[6])
    row.append(row1[7])
    row.append(row1[8])
    row.append("2018-08-01至2018-08-28")
    print(row)
    if operator.eq(result, row) == True:
        print("展示数据正确")
    else:
        print("展示数据错误")
def sanjizhou():
    denglu()
    result = []
    row = []
    driver.find_element_by_id('select2-hfv10_yjfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_yjfh"]/option[4]').click()
    driver.find_element_by_id('select2-hfv10_ejfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_ejfh"]/option[2]').click()
    driver.find_element_by_id('select2-hfv10_sjfh-container').click()
    driver.find_element_by_xpath('//*[@id="hfv10_sjfh"]/option[2]').click()
    driver.find_element_by_id('hfv10_tjfs').click()
    driver.find_element_by_xpath('//*[@id="hfv10_tjfs"]/option[2]').click()
    driver.find_element_by_id('hfv10_weekDate').send_keys('2018-08-21')
    driver.find_element_by_id('btn_query').click()
    sleep(1)
    num1 = driver.find_element_by_xpath('//*[@id="hgv1fr0"]/td[2]/div').text
    result.append(num1)
    for i in range(1, 13):
        if i >= 2 and i <= 9:
            num2 = int(driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]/div' % i).text)
            result.append(num2)
        else:
            num2 = driver.find_element_by_xpath('//*[@id="hgv1mr0"]/td[%s]/div' % i).text
            result.append(num2)
    print(result)

sanjizhou()


# driver.quit()