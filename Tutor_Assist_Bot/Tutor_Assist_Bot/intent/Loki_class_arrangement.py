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

DEBUG_class_arrangement = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_class_arrangement:
        print("[class_arrangement] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[可以]提[前]到[9].嗎":
        # write your code here
        pass

    if utterance == "[可以]提[前]到[9]:[30]嗎":
        # write your code here
        pass

    if utterance == "[可以]提[前]到[九點]嗎":
        # write your code here
        pass

    if utterance == "[可以]提早到[9].嗎":
        # write your code here
        pass

    if utterance == "[可以]提早到[9]:[30]嗎":
        # write your code here
        pass

    if utterance == "[可以]提早到[九點]嗎":
        # write your code here
        pass

    if utterance == "[可以]改[下午]2-4上課":
        # write your code here
        pass

    if utterance == "[可以]改到[9].嗎":
        # write your code here
        pass

    if utterance == "[可以]改到[9]:[30]嗎":
        # write your code here
        pass

    if utterance == "[可以]改到[九點]嗎":
        # write your code here
        pass

    if utterance == "[能]延[後][一小時][半]":
        # write your code here
        pass

    if utterance == "[能]延[後][半][小時]":
        # write your code here
        pass

    if utterance == "[能]延[後][半個][小時]":
        # write your code here
        pass

    if utterance == "[這週][可以]改[時間]":
        # write your code here
        pass

    if utterance == "[這週][家教][可以]改時間嗎":
        # write your code here
        pass

    if utterance == "[這週]上課[可以]改時間嗎":
        # write your code here
        pass

    if utterance == "上課[日][我]想商量調整一下":
        # write your code here
        pass

    if utterance == "上課[日][我]想討論一下":
        # write your code here
        pass

    if utterance == "想要延[後][一個半小時]":
        # write your code here
        pass

    if utterance == "想要延[後][一小時][半]":
        # write your code here
        pass

    if utterance == "想討論[下週]的[時間]":
        # write your code here
        pass

    if utterance == "換成[禮拜二][6]-[8]上課":
        # write your code here
        pass

    if utterance == "改[8]到[10]":
        # write your code here
        pass

    if utterance == "改[8]至[10]":
        # write your code here
        pass

    if utterance == "改[八點]至[十點]":
        # write your code here
        pass

    if utterance == "改[周一][8]-[10]":
        # write your code here
        pass

    if utterance == "改成[周日]過來":
        # write your code here
        pass

    return resultDICT