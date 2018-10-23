from appium import webdriver
import time
import cx_Oracle as oracle
import xlrd

def yanzhengma(number):
    db = oracle.connect('pj_extbank', 'pj_extbank', '192.168.55.5:1521/ljcprd')
    cur = db.cursor()
    cur.execute("select YZM from EXT_YZM where SJH = '%r' order by CJSJ desc"%number)
    row = cur.fetchone()
    yanzheng = row[0]
    print(yanzheng)
    db.close()
    return yanzheng
desired_caps = {
    #设备系统
    'platformName': 'Android',
    #设备名称
    'deviceName': '127.0.0.1:62001',
    #安卓版本
    'platformVersion': '4.4.2',
    # apk包名
    'appPackage': 'com.huiyinxun.wallet.laijc',
    # apk的launcherActivity
    'appActivity': 'com.huiyinxun.wallet.laijc.ui.welcome.activity.WelcomeActivity',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
     'resetKeyboard':True,# 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)
driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/tv_cancel').click()
for i in range(4):
    # 打印屏幕高和宽
    print(driver.get_window_size())
    # 获取屏幕的高
    x = driver.get_window_size()['width']
    # 获取屏幕宽
    y = driver.get_window_size()['height']
    driver.swipe(6 / 7 * x, 1 / 2 * y, 1 / 7 * x, 1 / 2 * y, 300)
    time.sleep(1)
driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/btn_welcome').click()
driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/tv_register').click()
excel = xlrd.open_workbook(u'来聚财注册号码.xls')
nums = excel.sheet_by_index(0)
row = nums.nrows
for i in range(1,row):
    num=int(nums.cell(i, 0).value)
    print(num)
    driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/register_username').send_keys(num)
    driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/btn_countdown').click()
    time.sleep(2)
    driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/security_code').send_keys(yanzhengma(num))
    driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/register_password').send_keys(123456)
    driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/register_again_password').send_keys(123456)
    driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/btn_register').click()
    time.sleep(1)
    driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/tv_register').click()


driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/iv_business').click()

