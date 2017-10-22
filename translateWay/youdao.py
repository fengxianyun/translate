# coding: utf-8
'''
Created on 2017年10月22日

@author: raytine
'''
from selenium import webdriver
import time

def translate(message):
    chrome_login=webdriver.Chrome('../chromedriver.exe')
    chrome_login.get('http://fanyi.baidu.com/translate')
    time.sleep(1)
    # chrome_login.maximize_window()
    chrome_login.find_element_by_id('baidu_translate_input').clear()
    chrome_login.find_element_by_id('baidu_translate_input').send_keys(message)
    time.sleep(5)
    res = chrome_login.find_elements_by_css_selector('.target-output')
    result = []
    for i in res:
        result.append(i.text)
    return result