# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from jd.items import *
import pymongo
import json

class JdPipeline(object):
    def __init__(self):
        host='127.0.0.1'
        port=27017
        dbname='JD1'
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbname]
        self.post = tdb['phone']
    def process_item(self, item, spider):
        phoneinfo = dict(item)
        self.post.insert(phoneinfo)
        return item
