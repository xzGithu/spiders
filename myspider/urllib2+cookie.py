#-*-coding:utf8-*-
# import urllib2
# import cookielib
#
# cookie = cookielib.CookieJar()
#
# handler = urllib2.HTTPCookieProcessor(cookie)
#
# opener = urllib2.build_opener(handler)
#
# response = opener.open('http://www.baidu.com')
#
# for item in cookie:
#     print item.name
#     print item.value


#
# import urllib2
# import cookielib
# import urllib
#
# filename = '1.txt'
# cookie = cookielib.MozillaCookieJar(filename)
# handler = urllib2.HTTPCookieProcessor(cookie)
# opener = urllib2.build_opener(handler)
# postdata = urllib.urlencode({'loginname':'jdsc_xz','nloginpwd':'Xuzhe@1990'})
# loginurl = 'https://passport.jd.com/new/login.aspx'
#
# result = opener.open(loginurl,postdata)
# cookie.save(ignore_discard=True,ignore_expires=True)
# listurl = 'https://order.jd.com/center/list.action'
# result = opener.open(listurl)
# print result.read()


#
# import urllib
# import urllib2
# import cookielib
# import re
# import socket
# from lxml import etree
#
# def login(url,data={ }):
#     trytimes = 0
#     while True:
#         if (trytimes>20):
#             print 'many times not success,give up'
#             break
#         try:
#             if (data=={ }):
#                 req = urllib2.Request(url)
#             else:
#                 req = urllib2.Request(url,urllib.urlencode(data))
#             req = urllib2.urlopen(req).read()
#             trytimes = trytimes + 1
#         except socket.error:
#             print '连接失败，尝试重新连接。'
#         else:
#             break
#     return req
#
#
#
# try:
#     # filename = 'cookie.txt'
#     cookie = cookielib.CookieJar()
#     handler = urllib2.HTTPCookieProcessor(cookie)
# except:
#     raise
# else:
#     opener = urllib2.build_opener(handler)
#     opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
#     urllib2.install_opener(opener)
#
#
# url = 'https://passport.jd.com/uc/login'
#
# logins = login(url)
# # print logins
#
# page = etree.HTML(logins)
# uuids = page.xpath('/html/body/div[2]/div/div[1]/div/div[3]/div[3]/div/form/input[2]')
# print uuids
# for i in uuids:
#     uuid = i.get('value')
# print uuid
# postdata = {'loginname':'jdsc_xz',
#             'nloginpwd':'Xuzhe@1990',
#             'loginpwd':'Xuzhe@1990',
#             'uuid':uuid,
#             'authcode':''}
# pqss = login(url,postdata)
# print pqss
#
#
#
# # uuid =



# -*- coding: utf-8 -*-
# !/usr/bin/python
import os
import urllib2
import urllib
import cookielib
import re
import sys
# import BeautifulSoup
from bs4 import BeautifulSoup



def getHtml(url,data={}):
	if(data=={}):
		req=urllib2.Request(url)
	else:
		req=urllib2.Request(url,urllib.urlencode(data))
	html=urllib2.urlopen(req).read()
	return html
try:
    cookie = cookielib.CookieJar()
    cookieProc = urllib2.HTTPCookieProcessor(cookie)
except:
    raise
else:
     opener = urllib2.build_opener(cookieProc)
     opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')]
     urllib2.install_opener(opener)
auth_url='https://passport.jd.com/uc/loginService'

home_url='http://usergrade.jd.com/user/consume'

url = "https://passport.jd.com/uc/login"
login=getHtml(url)
#print login
loginSoup = BeautifulSoup(login,'html.parser')

uuid = loginSoup.find_all("form")[0].find_all("input")[0]['value']
print uuid
clrName=loginSoup.find_all("form")[0].find_all("input")[6]['name']
clrValue=loginSoup.find_all("form")[0].find_all("input")[6]['value']

eid=loginSoup.find_all("form")[0].find_all("input")[4]['value']
fp=loginSoup.find_all("form")[0].find_all("input")[5]['value']

# checkPicUrl = loginSoup.find_all("div",id="o-authcode")[0].find_all("img")[0][‘src2‘]
# req = getHtml(checkPicUrl)
# checkPic = open("checkPic.jpg","w")
# checkPic.write(req)
# checkPic.close()
# #调用mac系统的预览(图像查看器)来打开图片文件
# os.system(‘open /Applications/Preview.app/ checkPic.jpg‘)
# checkCode = raw_input("请输入弹出图片中的验证码：")
# #登录URL
url = "http://passport.jd.com/uc/loginService"

postData = {
    'loginname':'jdsc_xz',
    'nloginpwd':'Xuzhe@1990',
    'loginpwd':'Xuzhe@1990',
    # str(clrName):str(clrValue),
    'uuid':uuid,
    'authcode': '',
}
passport=getHtml(url,postData)
print passport
cookieJar=cookielib.CookieJar()
# 实例化一个全局opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
# 获取cookie
# req=urllib2.Request(auth_url,postData)
# result = opener.open(req)
# result = opener.open(url,postData)
# 访问主页 自动带着cookie信息

result1 = opener.open('http://i.jd.com/user/info')
# 显示结果
print result1.read()
soup=BeautifulSoup(result1,'html.parser')
#昵称
# nickName = soup.find_all("input", id="nickName")[0]["value"]
# print "nickName:",
# print nickName