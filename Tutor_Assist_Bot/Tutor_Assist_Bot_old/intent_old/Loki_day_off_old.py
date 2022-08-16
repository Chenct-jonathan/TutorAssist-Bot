#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for day_off

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os
from ArticutAPI import Articut
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

scheduleDICT = {"Mon":"", "Tue":"", "Wed":"", "Thurs":"", "Fri":"","Sat":"", "Sun":""}

DEBUG_day_off = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_day_off:
        print("[day_off] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[XX][先]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        if infoDICT["time"] != [[]]:
            resultDICT["CancelTimeText"] = infoDICT["time"][0][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][-1]["datetime"], '%Y-%m-%d %H:%M:%S'))
        else : 
            resultDICT["CancelTimeText"] ="unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        
        pass

    if utterance == "[XX][先]停課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        if infoDICT["time"] != [[]]:
            resultDICT["CancelTimeText"] = infoDICT["time"][0][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][-1]["datetime"], '%Y-%m-%d %H:%M:%S'))
        else : 
            resultDICT["CancelTimeText"] ="unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        
        pass

    if utterance == "[XX][先]暫停":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        if infoDICT["time"] != [[]]:
            resultDICT["CancelTimeText"] = infoDICT["time"][0][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][-1]["datetime"], '%Y-%m-%d %H:%M:%S'))
        else : 
            resultDICT["CancelTimeText"] ="unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        
        pass

    if utterance == "[XX][先]請假":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        if infoDICT["time"] != [[]]:
            resultDICT["CancelTimeText"] = infoDICT["time"][0][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][-1]["datetime"], '%Y-%m-%d %H:%M:%S'))
        else : 
            resultDICT["CancelTimeText"] ="unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        
        pass

    if utterance == "[今天][先]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"

        pass

    if utterance == "[今天][先]停課":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"

        pass

    if utterance == "[今天][先]暫停":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"

        pass

    if utterance == "[今天][先]請假":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"
        
        pass

    if utterance == "[先]不上課喔":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][-1]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = "不上課"
        pass

    if utterance == "[先]不用[過]來喔":
        # write your code here
        pass

    if utterance == "[先]不用來":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S'))
        pass

    if utterance == "[先]不用幫[XX]上課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = "不用過去"
        pass

    if utterance == "[先]不用幫[弟弟]上課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = ("不用幫"+infoDICT["event"][0][0]+infoDICT["event"][0][1])
        pass

    if utterance == "[先]讓[XX]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[先]讓[XX]停課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[先]讓[XX]暫停":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[先]讓[XX]請假":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[先]讓[弟弟]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[先]讓[弟弟]停課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[先]讓[弟弟]暫停":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[先]讓[弟弟]請假":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[弟弟][先]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[弟弟][先]停課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[弟弟][先]暫停":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[弟弟][先]請假":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["CancelKeyword"] = infoDICT["event"][0][1]
        pass

    if utterance == "[XX]請[病假]":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = "UNKOWN"
        resultDICT["CancelDate"] = "UNKNOWN"
        resultDICT["CancelKeyword"] = re.search("請([^>]+假)",inputSTR).group(1)
        pass

    if utterance == "[今天][病假]":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        #resultDICT["CancelKeyword"] = re.search("([^>]+假)",inputSTR).group(1)
        pass

    if utterance == "[今天]請[病假]":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        print(infoDICT)
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))        
        resultDICT["CancelKeyword"] = re.search("請([^>]+假)",inputSTR).group(1)
        pass

    if utterance == "[弟弟]請[病假]":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        resultDICT["CancelTimeText"] = infoDICT["time"][0][0]["text"]
        resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))        
        resultDICT["CancelKeyword"] = re.search("請([^>]+假)",inputSTR).group(1)
        pass

    return resultDICT