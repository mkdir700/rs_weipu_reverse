# -*- coding: utf-8 -*-
"""
Created on 2021/5/26 9:39
---------
@summary: 加载处理后的html页面
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import asyncio
import os

from pyppeteer import launch
from pyppeteer_stealth import stealth


async def close_page(browser):
    await browser.close()


async def start():
    browser = await launch(
        {
            'headless': False,
            'userDataDir': './userDataDir',
            'args': [
                '--no-sandbox',
            ]
        }
    )
    page = await browser.newPage()
    await page.setViewport(viewport={'width': 1000, 'height': 800})
    await stealth(page)
    await page.goto('http://localhost:9000/pure.html')
    url = await page.evaluate("() => {searchList(); return genUrl;}")
    cookies = await page.cookies()
    await browser.close()
    return url, cookies


def load_page():
    url, cookies = asyncio.get_event_loop().run_until_complete(start())
    t_cookie = None
    for cookie in cookies:
        if cookie['name'] == 'GW1gelwM5YZuT':
            t_cookie = cookie['value']
    return url, t_cookie
    

if __name__ == '__main__':
    print(load_page())
