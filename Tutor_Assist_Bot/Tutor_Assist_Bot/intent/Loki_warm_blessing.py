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
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_warm_blessing:
        print("[warm_blessing] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[中秋節][愉快]":
        infoDICT = articut.parse(inputSTR)
        if len(args[1])<2:
            resultDICT["Holiday"] = "unknown"
        else :resultDICT["Holiday"] = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
        pass

    if utterance == "[中秋節]快樂":
        infoDICT = articut.parse(inputSTR)
        if len(args[1])<2:
            resultDICT["Holiday"] = "unknown"
        else :resultDICT["Holiday"] = re.search("<TIME_holiday>([^<]+)</TIME_holiday>", "".join(infoDICT["result_pos"])).group(1)
        pass

    if utterance == "[假期][愉快]":
        infoDICT = articut.parse(inputSTR, userDefinedDictFILE = "./intent/USER_DEFINED.json")
        if len(args[1])<2:
            resultDICT["Holiday"] = "unknown"
        else :resultDICT["Holiday"] = re.search("((?<=<ENTITY_noun>)|(?<=<ENTITY_nouny>)|(?<=<UserDefined>))([^>]+)((?=</ENTITY_noun><MODIFIER>愉快</MODIFIER>)|(?=</ENTITY_nouny><MODIFIER>愉快</MODIFIER>)|(?=</UserDefined><MODIFIER>愉快</MODIFIER>))", "".join(infoDICT["result_pos"])).group(2)
        pass

    if utterance == "[假期]快樂":
        infoDICT = articut.parse(inputSTR, userDefinedDictFILE = "./intent/USER_DEFINED.json")
        print(infoDICT)
        resultDICT["Holiday"] = re.search("((?<=<ENTITY_noun>)|(?<=<ENTITY_nouny>)|(?<=<UserDefined>))([^>]+)((?=</ENTITY_noun><ENTITY_nouny>快樂</ENTITY_nouny>)|(?=</ENTITY_nouny><ENTITY_nouny>快樂</ENTITY_nouny>)|(?=</UserDefined><ENTITY_nouny>快樂</ENTITY_nouny>))", "".join(infoDICT["result_pos"])).group(2)
        pass

    return resultDICT