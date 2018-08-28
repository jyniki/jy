# -*- coding: utf-8 -*-

import requests
from selenium import webdriver
from time import sleep
profile=webdriver.FirefoxProfile()
profile.set_preference('browser.download.dir', '/Users/jiangyu/Desktop/tianchi/downloads/')
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
driver = webdriver.Firefox(firefox_profile=profile)
driver.get('http://jupter-oss.oss-cn-hangzhou.aliyuncs.com/file/opensearch/documents/110/SRAD2018_TRAIN_034.zip?Expires=1535465357&OSSAccessKeyId=unrUSZdy4TBoR9Kz&Signature=VeuP7O8zMM2QmGmUWF6V4mP1KdA%3D&response-content-disposition=attachment%3B%20')
driver.find_element_by_xpath('//a[text()="testsaveas.zip"]').click()
sleep(3)
driver.quit
