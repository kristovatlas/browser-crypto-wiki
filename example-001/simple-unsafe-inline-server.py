#!/usr/bin/env python2
#http://stackoverflow.com/questions/21956683/python-enable-access-control-on-simple-http-server#21957017
from SimpleHTTPServer import SimpleHTTPRequestHandler
import BaseHTTPServer

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Content-Security-Policy', "script-src 'self' 'unsafe-inline';")
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    BaseHTTPServer.test(CORSRequestHandler, BaseHTTPServer.HTTPServer)
