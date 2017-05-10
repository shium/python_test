# -*- coding: utf-8 -*-
import scrapy
from ..items import BookItem
import re

class DoubanBookSpider(scrapy.Spider):
    name = "doubanbook"
    allowed_domains = ['book.douban.com']
    start_urls = ['https://book.douban.com/top250']
    
    def parse_info(self, response):
        book_info = BookItem()
        book_info['name']   = response.xpath("//div[@id='wrapper']/h1/span/text()").extract()
        book_info['author'] = response.xpath("//div[@id='info']/a/text()").extract()
        book_info['score']  = response.xpath("//strong/text()").extract()
        book_info['content']= response.xpath("//div[@class='indent']//div[@class='intro']/p/text()").extract()
        author = book_info['author'][0]
        book_info['author'] = re.sub("\s", "", author)
        return book_info
        
    def parse_page(self, response):
        book_links = response.xpath("//tr[@class='item']/td[@valign='top']/div/a/@href").extract()
        for i in book_links:
            yield scrapy.Request(i, callback=self.parse_info)
            
    def parse(self, response):
        url_hosts = ['https://book.douban.com/top250?start=0']
        num_page = response.xpath("//div[@class='article']/div/div//a[last()]/text()").extract()
        for i in range(1, int(num_page[0])):
            urls = "https://book.douban.com/top250?start=" + str(i * 25)
            url_hosts.append(urls)

        for i in url_hosts:
            yield scrapy.Request(i, callback=self.parse_page)