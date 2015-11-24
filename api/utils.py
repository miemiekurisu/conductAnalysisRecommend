#-*-encoding:utf-8-*-
'''
Created on 2015年11月24日

@author: chris
'''
import urllib
import urllib2
import json
import socks
from setting import socksproxy
from sockshandler import SocksiPyHandler

def post(queryUrl,param,timeout=60):
    if socksproxy:
        proxyon = SocksiPyHandler(socks.SOCKS5, "127.0.0.1", 1080)
        opener = urllib2.build_opener(proxyon)
    else:
        opener = urllib2.build_opener()
    postdata = urllib.urlencode(param)
    response = opener.open(queryUrl, postdata,timeout)
    data = response.read()
    opener.close()
    return json.loads(data.decode('utf-8'))