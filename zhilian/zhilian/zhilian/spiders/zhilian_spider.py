import re
import json
from scrapy.selector import Selector
from scrapy.spider import Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from zhilian.items import *

class ZhiLianSpider(CrawlSpider):
    name = 'zhilian'
    allowed_domains = ["jobs.zhaopin.com"]
    start_urls = ["http://jobs.zhaopin.com/beijing"]
    rules = [
        Rule(SgmlLinkExtractor(allow=("/beijing/p\d{,2}}")),follow=True,callback='parse')
    ]
    def parse(self,response):
        items=[]
        sel = Selector(response)
        base_url = get_base_url(response)
        list1 =sel.css('div.details_container')
        for lis in list1:
            item = ZhilianItem()
            item['name'] = lis.css('.post a').xpath('text()').extract()
            item['company'] = lis.css('.company_name a').xpath('text()').extract()
            item['salay'] = lis.css('.salary::text').extract()
            item['time'] = lis.css('.release_time::text').extract()
            item['fankui'] = lis.css('.address::text').extract()
            item['link'] = lis.css( '.company_name a').xpath('@href').extract()
            items.append(item)
        return items



