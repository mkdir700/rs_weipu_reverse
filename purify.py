# -*- coding: utf-8 -*-
"""
Created on 2021/5/24 17:15
---------
@summary: 注入代码
1. 去除定时无限debugger
2. 去除死循环debugger
3. 插入searchList方法,用于生成签名
4. 将得到的签名提升至全局变量,可通过 `genUrl` 访问
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import re


def purify_html():
    with open("raw.html", encoding="utf-8") as f:
        text = f.read()
    
    r = re.findall("_\$[\w\d\$]{2}\(79,_\$[\w\d\$]+\);", text)[0]
    var_name = re.findall("_\$[\w\d\$]{2}\(79,(_\$[\w\d\$]+)\);", r)[0]
    
    pp = """%(var_name)s = %(var_name)s.replace(/(_\$[\w\d\$]+)\+=_\$[\w\d\$]+\[5\]\+(_\$[\w\d\$]+\([^)]+\);)/gm, `$1="?"+$2window.genUrl=$1;`);%(var_name)s = %(var_name)s.replace(/(<389\){)[^}]+/gm, `$1`);%(var_name)s = %(var_name)s.replace("debugger", "");""" % {
        'var_name': var_name}
    
    result = text.replace(r, pp + r)
    result = result.replace("/NJDrTcXo8msX/leE4DkIasHMb.f22c526.js",
                            "http://qikan.cqvip.com/NJDrTcXo8msX/leE4DkIasHMb.f22c526.js")
    result = re.sub(r"(/dist)", "http://qikan.cqvip.com/dist", result)
    result = re.sub(r'https://hm.baidu.com/hm.js[^"]+', '', result)
    result = result.replace("</body>",
                            '<script>searchList=function(a){$.ajax({url:"/Search/SearchList",type:"post",dataType:"html",data:{searchParamModel:a},beforeSend:function(){loadding()},complete:function(){loaddingClose()},success:function(){console.log("请求成功")},error:function(){loaddingClose()}})};</script></body>')
    # print(result)
    
    with open('pure.html', "w", encoding="utf-8") as f:
        f.write(result)
    
    print("HTML页面代码注入完成")


if __name__ == '__main__':
    purify_html()