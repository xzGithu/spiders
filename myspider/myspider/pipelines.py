# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import json
import codecs
# from scrapy import items
# from scrapy.conf import settings
class MyspiderPipeline(object):

    def __init__(self):
        host = '127.0.0.1'
        port = 27017
        dbName = 'SPIDER'
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[dbName]
        self.post = tdb['novel']
        # self.file = codecs.open('item.jl', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        bookInfo = dict(item)
        self.post.insert(bookInfo)
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(line)
        return item


class spiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('item.jl','w',encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.file.write(line)
        return item
