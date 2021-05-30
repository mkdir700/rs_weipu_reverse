# -*- coding: utf-8 -*-
"""
Created on 2021/5/25 15:25
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import requests

session = requests.session()
s = input("请输入GW1gelwM5YZuS的值:\r\n")
value = input("请输入GW1gelwM5YZuT的值:\r\n")
session.headers = {
    "Host": "qikan.cqvip.com",
    "Connection": "keep-alive",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    "sec-ch-ua-mobile": "?0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Cookie": "GW1gelwM5YZuS={}; GW1gelwM5YZuT={}".format(s, value),
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
resp = session.get("http://qikan.cqvip.com/Qikan/Search/Advance?from=index")
# print(resp.text)
# print(resp.request.headers)
print(resp.status_code)
