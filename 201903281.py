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

url="https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=ipx00232/?i3_ref=search&i3_ord=1"

#chrome_options = Options()
#chrome_options.add_argument("--headless")       # define headless
#driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome()     #開啟chrome
action = ActionChains(driver) #模擬按鍵 宣告
#driver.get(url+url2)
driver.get(url)
time.sleep(3) #延遲三秒
action.move_by_offset(10, 50).perform() #移動滑鼠
time.sleep(3)
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='サービス'])[1]/preceding::img[1]").click()

html = driver.page_source       # get html
driver.get_screenshot_as_file("E:\\sreenshot1.png") 
bs = BeautifulSoup(driver.page_source, "lxml")
bss=bs.prettify()
fp=open('E:\\file.html', 'wb')
fp.write(bss.encode('utf-8'))
#print(tag.encode('utf-8'),file=fp)
fp.close