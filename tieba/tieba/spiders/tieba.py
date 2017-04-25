
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector
from items import TiebaItem



class tiebaSpider(CrawlSpider):
    name = "tieba"
    start_urls ="http://tieba.baidu.com/p/5034839578"
    rules = [Rule(LinkExtractor(allow=("/p/5034839578\?pn=\d{,4}")),follow=True,callback='parse')]

    def parse(self,response):
        items=[]
        select = Selector(response)
        authors = select.css('div.d_author')
        contents = select.css('div.d_post_content_main')
        for uu in authors:
            item = TiebaItem()
            item['name']=uu.css('.d_name a').xpath('text()').extract()
            items.append(item)

        for cc in contents:
            item = TiebaItem()
            item['content']=cc.css('.p_content cc div').xpath('text()').extract()
            items.append(item)
        return items


#        print urlsnum.xpath('./li/li/span[2]').xpath('text()').extract()



