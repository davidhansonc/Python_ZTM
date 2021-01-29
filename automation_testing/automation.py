# -*- coding: utf-8 -*-
# @Author: davidhansonc
# @Date:   2021-01-13 13:43:48
# @Last Modified by:   davidhansonc
# @Last Modified time: 2021-01-13 16:24:46
from selenium import webdriver

chrome_browser = webdriver.Chrome()

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_css_selector('#get-input > .btn.btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_css_selector('#user-message')
user_message.clear()
user_message.send_keys('hello!')

show_message_button.click()

chrome_browser.quit()