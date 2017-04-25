#-*-coding:utf8-*-
import pymongo

connection = pymongo.MongoClient()
tdb = connection.SPIDER
post_info = tdb.test

jike = {'name':u'极客','age':'5','skill':'python'}
post_info.insert(jike)

print u'完成'