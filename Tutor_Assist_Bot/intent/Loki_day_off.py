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
        resultDICT["CancelTime"] = infoDICT["time"]
        
        pass

    if utterance == "[XX][先]停課":
        # write your code here
        pass

    if utterance == "[XX][先]暫停":
        # write your code here
        pass

    if utterance == "[XX][先]請假":
        # write your code here
        pass

    if utterance == "[今天][先]休息":
        # write your code here
        pass

    if utterance == "[今天][先]停課":
        # write your code here
        pass

    if utterance == "[今天][先]暫停":
        # write your code here
        pass

    if utterance == "[今天][先]請假":
        # write your code here
        pass

    if utterance == "[先]不上課喔":
        # write your code here
        pass

    if utterance == "[先]不用[過]來喔":
        # write your code here
        pass

    if utterance == "[先]不用來":
        # write your code here
        pass

    if utterance == "[先]不用幫[XX]上課":
        # write your code here
        pass

    if utterance == "[先]不用幫[弟弟]上課":
        # write your code here
        pass

    if utterance == "[先]讓[XX]休息":
        # write your code here
        pass

    if utterance == "[先]讓[XX]停課":
        # write your code here
        pass

    if utterance == "[先]讓[XX]暫停":
        # write your code here
        pass

    if utterance == "[先]讓[XX]請假":
        # write your code here
        pass

    if utterance == "[先]讓[弟弟]休息":
        # write your code here
        pass

    if utterance == "[先]讓[弟弟]停課":
        # write your code here
        pass

    if utterance == "[先]讓[弟弟]暫停":
        # write your code here
        pass

    if utterance == "[先]讓[弟弟]請假":
        # write your code here
        pass

    if utterance == "[弟弟][先]休息":
        # write your code here
        pass

    if utterance == "[弟弟][先]停課":
        # write your code here
        pass

    if utterance == "[弟弟][先]暫停":
        # write your code here
        pass

    if utterance == "[弟弟][先]請假":
        # write your code here
        pass

    return resultDICT