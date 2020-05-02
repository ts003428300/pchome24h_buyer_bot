# -*- coding: utf-8 -*-
"""
Created on Sat May  2 21:16:24 2020

@author: Nick
"""

from selenium import webdriver
import requests
import time
import sys

option = webdriver.ChromeOptions()
#option.add_argument('headless')
option.add_argument("--lang=en")
option.add_argument("--no-sandbox")
driver = webdriver.Chrome(chrome_options=option,executable_path='./chromedriver.exe')


url = 'https://24h.pchome.com.tw/prod/DMBF0L-1900ALY1D'

driver.get(url)

button_buy = driver.find_element_by_xpath('//li[@id="ButtonContainer"]/button')
#記得先登入，否則會有問題
button_buy.click()

button_check = driver.find_element_by_class_name("check")


button_check.click()

#button_CC = driver.find_element_by_class_name("CC")
#
#button_CC.click()