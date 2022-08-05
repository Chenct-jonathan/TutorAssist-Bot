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
    if utterance == "[可以]換成[禮拜二][6]-[8]上課嗎?":
        # write your code here
        pass

    if utterance == "[可以]改[周一][8]-[10]嗎?":
        # write your code here
        pass

    if utterance == "[周一][可以]改[1]-[3]上課嗎":
        # write your code here
        pass

    if utterance == "[老師]早安:[5月]的上課[日][我]想商量調整一下。":
        # write your code here
        pass

    if utterance == "[週日][方便]改[下午][2]-[4]上課嗎?":
        # write your code here
        pass

    return resultDICT