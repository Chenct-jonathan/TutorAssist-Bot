#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for warm_blessing

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

DEBUG_warm_blessing = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"連假":["連假"],"進班":["進班"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_warm_blessing:
        print("[warm_blessing] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["warm_blessing"] = {}
    if utterance == "[中秋節]快樂":
        resultDICT["intentLIST"].append("warm_blessing")
        infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
        try:
            resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
        except:
            resultDICT["warm_blessing"]["Holiday"] = "unknown"
        pass

    if utterance == "[中秋節]愉快":
        resultDICT["intentLIST"].append("warm_blessing")
        infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
        try:
            resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
        except:
            resultDICT["warm_blessing"]["Holiday"] = "unknown"
        pass

    if utterance == "[假期]快樂":
        resultDICT["intentLIST"].append("warm_blessing")
        infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
        try:
            resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
        except:
            resultDICT["warm_blessing"]["Holiday"] = "unknown"
        pass

    if utterance == "[假期]愉快":
        resultDICT["intentLIST"].append("warm_blessing")
        infoDICT = articut.parse(args[0], userDefinedDictFILE = "./intent/USER_DEFINED.json")
        try:
            resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
        except:
            resultDICT["warm_blessing"]["Holiday"] = "unknown"
        pass

    if utterance == "祝[你]":
        resultDICT["intentLIST"].append("warm_blessing")
        infoDICT = articut.parse(inputSTR, userDefinedDictFILE = "./intent/USER_DEFINED.json")
        try:
            resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
        except:
            resultDICT["warm_blessing"]["Holiday"] = "unknown"
        pass

    if utterance == "祝[老師]":
        resultDICT["intentLIST"].append("warm_blessing")
        infoDICT = articut.parse(inputSTR, userDefinedDictFILE = "./intent/USER_DEFINED.json")
        try:
            resultDICT["warm_blessing"]["Holiday"] = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
        except:
            resultDICT["warm_blessing"]["Holiday"] = "unknown"
        pass

    return resultDICT