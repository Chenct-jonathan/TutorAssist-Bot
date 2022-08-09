#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import Articut
import json
import re

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

resultDICT = articut.parse("今天崇瑋先請假", level="lv3")
print(resultDICT)
print(resultDICT["event"][0][0])
posSTR = "".join(resultDICT["time"][0][0]["datetime"])
print(posSTR)
DateSTR = re.search("[0-9]+-[0-9]+-[0-9]+", posSTR)
print(DateSTR)

#print(resultDICT["time"][0][0]["datetime"][0])
print(resultDICT["time"][0][0]["text"])
print(resultDICT["event"][0][1])


#for key, value in resultDICT.items():
    #print(key, ' : ', value)