from selenium import webdriver
from time import sleep
import time
import unittest
import sys
print(sys.path)
sys.path.append('E:\\xuexi')
sys.path.append('C:\\Program Files\\JetBrains\\PyCharm 2018.1.3\\helpers\\pycharm')
sys.path.append('D:\\Python\\Python36\\python36.zip')
sys.path.append('D:\\Python\\Python36\\DLLs')
sys.path.append('D:\\Python\\Python36\\lib')
sys.path.append('D:\\Python\\Python36')
sys.path.append('D:\\Python\\Python36\\lib\\site-packages')
sys.path.append('D:\\Python\\Python36\\lib\\site-packages\\win32')
sys.path.append('D:\\Python\\Python36\\lib\\site-packages\\win32\\lib')
sys.path.append('D:\\Python\\Python36\\lib\\site-packages\\Pythonwin')
sys.path.append('C:\\Program Files\\JetBrains\\PyCharm 2018.1.3\\helpers\\pycharm_matplotlib_backend')
sys.path.append('E:\\xuexi\\zidonghua')


import HTMLTestRunner
import xmlrunner
import random


def qianzhi001(driver):

    driver.get("http://lb-test.com/#/passport/login")
    """输入账号和密码"""
    driver.find_element_by_xpath('//*[@placeholder="请输入账号"]').send_keys("sb001")
    driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys("qwaszx")
    driver.find_element_by_xpath('//*[@placeholder="请输入验证码"]').send_keys("8888")
    """点击登录"""
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    """双面玩法全投"""
    sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/div/ul/li[2]/a').click()
    sleep(2)
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[2]/div/div/ul/li[2]/div/div/ul[1]/li[3]/a').click()
    sleep(2)
    for i in range(2, 12):
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/ul/li[%d]/span[3]/div/input' % (
                i)).send_keys(1)
    """点击提交投注"""
    driver.find_element_by_xpath(
        '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[6]/a[1]').click()
    sleep(2)
    """确认投注弹框出现"""
    driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
    sleep(1)
    """投注成功弹框出现"""
    driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
    sleep(1)
"""生成不重复随机数，范围在0到9之间"""
def suiji(num):
    result =[]
    total = 1
    while total <= num:
        temp = random.randint(0, 9)
        if temp not in result:
            result.append(temp)
            total = total + 1
    return result
