# Coding:utf-8

import http.server
import socketserver
from urllib.error import HTTPError
import urllib


port = 80
adress = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adress, handler)

print(f"Server is started in the PORT {port}")

print("Go in your navigator and go this is link : localhost/")

httpd.serve_forever()


