#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for physical_course

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

DEBUG_physical_course = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"連假":["連假"],"進班":["進班"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_physical_course:
        print("[physical_course] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[先][面對面]上課":
        # write your code here
        pass

    if utterance == "[先]到[府]上課":
        # write your code here
        pass

    if utterance == "[先]到班上課":
        # write your code here
        pass

    if utterance == "[先]實體":
        # write your code here
        pass

    if utterance == "[先]恢復[面對面]":
        # write your code here
        pass

    if utterance == "[先]恢復到[府]":
        # write your code here
        pass

    if utterance == "[先]恢復實體":
        # write your code here
        pass

    if utterance == "[先]恢復實體課程":
        # write your code here
        pass

    if utterance == "[先]恢復進班":
        # write your code here
        pass

    if utterance == "[先]改回[面對面]":
        # write your code here
        pass

    if utterance == "[先]改回到[府]":
        # write your code here
        pass

    if utterance == "[先]改回實體":
        # write your code here
        pass

    if utterance == "[先]改回實體課程":
        # write your code here
        pass

    if utterance == "[先]改回進班":
        # write your code here
        pass

    if utterance == "[先]進班上課":
        # write your code here
        pass

    return resultDICT