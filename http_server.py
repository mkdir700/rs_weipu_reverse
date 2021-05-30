# -*- coding: utf-8 -*-
"""
Created on 2021/5/27 14:19
---------
@summary: 
---------
@author: mkdir700
@email:  mkdir700@gmail.com
"""
import http.server
import socketserver


def start_http_server():
    PORT = 9000
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()