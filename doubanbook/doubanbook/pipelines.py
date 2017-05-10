# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import MySQLdb
import json
import codecs

class DoubanbookPipeline(object):
    def __init__(self):
        self.file = codecs.open('doubanbook.json', 'w', encoding = 'utf-8')
    
    def process_item(self, item, spider):
        print 'process_item'
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
        
    def spider_closed(self, spider):
        self.file.close()
'''
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "200201", "doubanbook", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        print 'mysql'

        sql = 'INSERT INTO book_info(id, name, author,rating) VALUES (%s,%s,%s,%s)'
        self.cursor.execute(sql,(item['ISBN'],'name','author',item['rating']))
        self.db.close()
        print 'done'
        return item
    def _handle_error(self, failue, item, spider):
        print failue
'''
