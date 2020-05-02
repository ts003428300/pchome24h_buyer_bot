# -*- coding: utf-8 -*-
"""
Created on Sat May  2 22:43:24 2020

@author: Nick
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:28:04 2020

@author: Nick
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:16:24 2020

@author: Nick
"""
''''''
# Need to Empty your Chart 
''''''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import sys

username = ''  ## pchome 24h account
password = ''  ## password
mobile = ''    ## mobile
## Product
url = 'https://24h.pchome.com.tw/prod/DAAG0S-A9009TO6H'

option = webdriver.ChromeOptions()
#option.add_argument('headless')
option.add_argument("--lang=en")
option.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=option,executable_path='./chromedriver.exe')

## login
login_url = 'https://shopping.pchome.com.tw/'
driver.get(login_url)
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//li[@id="h_coupon"]/a'))
)
button_buy = driver.find_element_by_xpath('//li[@id="h_coupon"]/a').click()


element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "loginAcc"))
)
driver.find_element_by_id("loginAcc").send_keys(username)
time.sleep(1)
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "loginPwd"))
)
driver.find_element_by_id("loginPwd").send_keys(password)
time.sleep(1)
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//dd/a'))
)
button_buy = driver.find_element_by_xpath('//dd/a').click()
#time.sleep(5)

## Confirm login
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "c2f"))
)


driver.get(url)
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//li[@id="ButtonContainer"]/button'))
)
button_buy = driver.find_element_by_xpath('//li[@id="ButtonContainer"]/button')
#記得先登入，否則會有問題
button_buy.click()
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "check"))
)

## Check out
button_check = driver.find_element_by_class_name("check").click()


## ATM 
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "ATM"))
)
time.sleep(1)
button_CC = driver.find_element_by_class_name("ATM").click()

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "warning_btn_confirm"))
)
driver.find_element_by_id("warning_btn_confirm").click()

## Address Page
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "BuyerMobile"))
)
time.sleep(1)
driver.find_element_by_id("BuyerMobile").send_keys(mobile)
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "invoice_item"))
)
driver.find_element_by_class_name("invoice_item").click()
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "chk_agree"))
)
driver.find_element_by_id("chk_agree").click()
#driver.find_element_by_id("btnSubmit").click()

#    driver.quit()

    


