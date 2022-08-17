#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import Articut
import json
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

resultDICT = articut.parse("祝老師中秋節快樂", level="lv2")
userDefinedDict = json.load(open("./intent/USER_DEFINED.json",encoding="utf-8"))

#for key, value in resultDICT.items():
    #print(key, ' : ', value)
    
try:
    holiday = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(resultDICT["result_pos"])).group(1)
except:
    holiday = "unknown"
print(holiday)

#STR = "12345"
#print(STR[1:3])

infoDICT = articut.parse("崇瑋早上發燒，下午英文課先休息", level="lv3")
for key, value in infoDICT.items():
    print(key, ' : ', value)
print(str(infoDICT["time"][-1][-1]["time_span"]["year"][0]) + str(infoDICT["time"][-1][-1]["time_span"]["month"][0])+str(infoDICT["time"][-1][-1]["time_span"]["day"][0])+str(infoDICT["time"][-1][-1]["time_span"]["weekday"][0]))
print(str(datetime.strptime(str(infoDICT["time"][-1][-1]["time_span"]["year"][0]) + str(infoDICT["time"][-1][-1]["time_span"]["month"][0])+str(infoDICT["time"][-1][-1]["time_span"]["day"][0])+str(infoDICT["time"][-1][-1]["time_span"]["weekday"][0]),'%Y%m%d%w')))
#print(str(datetime.strptime(infoDICT["time"][-1][-1]["datetime"][0:11], '%Y-%m-%d')))






#outPutDICT = {}
#outPutDICT["CancelDate"] = str(datetime.strptime(resultDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
#outPutDICT["CancelTimeText"] = resultDICT["time"][0][0]["text"] 
#outPutDICT["CancelKeyword"] = 
#infoDICT = articut.parse("老師連假愉快喔", level="lv2", userDefinedDictFILE = "./intent/USER_DEFINED.json")
#nounStemLIST = articut.getNounStemLIST(resultDICT)
#timeLIST = articut.NER.getTime(infoDICT)

#now = datetime.now()

#day = infoDICT["time"][0][0]["datetime"].strftime("%d")
#print(resultDICT)
#print(infoDICT)

#date_time_obj = datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S')
#print(resultDICT["event"][0][0])
#posSTR = "".join(resultDICT["time"][0][0]["datetime"])
#print(posSTR)
#DateSTR = re.search("[0-9]+-[0-9]+-[0-9]+", posSTR)
#print(DateSTR)

#print(resultDICT["time"][0][0]["datetime"][0])
#print(resultDICT["time"][0][0]["text"])
#print(resultDICT["event"][0][1])

#demoSTR = articut.parse("我覺得今天先讓他休息好了!", level = "lv2")

#print(demoSTR)
    
#print(str(datetime.strptime(articut.parse("今天", level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S')))
#print(outPutDICT)
    
#print(re.search("<ENTITY_nouny>([^<]+)</ENTITY_nouny><MODIFIER>愉快</MODIFIER>", "".join(infoDICT["result_pos"])).group(1))
    
#print(re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1))

#print(timeLIST)
#print(re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1))
    
    
#print(nounStemLIST)
#print(re.search(r'[\u4e00-\u9fff]+',"".join(map(str,nounStemLIST[0][0]))).group())
#print(re.search(r'[\u4e00-\u9fff]+',"".join(map(str,timeLIST[0][0]))).group())

#print(re.search("[0-9]+-[0-9]+-[0-9]+","".join(infoDICT["time"][0][0]["datetime"])).group())
#print(day)
#print(now)
#print(type(now))
#print(date_time_obj)
#print(infoDICT["event"][0][1])

