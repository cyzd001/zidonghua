from appium import webdriver
import time
from PIL import Image, ImageEnhance
# import baseinfo
from pytesseract import *
from pymouse import PyMouse
from pykeyboard import PyKeyboard
desired_caps = {
    #设备系统
    'platformName': 'Android',
    #设备名称
    'deviceName': '127.0.0.1:7555',
    #安卓版本
    'platformVersion': '6.0.1',
    # apk包名
    'appPackage': 'org.cocos2d.huihuang07_openVersion',
    # apk的launcherActivity
    'appActivity': 'org.cocos2dx.javascript.AppActivity',
    'unicodeKeyboard': True,  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
     'resetKeyboard':False,# 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来
}
#aapt dump badging D:\huihuang07_openVersion-release-signed.apk  通过此命令获取apk包名和apk的launcherActivity
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(30)

keycode = {}
keycode['0'] = '7'
keycode['1'] = '8'
keycode['2'] = '9'
keycode['3'] = '10'
keycode['4'] = '11'
keycode['5'] = '12'
keycode['6'] = '13'
keycode['7'] = '14'
keycode['8'] = '15'
keycode['9'] = '16'
keycode['a'] = '29'
keycode['b'] = '30'
keycode['c'] = '31'
keycode['d'] = '32'
keycode['e'] = '33'
keycode['f'] = '34'
keycode['g'] = '35'
keycode['h'] = '36'
keycode['i'] = '37'
keycode['j'] = '38'
keycode['k'] = '39'
keycode['l'] = '40'
keycode['m'] = '41'
keycode['n'] = '42'
keycode['o'] = '43'
keycode['p'] = '44'
keycode['q'] = '45'
keycode['r'] = '46'
keycode['s'] = '47'
keycode['t'] = '48'
keycode['u'] = '49'
keycode['v'] = '50'
keycode['w'] = '51'
keycode['x'] = '52'
keycode['y'] = '53'
keycode['z'] = '54'




def shuru(asdf):
    m = asdf
    for i in m:
        driver.press_keycode(keycode[i])

m = PyMouse()
driver.tap([(636,648)],100)
time.sleep(2)
driver.tap([(601,327)],100)
# k = PyKeyboard()
# k.type_string("qwaskb0001")
# print(driver.press_keycode('7'))
# driver.close_app()  #关闭app
print(driver.available_ime_engines)  #获取手机输入法返回一个list
driver.activate_ime_engine('com.netease.nemu_vinput.nemu/com.android.inputmethodcommon.SoftKeyboard')
"""输入账号qwaskb001"""
shuru('qwaskb001')
# zhanghao =['45','51','29','47','39','30','7','7','8']
# for i in zhanghao:
#     driver.press_keycode(i)
driver.tap([(616,425)],100)
"""输入密码qwaszx12"""
mima = ['45','51','29','47','54','52','8','9']
for j in mima:
    driver.press_keycode(j)
driver.tap([(659,563)],100)
time.sleep(5)
driver.tap([(1121,754)],100)
time.sleep(2)
driver.tap([(789,262)],100)
driver.activate_ime_engine('com.netease.nemu_vinput.nemu/com.android.inputmethodcommon.SoftKeyboard')
"""输入账号qwaskb001"""
jine =['8','8','8']
for i in jine:
    driver.press_keycode(i)
driver.tap([(849,587)],100)
time.sleep(2)
driver.tap([(568,413)],100)
driver.activate_ime_engine('com.netease.nemu_vinput.nemu/com.android.inputmethodcommon.SoftKeyboard')
"""输入账号qwaskb001"""
bao =['8','9','10','11','12','13']
for i in bao:
    driver.press_keycode(i)
driver.tap([(680,531)],100)
time.sleep(2)
driver.tap([(719,538)],100)
time.sleep(2)
print("充值成功")
driver.tap([(1308,89)],100)


