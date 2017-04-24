#-*-coding:utf8-*-

from scrapy.selector import Selector

from scrapy.spiders import CrawlSpider
from JD.items import *
from scrapy.http import Request
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class jdspider(CrawlSpider):
    name = 'jdspider'
    allow_domains = ['jd.com']
    start_urls=[]
    for i in range(1,5):
        url = 'https://list.jd.com/list.html?cat=9987,653,655&page='+str(i)
        start_urls.append(url)
    # start_urls = ['https://list.jd.com/list.html?cat=9987,653,655&page=2']

    def parse(self,response):
        items=[]
        content = Selector(response)
        hxs = content.xpath('//li[@class="gl-item"]')
        for i in hxs:
            item = JdItem()
            item['shopname'] = i.xpath('div/div[7]/@data-shop_name').extract()
            item['phoneid'] = i.xpath('div/@data-sku').extract()
            item['goodname'] = i.xpath('div/div[4]/a/em/text()').extract()
            item['phoneurl'] = i.xpath('div/div[1]/a/@href').extract()
            # items.append(item)
            urls = "http://" + item['phoneurl'][0]
            item['phoneurl'] = urls
            yield Request(urls,meta={'item':item},callback=self.parse_detail)

    # def parse_detail(self,response):
    #     item=response.meta['item']
    #     sel=Selector(response)
    #     urls = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds=" + str(item['phoneid'][0])
    #     yield Request(urls,meta={'item':item},callback=self.parse_price)

    def parse_detail(self,response):
        item = response.meta['item']
        # a = response.body
        # jstsmp = json.loads(a,encoding="utf-8")
        # item['commentcount'] = jstsmp['CommentsCount'][0]['GoodRate']
        # return item
        ids = item['phoneid']
        sids = str(ids)
        print sids
        urls = "http://p.3.cn/prices/mgets?skuIds=J_" + sids[3:-2]
        yield Request(urls,meta={'item':item},callback=self.parse_price)

    def parse_price(self,response):
        item = response.meta['item']
        a=response.body
        temp = a.split('[')
        print temp[1][:-2]
        js = json.loads(temp[1][:-2])
        item['price'] = js['p']
        return item


        # return items

    #         phoneurls = 'http://'+item['phoneurl']
    #         urls = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds="+str(item['phoneid'])
    #         # yield scrapy.Request(phoneurls,meta={'item':item},callback=self.parse_phone)
    #         yield scrapy.Request(urls, meta={'item': item}, callback=self.parse_comment)
    #
    # def parse_comment(self,response):
    #     item = response.meta['item']
    #     js = json.loads(str(response.body))
    #     item['commentcount'] = js['CommentsCount'][0]['CommentCount']
    #     return item



