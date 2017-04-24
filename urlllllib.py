#-*-coding:utf8 -*-
import urllib
import urllib2
import cookielib
import re
import socket
import time

# url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
# headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"}
#
# req = urllib2.Request(url,headers=headers)
# # req.add_header(headers)
# response = urllib2.urlopen(req)
# # text = urllib2.urlopen(req)text.read()
# print response.read()

# url = 'http://www.iqianyue.com/mypost/'
# headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"}
# data = {'name':'ceo@iqianyue.com','pass':'aA123456'}
# cookie = cookielib.CookieJar()
# proc = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(proc)
# response1 = opener.open('http://www.baidu.com')
# for item in cookie:
#     print item.name
#     print item.value
# data = urllib.urlencode(data)
# request = urllib2.Request(url,data,headers=headers)
# response = urllib2.urlopen(request)
# print response.read()
#
#
# try:
#     urllib2.urlopen('http://blog.csdn.ne')
# except urllib2.URLError as e:
#     print e.reason
#
#
# url = 'https://passport.jd.com/new/login.aspx'
# urls = 'http://passport.jd.com/uc/loginService'
# files = urllib2.Request(url)
# response = urllib2.urlopen(files)
# data = response.read()
# # print   data
# # filename = 'cookie.txt'
# # cookie = cookielib.MozillaCookieJar(filename)
# # handler = urllib2.HTTPCookieProcessor(cookie)
# # opener = urllib2.build_opener(handler)
# reg = re.compile(r'<input type="hidden" id="uuid" name="uuid" value="(.*?)"/>')
# tt=reg.findall(data)
# # print tt
# headers = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"}
#
# data = {'nloginpwd':'jdsc_xz',
#         'loginname':'Xuzhe@1990',
#         'uuid':tt}
# datas = urllib.urlencode(data)
# # result = opener.open(urls,datas)
# # print result.read()
# # cookie.save(ignore_discard=True,ignore_expires=True)
# listurl = 'https://order.jd.com/center/list.action'
# # reqq = opener.open(listurl)
# req = urllib2.Request(urls,datas,headers=headers)
# response = urllib2.urlopen(req)
# print response.read()
#
# print u'\u8bf7\u60a8\u542f\u7528\u6d4f\u89c8\u5668Cookie\u529f\u80fd\u6216\u66f4\u6362\u6d4f\u89c8\u5668\u3002'


def Navigate(url,data={}):           #定义连接函数，有超时重连功能
    tryTimes = 0
    while True:
        if (tryTimes>20):
            print "多次尝试仍无法链接网络，程序终止"
            break
        try:
            if (data=={}):
                req = opener.open(url)
                # req = urllib2.Request(url)

            else:
                req = opener.open(url, urllib.urlencode(data))
                # req = urllib2.Request(url,urllib.urlencode(data))
            cookie.save(ignore_expires=True,ignore_discard=True)
            # req = urllib2.urlopen(req).read()
            req = req.read()
            tryTimes = tryTimes +1
        except socket.error:
            print "连接失败，尝试重新连接"
        else:
            break
    return req
try:
    filename = '11.txt'
    # cookie = cookielib.CookieJar()
    cookie = cookielib.MozillaCookieJar(filename)
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
except:
    raise
else:
     opener = urllib2.build_opener(cookieProc)
     opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
     urllib2.install_opener(opener)
url = 'https://passport.jd.com/uc/login'
login = Navigate(url)
reg = re.compile(r'<input type="hidden" id="uuid" name="uuid" value="(.*?)"/>')
regt = re.compile(r'<input type="hidden" name="_t" id="token" value="(.*?)" class="hide"/>')
regsa = re.compile(r'input type="hidden" id="sa_token" name="sa_token" value="(.*?)"/>')
regpub = re.compile(r'<input type="hidden" name="pubKey" id="pubKey" value="(.*?)" class="hide"/>')



# <input type="hidden" name="_t" id="token" value="_ntwiLZX" class="hide"/>
tt=reg.findall(login)[0]
ttt = regt.findall(login)[0]
sag = regsa.findall(login)
pub = regpub.findall(login)
print tt
print ttt
codeurl = "http://authcode.jd.com/verify/image?a=1&acid="+str(tt)+"&uid="+str(tt)#+"&yys="+str(int(time.time()*1000))
# res = urllib2.Request(codeurl)
# content = urllib2.urlopen(res)
# data1 = content.read()
# txt = open('D:\\WORK\\my-python-project\\1.html','wb')
# txt.write(data1)
# txt.close()
print codeurl
urls = 'http://passport.jd.com/uc/loginService'#?uuid='+str(tt)
print urls
code = raw_input('input code:')
data = {'nloginpwd':'Xuzhe@1990',
        # 'loginpwd':'Xuzhe@1990',
        'loginname':'jdsc_xz',
        'uuid':tt,
        '_t':ttt,
        'authcode':code,
        # 'pubKey':pub,
        # 'sa_token':sag,
        }
# head = {"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"}

# data = urllib.urlencode(data)
passport = Navigate(urls,data)
print passport
print u"\u8bf7\u5237\u65b0\u9875\u9762\u540e\u91cd\u65b0\u63d0\u4ea4"
print u"\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801"
print u"\u9a8c\u8bc1\u7801\u4e0d\u6b63\u786e\u6216\u9a8c\u8bc1\u7801\u5df2\u8fc7\u671f"

listurl = 'https://order.jd.com/center/list.action'

request = opener.open(listurl)

print request.read()