from scrapy.contrib.spiders import CrawlSpider,Rule
# from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector
from baidutt.items import BaiduttItem
# from scrapy.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.contrib.linkextractors import LinkExtractor


class tiebaSpider(CrawlSpider):
    name = "tieba"
    allowed_domains=["baidu.com"]
    start_urls =["http://tieba.baidu.com/p/5051125142"]
    rules = [
        Rule(LinkExtractor(allow=("/5051125142\?pn=(\d)")), follow=True, callback='parse_cont'),
    ]
    def parse11(self,response):
        pass

    def parse_cont(self,response):
        items=[]
        select = Selector(response)
        text = select.css('div.l_post.j_l_post.l_post_bright')
        # authors = select.css('div.d_author')
        # contents = select.css('div.d_post_content_main')
        for list in text:
            item=BaiduttItem()
            item['name']=list.css('.d_author ul li.d_name a').xpath('text()').extract()
            item['content'] = list.css('.d_post_content_main cc div').xpath('text()').extract()
            items.append(item)
        return items
        # for uu in authors:
        #     item = BaiduttItem()
        #     item['name']=uu.css('.d_name a').xpath('text()').extract()
        #
        #
        #     for cc in contents:
        #         item = BaiduttItem()
        #         item['content']=cc.css('.p_content cc div').xpath('text()').extract()
        #         items.append(item)
        # return items
    # def _process_request(self,request):
    #     return request


#        print urlsnum.xpath('./li/li/span[2]').xpath('text()').extract()
