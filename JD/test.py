#-*-coding:utf-8-*-
import json

text={"CommentsCount":[{"SkuId":4835534,"ProductId":4835534,"ShowCount":30000,"ShowCountStr":"3+",
                   "CommentCountStr":"20+","CommentCount":200000,"AverageScore":5,"GoodCountStr":"19+",
                   "GoodCount":190000,"AfterCount":3100,"AfterCountStr":"3100+","GoodRate":0.976,"GoodRateShow":98,
                   "GoodRateStyle":146,"GeneralCountStr":"2900+","GeneralCount":2900,"GeneralRate":0.014,"GeneralRateShow":1,
                   "GeneralRateStyle":2,
                   "PoorCountStr":"2000+","PoorCount":2000,"PoorRate":0.01,"PoorRateShow":1,"PoorRateStyle":2}]}
js = json.loads(str(text))
# print text['CommentsCount'][0]['CommentCount']
# print text['CommentsCount'][0]['GoodRate']