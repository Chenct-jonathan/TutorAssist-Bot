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
from ArticutAPI import Articut
import os
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_day_off = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"連假":["連假"],"進班":["進班"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_day_off:
        print("[day_off] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[XX][先]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        #for key, value in infoDICT.items():
            #print(key, ' : ', value)        
        try :
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
            #resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][-1][-1]["datetime"][:11], '%Y-%m-%d'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        #if infoDICT["time"] != [[]]:
            #resultDICT["CancelTimeText"] = infoDICT["time"][0][-1]["text"]
            #resultDICT["CancelDate"] = str(datetime.strptime(infoDICT["time"][0][-1]["datetime"], '%Y-%m-%d %H:%M:%S'))
        #else : 
            #resultDICT["CancelTimeText"] ="unknown"
            #resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "休息"
        pass

    if utterance == "[XX][先]停課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "停課"
        pass

    if utterance == "[XX][先]暫停":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "暫停"
        pass

    if utterance == "[XX][先]請[病假]":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "請{}".format(args[2])
        pass

    if utterance == "[XX][先]請假":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[今天][先]休息":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "休息"
        pass

    if utterance == "[今天][先]停課":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "停課"
        pass

    if utterance == "[今天][先]暫停":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "暫停"
        pass

    if utterance == "[今天][先]病假":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "病假"
        pass

    if utterance == "[今天][先]請假":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[今天]請病假":
        resultDICT["CancelTimeText"] = args[0]
        resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "請病假"
        pass

    if utterance == "[先]不上課喔":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不用來":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不用幫[XX]上課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不用幫[弟弟]上課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不用過來喔":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = "unknown"
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]讓[XX]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "休息"
        pass

    if utterance == "[先]讓[XX]停課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "停課"
        pass

    if utterance == "[先]讓[XX]暫停":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "暫停"
        pass

    if utterance == "[先]讓[XX]請假":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]讓[弟弟]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "休息"
        pass

    if utterance == "[先]讓[弟弟]停課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "停課"
        pass

    if utterance == "[先]讓[弟弟]暫停":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "暫停"
        pass

    if utterance == "[先]讓[弟弟]請假":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[1]
        resultDICT["CancelKeyword"] = "請假"
        pass

    if utterance == "[弟弟][先]休息":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "休息"
        pass

    if utterance == "[弟弟][先]停課":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "停課"
        pass

    if utterance == "[弟弟][先]暫停":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "暫停"
        pass

    if utterance == "[弟弟][先]請[病假]":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "請{}".format(args[2])
        pass

    if utterance == "[弟弟][先]請假":
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S'))
        except:
            resultDICT["CancelTimeText"] = "unknown"
            resultDICT["CancelDate"] ="unknown"
        resultDICT["Course/Student"] = args[0]
        resultDICT["CancelKeyword"] = "請假"
        pass

    return resultDICT