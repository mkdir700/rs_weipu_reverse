# -*- coding: utf-8 -*-
"""
Created on 2021/5/23 16:38
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import requests

payload = "searchParamModel=%7B%22ObjectType%22%3A1%2C%22SearchKeyList%22%3A%5B%7B%22FieldIdentifier%22%3A%22M%22%2C%22SearchKey%22%3A%22%E5%8C%97%E5%A4%A7%22%2C%22PreLogicalOperator%22%3A%22%22%2C%22IsExact%22%3A%220%22%7D%5D%2C%22SearchExpression%22%3A%22%22%2C%22BeginYear%22%3A%22%22%2C%22EndYear%22%3A%22%22%2C%22JournalRange%22%3A%22%22%2C%22DomainRange%22%3A%22%22%2C%22PageSize%22%3A%220%22%2C%22PageNum%22%3A%221%22%2C%22Sort%22%3A%220%22%2C%22ClusterFilter%22%3A%22%22%2C%22SType%22%3A%22%22%2C%22StrIds%22%3A%22%22%2C%22UpdateTimeType%22%3A%22%22%2C%22ClusterUseType%22%3A%22Article%22%2C%22IsNoteHistory%22%3A1%2C%22AdvShowTitle%22%3A%22%E9%A2%98%E5%90%8D%E6%88%96%E5%85%B3%E9%94%AE%E8%AF%8D%3D%E5%8C%97%E5%A4%A7%22%2C%22ObjectId%22%3A%22%22%2C%22ObjectSearchType%22%3A%220%22%2C%22ChineseEnglishExtend%22%3A%220%22%2C%22SynonymExtend%22%3A%220%22%2C%22ShowTotalCount%22%3A%220%22%2C%22AdvTabGuid%22%3A%224361c899-1a1a-2b2b-eefe-cf94a80612f7%22%7D"

# G5tA5iQ4 = "GW1gelwM5YZuT=53tnkdbc7fkZqqqmyLGO_jG6yd5M_o_OeNzMda2gdX1UVYqU7soR3uvGJN2FzkrlXCj4kvQ3y8bOCpu176YApi0n0YC0Dd_.VStzt7lK4K8DBx8JpfTiw_DmEpAOqGWyqf1I..FizJ47Thz.gCCUyNk92SAs2CAIXuTv5e__60_9PE327lvEvQ3f5s4XoJDogBLgaBDOWPwBZFsgCgmoEKFZNk68YVfBvZA26IY4_svsGhuXWvf3MLjY4ghZsoqu5j24GtH1khOTmWudwb7HHJaygDcEMiPL8TfPRtpIVRnKGNRphLsuXix15WNQJlTKNr067uJmKebSmxiN3WjRN6Q_ZB8eXZRNHH0GyFLU7PK7A; "
# coo = G5tA5iQ4+"GW1gelwM5YZuS=5EOPFwfvc3cqZqGi3iA.Q2zuYYlBue6AKWFbTncyeGBsMjkpEzfqngjAhw8_M7oMWdEM6kDz9yF2U1E1y2WAena"
coo = "GW1gelwM5YZuS=5T9tXKF_Y9y8.Z62eptZwN7dvqbUDCFloXZTOgZ6cFhbQR3k7JTSOU4Uz08VHoDsjoL4qcnbtAF5WtaGwRZiaZA; GW1gelwM5YZuT=53tCLADczzKaqqqmyN22oRqGV2esN7Lk2IjIL6InvsswK4JiU__fXiQjtj4iMlypIUrU0.KYQerENwQcw2vbI7xSlV3ePymprH5VRE4XuwB4W8AyoIRqET37pbHbY47e5JyRGq7fsc8c7XJeXXqpWf1Ss5r2PP_yswOK0gA3bnFhcxt_DdEgvUs5jbulj_OZ7hJeFOh1GjbGi42UWtGXac00rhMxIahwLmtD9wiWO2gHA"
session = requests.Session()

session.headers = {
    "Accept": "text/html, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    # "Content-Length": "948",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": coo,
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

# print("https://qikan.cqvip.com:443/Search/SearchList?{}".format(G5tA5iQ4))

resp = session.request(
    "POST",
    # "http://qikan.cqvip.com/Search/SearchList?{}".format(G5tA5iQ4),
    "http://qikan.cqvip.com/Search/SearchList?G5tA5iQ4=5_kAvPP2Ipfv8krqeFOToiPMg6mW8nBEzDbaq_2wk3VAGYi8i8dm7QhdOg5.Bz0Foj8G0eYvJ0rMqZfiXuSwbak90jTyvsZy_wswvOJ3kc1bshKQxTZofXhjN3NV.nSkLoEFC8Tgvrcabg5cZ7PlXCsunwQRjqgEx1gvVLnwzNUyffgcOWFc1bjvnlOp5xbTTqe2vWi1h0oJwzWEvLvOCkly0Sty_Fg6gT16O5cDdpt7wyr2W3Zt6kuxFN6szEVLoKi6pE2xoYjn2xruymb5VKerJoc1Ck7I2DboCYERMsk.d0.u0Ly.rjarVVa9iOE7zrRC1FSCYdquuRsfMfN1n95C0xwIXKUk5EphCgZebFmhRauCsVSrKlqs4IUi0zAeT",
    data=payload
)
# {"DebugMessage":"未将对象引用设置到对象的实例。","PromptMsg":"系统出现异常，请联系管理员","Result":0,"RetValue":null,"Tag":null}
print(resp.request.headers)
print(resp.request.body)
print(resp.status_code)
print(resp.text)
