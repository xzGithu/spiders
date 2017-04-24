#-*-coding:utf8-*-
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request,FormRequest,HtmlResponse

import urllib2
import re

class jdspiders(CrawlSpider):

    name = "jdsp"
    allowed_domain = ["jd.com"]
    start_urls =["https://order.jd.com/center/list.action"]
    headers = {	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}

    def start_requests(self):
        return [Request("https://passport.jd.com/uc/login",meta={'cookiejar':1},callback=self.post_login)]

    def post_login(self,response):
        print "logining"
        reg = re.compile(r'<input type="hidden" id="uuid" name="uuid" value="(.*?)"/>')
        regt = re.compile(r'<input type="hidden" name="_t" id="token" value="(.*?)" class="hide"/>')


        tt = reg.findall(response.body)[0]
        ttt = regt.findall(response.body)[0]
        codeurl = "http://authcode.jd.com/verify/image?a=1&acid=" + str(tt) + "&uid=" + str(tt)
        print codeurl

        code = raw_input('input code:')
        return [FormRequest.from_response(response,
                                          url='http://passport.jd.com/uc/loginService',
                                          meta = {'cookiejar':response.meta['cookiejar']},
                                          headers = self.headers,
                                          formdata={
                                            'nloginpwd': 'Xuzhe@1990',
                                            'loginname':'jdsc_xz',
                                            'uuid':tt,
                                            '_t':ttt,
                                            'authcode':code,

                                          },
                                          callback = self.after_login,
                                          dont_filter = True,
                                          # 'dont_redirect':True,
                                          )]
    def after_login(self,response):
        for u in self.start_urls:
            yield Request(u,meta={'cookiejar':response.meta['cookiejar']},callback=self.parse_de)
            url = response.url
            print url
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            print response.read()

        # print 'after loggin'
        # cookie = response.request.headers.getlist('Cookie')
        # print cookie
        # print response.body

    def parse_de(self, response):
        content = Selector(response)

        hxs = content.xpath('//title')
        print response.url
        print hxs.xpath('text()').extract()
        # print response.body
        print '****************'
        # if not "jdsc_xz" in response.body:
        #     print "login error"
        # else:
        #     print "success"
        # for url in self.start_urls:
        #     # yield self.make_requests_from_url(url,meta={'cookiejar': response.meta['cookiejar']})
        #     yield Request(url, meta={'cookiejar': response.meta['cookiejar']})

    # def parse_page(self, response):
    #     item=[]
    #     content = Selector(response)
    #     hxs = content.xpath('//title')
    #     # print response.body
    #     item['name'] = hxs.xpath('text()').extract()
    #     return item