class qcssctest(unittest.TestCase):
    '''游戏运行情况'''
    def panduan(self):
        '''识别网站'''
        driver = webdriver.Firefox()
        driver.get("http://lb-test.com/")
        option = webdriver.FirefoxOptions()
        option.add_argument('headless')
        sleep(1)
        '''获取当前的title'''
        title = driver.title
        print(title)
        if title == "皇家彩世界":
            print("目前打开的是皇家彩世界")
        elif title == "49彩票":
            print("目前打开的是49彩票")
        elif title == "宝开彩票":
            print("目前打开的是宝开彩票")
        elif title == "盈彩吧":
            print("目前打开的是盈彩吧")
        else:
            print("目前打开的是龙彩")
        driver.quit()
    def qcssc_shuzipan_test(self):
        '''数字盘'''
        driver = webdriver.Firefox()
        driver.get("http://lb-test.com/#/passport/login")
        """输入账号和密码"""
        driver.find_element_by_xpath('//*[@placeholder="请输入账号"]').send_keys("sb001")
        driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys("qwaszx")
        driver.find_element_by_xpath('//*[@placeholder="请输入验证码"]').send_keys("8888")
        """点击登录"""
        driver.find_element_by_xpath('//*[@type="submit"]').click()
        """数字盘玩法全投"""
        sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[2]/div/div/ul/li[2]/a').click()
        sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div/div/ul/li[2]/div/div/ul[1]/li[3]/a').click()
        sleep(1)
        """万位投注"""
        for i in range(2, 12):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/ul/li[%d]/span[3]/div/input' % (
                    i)).send_keys(1)
        """"千位投注"""
        for j in range(2, 12):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    j)).send_keys(1)
        """"百位投注"""
        for k in range(2, 12):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/ul/li[%d]/span[3]/div/input' % (
                    k)).send_keys(1)
        """"十位投注"""
        for l in range(2, 12):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/ul/li[%d]/span[3]/div/input' % (
                    l)).send_keys(1)
        """"个位投注"""
        for m in range(2, 12):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[5]/ul/li[%d]/span[3]/div/input' % (
                    m)).send_keys(1)
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[6]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_shuangmian_test(self):
        '''双面'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        sleep(1)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[2]').click()
        """万位投注"""
        for i in range(2, 8):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/ul/li[%d]/span[3]/div/input' % (
                    i)).send_keys(1)
        """"千位投注"""
        for j in range(2, 8):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    j)).send_keys(1)
        """"百位投注"""
        for k in range(2, 8):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/ul/li[%d]/span[3]/div/input' % (
                    k)).send_keys(1)
        """"十位投注"""
        for l in range(2, 8):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/ul/li[%d]/span[3]/div/input' % (
                    l)).send_keys(1)
        """"十位投注"""
        for m in range(2, 8):
            driver.find_element_by_xpath(
                '//html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[5]/ul/li[%d]/span[3]/div/input' % (
                    m)).send_keys(1)
        for p in range(1, 5):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    p)).send_keys(1)
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[7]/a[1]').click()
        sleep(1)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizidingweiwan_test(self):
        """一字定位(万位)"""
        driver = webdriver.Firefox()
        qianzhi001(driver)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[3]').click()
        for i in range(1,17):
            driver.find_element_by_xpath(
                '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    i)).send_keys(1)
        for j in range(1,5):
            driver.find_element_by_xpath(
                '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    j)).send_keys(1)
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[3]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizidingweiqian_test(self):
        '''一字定位(千位)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[3]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[2]').click()
        for i in range(1, 17):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    i)).send_keys(1)
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizidingweibai_test(self):
        '''一字定位(百位)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[3]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[3]').click()
        for i in range(1, 17):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    i)).send_keys(1)
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizidingweishi_test(self):
        '''一字定位(十位)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[3]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[4]').click()
        for i in range(1, 17):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    i)).send_keys(1)
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizidingweige_test(self):
        '''一字定位(个位)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[3]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[5]').click()
        for i in range(1, 17):
            driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[3]/div/input' % (
                    i)).send_keys(1)
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweiwanqian_test(self):
        '''二字定位(万千)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[1]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        ww = random.randint(0,9)
        qw = random.randint(0,9)
        print("万位:",ww,"千位:",qw)
        '''万位'''
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span'%(ww+2)).click()
        '''千位'''
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span'%(qw+2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweiwanbai_test(self):
        '''二字定位(万百)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[2]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        ww = random.randint(0, 9)
        bw = random.randint(0, 9)
        print("万位:", ww, "百位:", bw)
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        ww + 2)).click()
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        bw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweiwanshi_test(self):
        '''二字定位(万十)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[3]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        ww = random.randint(0, 9)
        sw = random.randint(0, 9)
        print("万位:", ww, "十位:", sw)
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        ww + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        sw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweiwange_test(self):
        '''二字定位(万个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[4]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        ww = random.randint(0, 9)
        gw = random.randint(0, 9)
        print("万位:", ww, "个位:", gw)
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        ww + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweiqianbai_test(self):
        '''二字定位(千百)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[5]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        qw = random.randint(0, 9)
        bw = random.randint(0, 9)
        print("千位:", qw, "百位:", bw)
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        qw + 2)).click()
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        bw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweiqianshi_test(self):
        '''二字定位(千十)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[6]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        qw = random.randint(0, 9)
        sw = random.randint(0, 9)
        print("千位:", qw, "十位:", sw)
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        qw + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        sw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweiqiange_test(self):
        '''二字定位(千个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[7]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        qw = random.randint(0, 9)
        gw = random.randint(0, 9)
        print("千位:", qw, "个位:", gw)
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        qw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweibaishi_test(self):
        '''二字定位(百十)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[8]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        bw = random.randint(0, 9)
        sw = random.randint(0, 9)
        print("百位:", bw, "十位:", sw)
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        bw + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        sw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweibaige_test(self):
        '''二字定位(百个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[9]').click()
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        bw = random.randint(0, 9)
        gw = random.randint(0, 9)
        print("百位:", bw, "个位:", gw)
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        bw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_erzidingweishige_test(self):
        '''二字定位(十个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[4]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[10]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择号码'''
        sw = random.randint(0, 9)
        gw = random.randint(0, 9)
        print("十位:", sw, "个位:", gw)
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        sw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiwqb_test(self):
        '''三字定位(万千百)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[1]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        ww = random.randint(0, 9)
        bw = random.randint(0, 9)
        qw = random.randint(0, 9)
        print("千位:", qw, "百位:", bw,"万位:", ww)
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        qw + 2)).click()
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        bw + 2)).click()
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    ww + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiwqs_test(self):
        '''三字定位(万千十)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[2]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        ww = random.randint(0, 9)
        sw = random.randint(0, 9)
        qw = random.randint(0, 9)
        print("千位:", qw, "十位:", sw,"万位:", ww)
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        ww + 2)).click()
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        qw + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    sw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiwqg_test(self):
        '''三字定位(万千个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[3]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        ww = random.randint(0, 9)
        gw = random.randint(0, 9)
        qw = random.randint(0, 9)
        print("千位:", qw, "个位:", gw,"万位:", ww)
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        ww + 2)).click()
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        qw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiwbs_test(self):
        '''三字定位(万百十)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[4]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        ww = random.randint(0, 9)
        bw = random.randint(0, 9)
        sw = random.randint(0, 9)
        print("百位:", bw, "十位:", sw,"万位:", ww)
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        ww + 2)).click()
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        bw + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    sw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiwbg_test(self):
        '''三字定位(万百个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[5]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        ww = random.randint(0, 9)
        bw = random.randint(0, 9)
        gw = random.randint(0, 9)
        print("百位:", bw, "个位:", gw,"万位:", ww)
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        ww + 2)).click()
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        bw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiwsg_test(self):
        '''三字定位(万十个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[6]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        ww = random.randint(0, 9)
        sw = random.randint(0, 9)
        gw = random.randint(0, 9)
        print("十位:", sw, "个位:", gw,"万位:", ww)
        '''万位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        ww + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        sw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiqbs_test(self):
        '''三字定位(千百十)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[7]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        qw = random.randint(0, 9)
        sw = random.randint(0, 9)
        bw = random.randint(0, 9)
        print("十位:", sw, "百位:", bw,"千位:", qw)
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        qw + 2)).click()
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        bw + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    sw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiqbg_test(self):
        '''三字定位(千百个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[8]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        qw = random.randint(0, 9)
        gw = random.randint(0, 9)
        bw = random.randint(0, 9)
        print("个位:", gw, "百位:", bw,"千位:", qw)
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        qw + 2)).click()
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        bw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweiqsg_test(self):
        '''三字定位(千十个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[9]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        qw = random.randint(0, 9)
        sw = random.randint(0, 9)
        gw = random.randint(0, 9)
        print("十位:", sw, "个位:", gw,"千位:", qw)
        '''千位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        qw + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        sw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_sanzidingweibsg_test(self):
        '''三字定位(百十个)'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[5]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[10]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        sw = random.randint(0, 9)
        gw = random.randint(0, 9)
        bw = random.randint(0, 9)
        print("个位:", gw, "百位:", bw,"十位:", sw)
        '''百位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[1]/li[%d]/span' % (
                        bw + 2)).click()
        '''十位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[2]/li[%d]/span' % (
                        sw + 2)).click()
        '''个位'''
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[3]/li[%d]/span' % (
                    gw + 2)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizizuhequanwu_test(self):
        '''全五一字组合'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[6]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[1]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        for i in range(1,11):
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[2]'%(i)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizizuheqiansan_test(self):
        '''前三一字组合'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[6]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[2]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        for i in range(1,11):
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[2]'%(i)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizizuhezhongsan_test(self):
        '''中三一字组合'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[6]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[3]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        for i in range(1,11):
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[2]'%(i)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_yizizuhehousan_test(self):
        '''后三一字组合'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[6]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[4]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        for i in range(1,11):
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[2]'%(i)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_zuxuansanqiansan_test(self):
        '''组选三前三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[7]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[1]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择5个号码'''
        for i in suiji(5):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span'%(i+1)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_zuxuansanzhongsan_test(self):
        '''组选三中三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[7]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[2]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择5个号码'''
        for i in suiji(5):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span'%(i+1)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_zuxuansanhousan_test(self):
        '''组选三后三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[7]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[3]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择5个号码'''
        for i in suiji(5):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span'%(i+1)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_zuxuanliuqiansan_test(self):
        '''组选六前三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[8]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[1]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择5个号码'''
        for i in suiji(5):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span'%(i+1)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_zuxuanliuzhongsan_test(self):
        '''组选六中三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[8]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[2]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择5个号码'''
        for i in suiji(5):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span'%(i+1)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_zuxuanliuhousan_test(self):
        '''组选六后三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[8]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[3]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        '''选择5个号码'''
        for i in suiji(5):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span'%(i+1)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_kuangduqiansan_test(self):
        '''跨度前三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[9]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[1]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        for i in range(1,11):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[1]'%(i)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_kuangduzhongsan_test(self):
        '''跨度中三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[9]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[2]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        for i in range(1,11):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[1]'%(i)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_kuangduhousan_test(self):
        '''跨度后三'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[9]').click()
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[1]/ul/li/span[2]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)
        for i in range(1,11):
            driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul/li[%d]/span[1]'%(i)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()
    def qcssc_longhu_test(self):
        '''龙虎'''
        driver = webdriver.Firefox()
        qianzhi001(driver)
        driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div[2]/div[1]/div[1]/ul/li[10]').click()
        sleep(1)
        '''快捷金额'''
        driver.find_element_by_xpath('//*[@id="quickAmount"]').send_keys(1)

        for i in range(1,11):
            for j in range(2,5):
                driver.find_element_by_xpath(
                    '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/ul[%d]/li[%d]/span[1]' % (i,j)).click()
        """点击提交投注"""
        driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/div/a[1]').click()
        sleep(2)
        """确认投注弹框出现"""
        driver.find_element_by_xpath('//*[@class="notify-btn notify-btn-primary notify-btn-small"]').click()
        sleep(1)
        """投注成功弹框出现"""
        driver.find_element_by_xpath('//*[@class="swal-button swal-button--confirm"]').click()
        driver.quit()





