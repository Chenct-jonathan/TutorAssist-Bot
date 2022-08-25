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
from ArticutAPI import Articut
import os
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_class_arrangement = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"線上":["線上"],"連假":["連假"],"進班":["進班"],"遠距":["遠距"],"小時半":["小時半"],"面對面":["面對面"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_class_arrangement:
        print("[class_arrangement] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["class_arrangement"] = {}
    if utterance == "[禮拜天][可以]幫[XX]上課嗎":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[2]
        pass

    if utterance == "[禮拜天][可以]幫[弟弟]上課嗎":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[2]
        pass

    if utterance == "延[後][一]小時半":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[1]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "延[後][半個][小時]":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[1]+args[2]
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "延[後][半小時]":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[1]
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "延[後]到[8].":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[1]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "延[後]到[八點]":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[1]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "延後"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "提早[一]小時半":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[1]+"小時半"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "提早[半個][小時]":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[1]+args[2]
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "提早[半小時]":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = args[1]
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "提早到[8].":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "提早到[八點]":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "提早"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "改[8].":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "改[XX]的時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]
        pass

    if utterance == "改[八點]":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "改[週四]的時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]
        pass

    if utterance == "改一下[XX]的時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]
        pass

    if utterance == "改一下上課時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "改一下時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "改上課時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "改到[8].":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "改到[八點]":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "改時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "討論[XX]的時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]
        pass

    if utterance == "討論[週四]的時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]
        pass

    if utterance == "討論上課時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "調整[XX]的時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]
        pass

    if utterance == "調整[週四]的時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = args[0]
        pass

    if utterance == "調整上課時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    if utterance == "調整時間":
        resultDICT["intentLIST"].append("class_arrangement")
        resultDICT["class_arrangement"]["AlterTime"] = "unknown"
        resultDICT["class_arrangement"]["EarlyOrLate"] = "unknown"
        resultDICT["class_arrangement"]["AlterTimeSpan"] = "unknown"
        resultDICT["class_arrangement"]["Course/Student"] = "unknown"
        pass

    return resultDICT