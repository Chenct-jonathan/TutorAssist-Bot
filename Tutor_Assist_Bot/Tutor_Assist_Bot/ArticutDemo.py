#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import Articut
import json
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

resultDICT = articut.parse("明天弟弟先請假好了", level="lv2")
userDefinedDict = json.load(open("./intent/USER_DEFINED.json",encoding="utf-8"))
infoDICT = articut.parse("老師連假愉快喔", level="lv2", userDefinedDictFILE = "./intent/USER_DEFINED.json")
nounStemLIST = articut.getNounStemLIST(resultDICT)
timeLIST = articut.NER.getTime(infoDICT)

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

demoSTR = articut.parse("我覺得今天先讓他休息好了!", level = "lv2")

print(demoSTR)


for key, value in infoDICT.items():
    print(key, ' : ', value)
    
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

