#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for inform_time_adv

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

DEBUG_inform_time_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"線上":["線上"],"連假":["連假"],"進班":["進班"],"遠距":["遠距"],"小時半":["小時半"],"面對面":["面對面"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_inform_time_adv:
        print("[inform_time_adv] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "8-10":
        # write your code here
        pass

    if utterance == "8/16 8.":
        # write your code here
        pass

    if utterance == "8/16 8:00":
        # write your code here
        pass

    if utterance == "8/16 八點":
        # write your code here
        pass

    if utterance == "8/16的8-10":
        # write your code here
        pass

    if utterance == "8/16的8:00-10:00":
        # write your code here
        pass

    if utterance == "8/16的八點到十點":
        # write your code here
        pass

    if utterance == "八月16 8.":
        # write your code here
        pass

    if utterance == "八月16 8:00":
        # write your code here
        pass

    if utterance == "八月16的8-10":
        # write your code here
        pass

    if utterance == "八月16的8:00-10:00":
        # write your code here
        pass

    if utterance == "八月16的五點到七點":
        # write your code here
        pass

    if utterance == "八月十六日":
        # write your code here
        pass

    if utterance == "八月十六日的5-7":
        # write your code here
        pass

    if utterance == "八月十六日的5:00到7:00":
        # write your code here
        pass

    if utterance == "八月十六日的五點到七點":
        # write your code here
        pass

    if utterance == "八月十六日的八點":
        # write your code here
        pass

    if utterance == "八月十六的八點":
        # write your code here
        pass

    if utterance == "八點-十點":
        # write your code here
        pass

    return resultDICT