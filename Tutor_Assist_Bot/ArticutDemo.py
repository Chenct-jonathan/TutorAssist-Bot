#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import Articut
import json
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

resultDICT = articut.parse("我想說今天崇瑋英文課先請假好了", level="lv2")
infoDICT = articut.parse("我想說今天崇瑋英文課先請假好了", level="lv3")
nounStemLIST = articut.getNounStemLIST(resultDICT)
timeLIST = articut.NER.getTime(resultDICT)

now = datetime.now()

#day = infoDICT["time"][0][0]["datetime"].strftime("%d")
#print(resultDICT)
print(infoDICT)

date_time_obj = datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S')
#print(resultDICT["event"][0][0])
#posSTR = "".join(resultDICT["time"][0][0]["datetime"])
#print(posSTR)
#DateSTR = re.search("[0-9]+-[0-9]+-[0-9]+", posSTR)
#print(DateSTR)

#print(resultDICT["time"][0][0]["datetime"][0])
#print(resultDICT["time"][0][0]["text"])
#print(resultDICT["event"][0][1])


for key, value in resultDICT.items():
    print(key, ' : ', value)
    
print(nounStemLIST)
print(re.search(r'[\u4e00-\u9fff]+',"".join(map(str,nounStemLIST[0][0]))).group())
print(re.search(r'[\u4e00-\u9fff]+',"".join(map(str,timeLIST[0][0]))).group())

print(re.search("[0-9]+-[0-9]+-[0-9]+","".join(infoDICT["time"][0][0]["datetime"])).group())
#print(day)
print(now)
print(type(now))
print(date_time_obj)

