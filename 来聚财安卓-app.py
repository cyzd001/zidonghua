from appium import webdriver
import time
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
time.sleep(4)
driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/tv_cancel').click()
for i in range(4):
    # 打印屏幕高和宽
    print(driver.get_window_size())
    # 获取屏幕的高
    x = driver.get_window_size()['width']
    # 获取屏幕宽
    y = driver.get_window_size()['height']
    driver.swipe(6 / 7 * x, 1 / 2 * y, 1 / 7 * x, 1 / 2 * y, 300)
    time.sleep(2)
driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/btn_welcome').click()
driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/login_username').send_keys(17725848455)
driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/login_password').send_keys('1234ab')
driver.find_element_by_id('com.huiyinxun.wallet.laijc:id/btn_login').click()
time.sleep(1)
driver.find_element_by_id('android:id/button1').click()
driver.find_element_by_xpath('//*[@class="android.widget.LinearLayout"]').click()
str = driver.find_element_by_xpath('//*[@text="今日收益"]').is_displayed()
print(str)
if str == True:
    print("成功打开来聚财app")
else:
    print("成功打开来聚财app")


