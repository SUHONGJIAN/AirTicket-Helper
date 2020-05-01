from splinter import Browser
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')

# browser = Browser('chrome', options = options, headless = True)
browser = Browser('chrome', options = options)
browser.visit('https://www.jejuair.net/jejuair/cn/main.do')

browser.find_by_id('gnb_login_button0').first.click()
browser.fill('userid_1', 'suhjboy')
browser.fill('pid_1', 'fewcwkbh')
browser.find_by_id('chkIDSave').click()
browser.find_by_id('btnMemberLogin').click()
time.sleep(1)

# 选择单程和起点终点日期
browser.find_by_id('btnTripSingle').click()
browser.find_by_id('btnDepStn1').click()
browser.find_by_xpath('//*[@id="dl1"]/dd[1]/button').click()
browser.find_by_xpath('//*[@id="dl2"]/dd[9]/button').click()
browser.find_by_xpath('//*[@id="doubleCal1"]/div/div/a[2]').click()
browser.find_by_xpath('//*[@id="doubleCal1"]/div/table/tbody/tr[1]/td[6]').click()
#browser.find_by_id('dateCal1').click()
#browser.find_by_xpath('//*[@id="doubleCal1"]/div/table/tbody/tr[4]/td[4]/a').click()
browser.find_by_id('btnDoubleOk').click()
browser.find_by_id('btnReservation').click()
browser.find_by_name('divTooDep').click()

# 不确定下面第一个是否选择正确
browser.find_by_id('tdDep_0_3').click()
# browser.find_by_id('btnNextStep').click()
browser.find_by_id('btnDoNext').click()

# 输入乘客信息
browser.find_by_id('txtTelephone').type('86-15262100685')
browser.find_by_id('txtPaxTitle0').click()
browser.find_by_xpath('//*[@id="dvAdt0"]/div[1]/div/ul/li[1]').click()
browser.find_by_id('btnComplete').click()

# browser.find_by_id("closeAdPop").click()
# browser.find_by_xpath("/html/body/div[3]/div[1]/div/div[3]/div[1]/span[2]/a[1]").click()

# with browser.get_iframe('MxsLoginIframe') as iframe:    # can pass iframe's name / id / index
#     iframe.fill('UserNameInput', 'suhjboy@gmail.com')
#     iframe.fill('PasswordInput', 's1996h0418j8631')
#     iframe.find_by_id("IsKeepLoginState").click()
#     iframe.find_by_id("account-submit").click()

# browser.fill('OriCity', '首尔')

# browser.quit()