from myspider.items import MyspiderItem

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from multiprocessing.dummy import Pool

class nouSpider(CrawlSpider):
    name = 'novspider'
    allow_domains = ["daomubiji.com"]
    start_urls = ["http://www.daomubiji.com"]

    def parse(self,response):

        select = Selector(response)
        aa = select.xpath('//article')
        for each in aa.xpath('.//a'):
            urls = each.xpath('@href').extract()
            # print urls
            for url in urls:
                print url
                yield Request(url, callback=self.parse_item)

    def parse_item(self,response):
        items = []
        content = Selector(response)
        list1 = content.css('article.excerpt.excerpt-c3')
        # title = content.css('div.container')

        for each in list1:
            item = MyspiderItem()
            item['bookName'] = content.xpath('//head/title/text()').extract()
            item['chapterUrl'] = each.xpath('a/@href').extract()
            # cont = i.css('.a').xpath('text()').extract()
            # uurl = i.css('.a').xpath('@href').extract()
            text = each.css('a::text').extract()
            for i in text:
                try:
                    item['bookTitle'] = i.split(' ')[0]
                    item['chapterNum'] = i.split(' ')[1]
                except Exception,e:
                    continue

                try:
                    item['chapterName'] = i.split(' ')[2]
                except Exception,e:
                    item['chapterName'] = i.split(' ')[1][-3:]
                items.append(item)
        return items
            # yield item



