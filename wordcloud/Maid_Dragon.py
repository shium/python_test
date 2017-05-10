# -*- coding: utf-8 -*-
import urllib2
import gzip
import zlib
import re
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

def downhtml(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent, "Accept-Language": "zh-cn", 'Connection':'keep-alive','Accept-Encoding': 'gzip,deflate'}
    try:
        req = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(req)
        #print response.info().get('Content-Encoding')
        html = response.read()
        content = deflate(html)
        #print content
    except:
        print "get "+url+" error!"
    '''
    f = open("index.html", "w")
    f.write(content)
    f.close()
    '''
    return content
    
def deflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)
    
def findcomment(data):
    pattern = '\">(.*?)</d>'
    text = re.findall(pattern, data)
    f = open("index.txt", "a")
    for r in text:  
        f.write(r.decode("utf8") + "\n")
    f.close()

url = 'http://comment.bilibili.com/rc/15412094.xml'
content = downhtml(url) 
#print repr(content)
findcomment(content)