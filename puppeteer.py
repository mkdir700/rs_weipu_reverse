# -*- coding: utf-8 -*-
"""
Created on 2021/5/25 19:22
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import asyncio
import os
import time

from pyppeteer import launch
from pyppeteer_stealth import stealth


async def close_page(browser):
    await browser.close()


async def start():
    # 插件文件夹路径
    chrome_extension = os.path.join(os.path.abspath('./'), 'inject')
    browser = await launch(
        {
            'headless': False,
            'userDataDir': './userDataDir',
            'args': [
                '--no-sandbox',
                '--load-extension={}'.format(chrome_extension),
                '--disable-extensions-except={}'.format(chrome_extension),
                '--window-size=0,0'
            ]
        }
    )
    page = await browser.newPage()
    await page.setViewport(viewport={'width': 1000, 'height': 800})
    await stealth(page)
    await page.goto("http://qikan.cqvip.com/Qikan/Search/Advance?from=index")
    
    time.sleep(0.5)
    t = await page.evaluate("() => {return t_cookie;}")
    cookies = await page.cookies()
    s = None
    for c in cookies:
        if "GW1gelwM5YZuS" == c['name']:
            s = c['value']
    data = {'s': s, 't': t}
    # print(data)
    await browser.close()
    return data


def get_cookies():
    data = asyncio.get_event_loop().run_until_complete(start())
    return data

if __name__ == '__main__':
    print(get_cookies())
