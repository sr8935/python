#DMM
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time
import unittest, time, re
import requests
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#123123
url='https://www.dmm.co.jp/'
url2='search/=/searchstr=%E7%9B%B8%E6%B2%A2%E3%81%BF%E3%81%AA%E3%81%BF/limit=120/n1=FgRCTw9VBA4GAVhfWkIHWw__/'

#chrome_options = Options()
#chrome_options.add_argument("--headless")       # define headless
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()     #開啟chrome
action = ActionChains(driver) #模擬按鍵 宣告
#driver.get(url+url2)
driver.get("https://www.dmm.co.jp/digital/")
time.sleep(3) #延遲三秒
action.move_by_offset(10, 50).perform() #移動滑鼠
time.sleep(3)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='サービス'])[1]/preceding::img[1]").click()
driver.find_element_by_id("searchstr").click()
driver.find_element_by_id("searchstr").clear()
driver.find_element_by_id("searchstr").send_keys(u"相沢みなみ")
driver.find_element_by_name("commit").click()
driver.find_element_by_link_text("120").click()

html = driver.page_source       # get html
driver.get_screenshot_as_file("E:\\sreenshot1.png") 
bs = BeautifulSoup(driver.page_source, "lxml")
bss=bs.prettify()
#tag = bs.select("p > tmb")
#tags = bs.find_all('p' ,class='tmb')
tagg =bs.find_all('a',{'href':re.compile('https://www.dmm.co.jp/digital/videoa/-/detail/=/.*')})
tag = bs.find_all('p',class_='tmb')

for s in tagg:
    #print(s.find('a',{'href':True}))
    print(s.get('href'))
    
    # 新聞標題
    #print("標題：" + s.text)
    # 新聞網址
    #print("網址：" + s.get('href'))
    #print(s.get('href'))
#print(tag)
fp=open('E:\\file.html', 'wb')
fp.write(bss.encode('utf-8'))
#print(tag.encode('utf-8'),file=fp)
fp.close


#driver.close()


'''
r = requests.get(url+url2)
#if r.status_code == requests.codes.ok:
soup = BeautifulSoup(r.text, 'html.parser')
print(soup)
'''
