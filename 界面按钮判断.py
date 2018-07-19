from selenium import webdriver
from time import sleep

option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

#打开网页
driver = webdriver.Chrome(chrome_options=option)
driver.get("http://lb-test.com/#/passport/login")
sleep(1)
#输入账号和密码
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/form/div[1]/div/div[1]/input').send_keys("sb002")
driver.find_element_by_xpath('//*[@placeholder="请输入密码"]').send_keys("qwaszx1")
driver.find_element_by_xpath('//*[@placeholder="请输入验证码"]').send_keys("8888")

# 点击登录
driver.find_element_by_xpath('//*[@type="submit"]').click()
sleep(1)
# 分三步进入重庆时时彩界面
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/ul/li[5]/a/div').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/ul/li[5]/a/div').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/div').click()
sleep(1)
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/ul[5]/li[1]').click()
sleep(1)
try:
    if driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/ul/li[2]'):
        driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[1]/ul/li[2]').click()
except:
    print ("未找到双面玩法按钮")
driver.quit()


