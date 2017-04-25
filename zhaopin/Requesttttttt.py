#-*- coding:utf8 -*-
import requests
import re
# import sys
# reload(sys)
# sys.setdefaultencoding("gb18030")
# type = sys.getfilesystemencoding()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0'}
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/',headers = headers)
html.encoding='utf-8'
#print html.text

title = re.findall('"color:#666666;">(.*?)</span>',html.text,re.S)
for each in title:
    print each

chinese = re.findall('"color: #039;">(.*?)</a>',html.text,re.S)
for each in chinese:
    print each






