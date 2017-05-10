# -*- coding: utf-8 -*-
import scrapy
from ..items import DoubanbookItem
import urllib2
import sys
from lxml import etree
import re

reload(sys)
sys.setdefaultencoding( "utf-8" )

class douban_book_spider(scrapy.Spider):
    name = 'doubanbook'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/?icn=index-nav']
    
    def parse(self, response):
        book_classify_link = response.xpath('//table[@class="tagCol"]/tbody/tr/td/a/@href').extract()
        for i in book_classify_link:
            url = 'https://book.douban.com' + i
            yield scrapy.Request(url, meta={'url': url}, callback = self.parse_page)
           
    def parse_page(self, response):
        #book_info = DoubanbookItem()
        url = response.meta['url']
        last_page = response.xpath('//div[@id="subject_list"]/div[@class="paginator"]/a[last()]/text()').extract()
        for i in range(int(last_page[0])):
            next_page_url = url + '?start=' +str(i*20) + '&type=T'
#            next_page_url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=1960&type=T'
            selector = open_page(next_page_url)
            print 'open next url'
            books_link = selector.xpath('//div[@id="subject_list"]/ul/li/div[@class="info"]/h2/a/@href')
            print books_link
            if books_link != []:
                for j in books_link:
                    print j
                    book_info = DoubanbookItem()
                    info_page = open_page(j)
                    name   = info_page.xpath('//div[@id = "wrapper"]/h1/span/text()')
                    author = info_page.xpath('//div[@class="subject clearfix"]/div[@id="info"]/a/text()')
                    rating = info_page.xpath('//div[@id="interest_sectl"]/div/div/strong/text()')
                    ISBN   = info_page.xpath('//div[@class="subject clearfix"]/div[@id="info"]/text()[last()-1]')
                    author = re.sub("\s", "", author[0])
                    ISBN   = re.sub("\s", "", ISBN[0])
                    if author ==[]:
                        author[0] == NULL

                    book_info['name']   = name[0]
                    book_info['author'] = author
                    book_info['rating'] = float(rating[0])
                    book_info['ISBN']   = ISBN
                    print book_info

                    yield book_info
            else:
                print 'continue'
                continue

def open_page(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent, "Accept-Language": "zh-cn"}
    try:
        req = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(req)
        html = response.read()
    except:
        print "get "+url+" error!"

    selector = etree.HTML(html, parser = None, base_url = None)
    return selector
