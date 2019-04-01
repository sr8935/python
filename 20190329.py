#電子採購網
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

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless

driver = webdriver.Chrome(chrome_options=chrome_options)
#soup = BeautifulSoup("http://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance", 'html.parser')
#print(soup)

#driver = webdriver.Chrome()     # 打开 Chrome 浏览器
driver.get("http://web.pcc.gov.tw/tps/pss/tender.do?method=goSearch&searchMode=common&searchType=basic")
driver.find_element_by_link_text(u"招標查詢").click()
driver.find_element_by_id("searchTargetTPAM").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='履約地點'])[1]/following::input[1]").click()
time.sleep(1)
driver.find_element_by_id("dynamicCelocation_selectI").click()
time.sleep(1)
Select(driver.find_element_by_id("dynamicCelocation_selectI")).select_by_visible_text(u"新北市(非原住民地區)")
time.sleep(1)
driver.find_element_by_id("radProctrgCate1").click()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='採購級距'])[1]/following::td[1]").click()
driver.find_element_by_id("btnQuery").click()

html = driver.page_source       # get html
bs = BeautifulSoup(driver.page_source, "lxml")
driver.get_screenshot_as_file("E:\\sreenshot1.png")

print(html)
#file.write(html)
#print(,f2='E:\\file.txt')
fp=open('E:\\file.html', 'wb')
#fp.write(bs)
fp.write(bs.encode('utf-8'))
fp.close
driver.close()