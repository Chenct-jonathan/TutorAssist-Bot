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
        # write your code here
        pass

    if utterance == "[中秋節]快樂":
        # write your code here
        pass

    if utterance == "[假期][愉快]":
        # write your code here
        pass

    if utterance == "[假期]快樂":
        # write your code here
        pass

    return resultDICT