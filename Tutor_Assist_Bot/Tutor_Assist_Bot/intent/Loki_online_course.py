#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for online_course

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

DEBUG_online_course = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_online_course:
        print("[online_course] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[可以]改成[線上]":
        # write your code here
        pass

    if utterance == "[可以]調整為視訊上課":
        # write your code here
        pass

    if utterance == "是否維持[同個時段][上]線上課":
        # write your code here
        pass

    if utterance == "是否調整為視訊上課":
        # write your code here
        pass

    return resultDICT