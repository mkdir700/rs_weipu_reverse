# -*- coding: utf-8 -*-
"""
Created on 2021/5/24 16:53
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


# driver = webdriver.Remote(command_executor='http://192.168.20.222:4444/wd/hub',desired_capabilities={'browserName': 'chrome'})
# driver.get('https://qikan.cqvip.com/Qikan/Search/Advance?from=index/')
# print(driver.get_cookies())
# time.sleep(10)
# print(driver.page_source)
# driver.close()


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
# chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# chrome_options.add_extension("./inject.crx")
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
# script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
# 运行 JavaScript 代码
# driver.execute_script(script)

# with open('./stealth.min.js', 'r', encoding='utf-8') as f:
#     js = f.read()
#
# driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": js
# })

cqvipurl = 'http://qikan.cqvip.com/Qikan/Search/Advance?from=index'
# cqvipurl = 'https://bot.sannysoft.com/'
driver.get(cqvipurl)

# firefox_options = webdriver.FirefoxOptions()
# profile = webdriver.FirefoxProfile("C:\\Users\\mkdir700\AppData\Roaming\Mozilla\Firefox\Profiles\8s3z5uun.default-release")
# driver = webdriver.Firefox(profile)

# 显示等待输入框是否加载完成
# WebDriverWait(driver, 1000).until(
#     EC.presence_of_all_elements_located(
#         (By.CLASS_NAME, 'advance-submit')
#     )
# )
# time.sleep(2)
# # 设置第一查询条件，第一查询条件为单位名称
# node = driver.find_element_by_name("advSearchKeywords")
# node.click()  # 点击第一个检索条件下拉框# 选择检索条件为机构暨单位
# node.send_keys("清华大学")
# time.sleep(1)
# driver.find_element_by_xpath(
#     "//div[@id='basic_searchdomainfilter']/div[@class='advance-submit']/button").click()  # 点击检索按钮
# #
# print(driver.page_source)
cookies = driver.get_cookies()
c = ""
for cookie in cookies:
    c += "{}={}; ".format(cookie['name'], cookie['value'])
print("="*60)
print(c)
print(driver.execute_script('return t_cookie;'))