test = unittest.TestSuite()
test.addTest(qcssctest("panduan"))
test.addTest(qcssctest("qcssc_shuzipan_test"))
test.addTest(qcssctest("qcssc_shuangmian_test"))
test.addTest(qcssctest("qcssc_yizidingweiwan_test"))
# test.addTest(qcssctest("qcssc_yizidingweiqian_test"))
# test.addTest(qcssctest("qcssc_yizidingweibai_test"))
# test.addTest(qcssctest("qcssc_yizidingweishi_test"))
# test.addTest(qcssctest("qcssc_yizidingweige_test"))
# test.addTest(qcssctest("qcssc_erzidingweiwanqian_test"))
# test.addTest(qcssctest("qcssc_erzidingweiwanbai_test"))
# test.addTest(qcssctest("qcssc_erzidingweiwanshi_test"))
# test.addTest(qcssctest("qcssc_erzidingweiwange_test"))
# test.addTest(qcssctest("qcssc_erzidingweiqianbai_test"))
# test.addTest(qcssctest("qcssc_erzidingweiqianshi_test"))
# test.addTest(qcssctest("qcssc_erzidingweiqiange_test"))
# test.addTest(qcssctest("qcssc_erzidingweibaishi_test"))
# test.addTest(qcssctest("qcssc_erzidingweibaige_test"))
# test.addTest(qcssctest("qcssc_erzidingweishige_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiwqb_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiwqs_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiwqg_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiwbs_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiwbg_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiwsg_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiqbs_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiqbg_test"))
# test.addTest(qcssctest("qcssc_sanzidingweiqsg_test"))
# test.addTest(qcssctest("qcssc_sanzidingweibsg_test"))
# test.addTest(qcssctest("qcssc_yizizuhequanwu_test"))
# test.addTest(qcssctest("qcssc_yizizuheqiansan_test"))
# test.addTest(qcssctest("qcssc_yizizuhezhongsan_test"))
# test.addTest(qcssctest("qcssc_yizizuhehousan_test"))
# test.addTest(qcssctest("qcssc_zuxuansanqiansan_test"))
# test.addTest(qcssctest("qcssc_zuxuansanzhongsan_test"))
# test.addTest(qcssctest("qcssc_zuxuansanhousan_test"))
# test.addTest(qcssctest("qcssc_zuxuanliuqiansan_test"))
# test.addTest(qcssctest("qcssc_zuxuanliuzhongsan_test"))
# test.addTest(qcssctest("qcssc_zuxuanliuhousan_test"))
# test.addTest(qcssctest("qcssc_kuangduqiansan_test"))
# test.addTest(qcssctest("qcssc_kuangduzhongsan_test"))
# test.addTest(qcssctest("qcssc_kuangduhousan_test"))
# test.addTest(qcssctest("qcssc_longhu_test"))


now=time.strftime("%Y-%m-%d %H-%M-%S")
filename = "E:\\xuexi\\zdhbaogao\\"+now+".html"
fp = open(filename, "wb+")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="PC端自动化测试报告", description="用例执行情况:")
runner.run(test)
fp.close()



