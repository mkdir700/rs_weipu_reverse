# -*- coding: utf-8 -*-
"""
Created on 2021/5/26 12:49
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Remote(command_executor='http://192.168.20.222:49153/wd/hub',desired_capabilities={'browserName': 'firefox'})
# driver.get('https://qikan.cqvip.com/Qikan/Search/Advance?from=index/')
driver.get('https://baidu.com')
print(driver.get_cookies())
# time.sleep(10)
print(driver.page_source)
driver.close()

# import asyncio
# import pyppeteer
#
# async def demo():
#     await pyppeteer.connect({'browserWSEndpoint': 'ws://localhost:3000'})
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(demo())
