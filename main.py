# -*- coding: utf-8 -*-
"""
Created on 2021/5/24 15:07
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import threading

from puppeteer import get_cookies
import requests
from bs4 import BeautifulSoup

from purify import purify_html
from load_pure_page import load_page
from http_server import start_http_server

SESSION = requests.session()


SESSION.headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "qikan.cqvip.com",
    "Origin": "http://qikan.cqvip.com",
    "Pragma": "no-cache",
    "Referer": "http://qikan.cqvip.com/Qikan/Search/Advance?from=index",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

def fetch_index_page(cookies):
    """
    访问搜索主页
    :return:
    """
    SESSION.headers['Cookie'] = cookies
    # SESSION.headers = {
    #     "Host": "qikan.cqvip.com",
    #     "Connection": "keep-alive",
    #     "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    #     "sec-ch-ua-mobile": "?0",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #     "Cookie": cookies,
    #     "Sec-Fetch-Site": "none",
    #     "Sec-Fetch-Mode": "navigate",
    #     "Sec-Fetch-User": "?1",
    #     "Sec-Fetch-Dest": "document",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    # }
    resp = SESSION.get("http://qikan.cqvip.com/Qikan/Search/Advance?from=index")
    return resp.text


def search_request(url, cookies):
    SESSION.headers['Cookie'] = cookies

    # SESSION.headers = {
    #     "Accept": "text/html, */*; q=0.01",
    #     "Accept-Encoding": "gzip, deflate, br",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     "Cache-Control": "no-cache",
    #     "Connection": "keep-alive",
    #     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #     "Cookie": cookies,
    #     "Host": "qikan.cqvip.com",
    #     "Origin": "http://qikan.cqvip.com",
    #     "Pragma": "no-cache",
    #     "Referer": "http://qikan.cqvip.com/Qikan/Search/Advance?from=index",
    #     "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    #     "sec-ch-ua-mobile": "?0",
    #     "Sec-Fetch-Dest": "empty",
    #     "Sec-Fetch-Mode": "cors",
    #     "Sec-Fetch-Site": "same-origin",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    #     "X-Requested-With": "XMLHttpRequest",
    # }
    payload = "searchParamModel=%7B%22ObjectType%22%3A1%2C%22SearchKeyList%22%3A%5B%7B%22FieldIdentifier%22%3A%22M%22%2C%22SearchKey%22%3A%22%E5%8C%97%E5%A4%A7%22%2C%22PreLogicalOperator%22%3A%22%22%2C%22IsExact%22%3A%220%22%7D%5D%2C%22SearchExpression%22%3A%22%22%2C%22BeginYear%22%3A%22%22%2C%22EndYear%22%3A%22%22%2C%22JournalRange%22%3A%22%22%2C%22DomainRange%22%3A%22%22%2C%22PageSize%22%3A%220%22%2C%22PageNum%22%3A%221%22%2C%22Sort%22%3A%220%22%2C%22ClusterFilter%22%3A%22%22%2C%22SType%22%3A%22%22%2C%22StrIds%22%3A%22%22%2C%22UpdateTimeType%22%3A%22%22%2C%22ClusterUseType%22%3A%22Article%22%2C%22IsNoteHistory%22%3A1%2C%22AdvShowTitle%22%3A%22%E9%A2%98%E5%90%8D%E6%88%96%E5%85%B3%E9%94%AE%E8%AF%8D%3D%E5%8C%97%E5%A4%A7%22%2C%22ObjectId%22%3A%22%22%2C%22ObjectSearchType%22%3A%220%22%2C%22ChineseEnglishExtend%22%3A%220%22%2C%22SynonymExtend%22%3A%220%22%2C%22ShowTotalCount%22%3A%220%22%2C%22AdvTabGuid%22%3A%224361c899-1a1a-2b2b-eefe-cf94a80612f7%22%7D"
    resp = SESSION.request(
        "POST",
        "http://qikan.cqvip.com/Search/SearchList{}".format(url),
        data=payload
    )
    return resp


def main():
    # 开一个web服务
    t = threading.Thread(target=start_http_server)
    # 设置为守护线程，主线程结束时，子线程也一起去死 <_<
    t.daemon = True
    t.start()
    # 获取cookie(仅用于第一次访问主页)
    data = get_cookies()
    cookies = "GW1gelwM5YZuS={}; GW1gelwM5YZuT={}".format(data['s'], data['t'])
    print("用于访问搜索页面的cookie: \r\n", cookies)
    
    # 请求主页链接，获得源码
    text = fetch_index_page(cookies)
    with open('./raw.html', 'w', encoding='utf-8') as f:
        f.write(text)
    
    # 处理html源码
    purify_html()
    
    # 让浏览器加载处理后的HTML文件， 并获取签名和cookie
    url, t_cookie = load_page()
    cookies = "GW1gelwM5YZuS={}; GW1gelwM5YZuT={}".format(data['s'], t_cookie)
    print("用于接口搜索的cookie: \r\n", cookies)
    search_response = search_request(url, cookies)
    try:
        # 简单提取点数据，表示请求成功
        soup = BeautifulSoup(search_response.text, 'lxml')
        result = soup.find('div', {'class': 'layui-col-xs6 search-result'}).get_text()
        print(result)
    except AttributeError:
        print("获取数据失败")

if __name__ == '__main__':
    main()
