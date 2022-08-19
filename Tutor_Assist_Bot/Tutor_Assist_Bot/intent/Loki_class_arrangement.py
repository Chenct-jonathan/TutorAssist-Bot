#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for class_arrangement

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
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_class_arrangement = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"連假":["連假"],"進班":["進班"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_class_arrangement:
        print("[class_arrangement] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["class_arrangement"] = {}
    if utterance == "[15].[你][方便]嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""
        resultDICT["AlterTime"] = args[0]

        pass

    if utterance == "[15].[你]ok 嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[15].[老師]ok嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[15].好嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[七點]好嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[三點][你]ok嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[三點][老師]ok嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[五點][你][可以]嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[五點][你][方便]嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[五點][老師][可以]嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[五點][老師][方便]嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""        
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "[可以]改上課時間嗎":
        resultDICT["EarlyOrLate"] = "unknown"
        resultDICT["AlterTimeSpan"] = "unknown"
        resultDICT["AlterTime"] = "unknown"
        pass

    if utterance == "[可以]改時間嗎":
        resultDICT["EarlyOrLate"] = "unknown"
        resultDICT["AlterTimeSpan"] = "unknown"
        resultDICT["AlterTime"] = "unknown"
        pass

    if utterance == "[提早][半][小時]":
        #parsing bug
        pass

    if utterance == "[禮拜天][可以]幫[XX]上課嗎":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] = ""
        resultDICT["AlterTime"] = args[0]
        resultDICT["Course/Student"] = args[2]
        pass

    if utterance == "延[後][半][小時]":
        resultDICT["EarlyOrLate"] = args[0]
        resultDICT["AlterTimeSpan"] = args[1]+args[2]
        resultDICT["AlterTime"] = ""
        pass

    if utterance == "延[後]到[8].":
        resultDICT["EarlyOrLate"] = args[0]
        resultDICT["AlterTimeSpan"] =""
        resultDICT["AlterTime"] = args[1]
        pass

    if utterance == "延[後]到[八點]":
        resultDICT["EarlyOrLate"] = args[0]
        resultDICT["AlterTimeSpan"] =""
        resultDICT["AlterTime"] = args[1]
        pass

    if utterance == "提早到[8].":
        resultDICT["EarlyOrLate"] = "提早"
        resultDICT["AlterTimeSpan"] =""
        resultDICT["AlterTime"] = args[1]
        pass

    if utterance == "提早到[八點]":
        resultDICT["EarlyOrLate"] = "提早"
        resultDICT["AlterTimeSpan"] =""
        resultDICT["AlterTime"] = args[1]
        pass

    if utterance == "改[8].":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] =""
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "改[八點]":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] =""
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "改到[8].":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] =""
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "改到[八點]":
        resultDICT["EarlyOrLate"] = ""
        resultDICT["AlterTimeSpan"] =""
        resultDICT["AlterTime"] = args[0]
        pass

    if utterance == "需要調整時間嗎":
        resultDICT["EarlyOrLate"] = "unknown"
        resultDICT["AlterTimeSpan"] ="unknown"
        resultDICT["AlterTime"] = "unknown"
        pass

    return resultDICT