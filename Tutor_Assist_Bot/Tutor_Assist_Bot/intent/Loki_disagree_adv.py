#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for disagree_adv

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

DEBUG_disagree_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"線上":["線上"],"連假":["連假"],"進班":["進班"],"遠距":["遠距"],"小時半":["小時半"],"面對面":["面對面"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_disagree_adv:
        print("[disagree_adv] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "no":
        if "agree" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("agree")
            resultDICT["intentLIST"].append("disagree")
        elif len(inputSTR) >= 6:
            pass
        else: 
            resultDICT["intentLIST"].append("disagree")
        pass

    if utterance == "不對":
        if "agree" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("agree")
            resultDICT["intentLIST"].append("disagree")
        else: resultDICT["intentLIST"].append("disagree")
        pass

    if utterance == "不是":
        if "agree" in resultDICT["intentLIST"]:
            resultDICT["intentLIST"].remove("agree")
            resultDICT["intentLIST"].append("disagree")
        else: resultDICT["intentLIST"].append("disagree")
        pass

    if utterance == "錯":
        if "agree" in resultDICT["intentLIST"]:
            pass
        else: resultDICT["intentLIST"].append("disagree")
        pass

    if utterance == "錯誤":
        if "agree" in resultDICT["intentLIST"]:
            pass
        else: resultDICT["intentLIST"].append("disagree")
        pass

    return resultDICT