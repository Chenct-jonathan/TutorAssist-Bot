#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for class_arrangement_adv

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

DEBUG_class_arrangement_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"線上":["線上"],"連假":["連假"],"進班":["進班"],"遠距":["遠距"],"小時半":["小時半"],"面對面":["面對面"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_class_arrangement_adv:
        print("[class_arrangement_adv] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["class_arrangement"] = {}
    if utterance == "10.ok嗎":
        resultDICT["class_arrangement"]["AlterTime"] = args[0]
        pass

    if utterance == "10.可以嗎":
        # write your code here
        pass

    if utterance == "10.好嗎":
        # write your code here
        pass

    if utterance == "10.方便嗎":
        # write your code here
        pass

    if utterance == "10ok嗎":
        # write your code here
        pass

    if utterance == "3-5ok嗎":
        # write your code here
        pass

    if utterance == "3-5嗎":
        # write your code here
        pass

    if utterance == "3-5好嗎":
        # write your code here
        pass

    if utterance == "3-5點你ok嗎":
        # write your code here
        pass

    if utterance == "3-5點你可以嗎":
        # write your code here
        pass

    if utterance == "3-5點你方便嗎":
        # write your code here
        pass

    if utterance == "3-5點嗎":
        # write your code here
        pass

    if utterance == "3-五點好嗎":
        # write your code here
        pass

    if utterance == "3.-5.你ok嗎":
        # write your code here
        pass

    if utterance == "3.-5.你可以嗎":
        # write your code here
        pass

    if utterance == "3.-5.你方便嗎":
        # write your code here
        pass

    if utterance == "3點-5你ok嗎":
        # write your code here
        pass

    if utterance == "3點-5你可以嗎":
        # write your code here
        pass

    if utterance == "3點-5你方便嗎":
        # write your code here
        pass

    if utterance == "3點-5嗎":
        # write your code here
        pass

    if utterance == "三點-5ok嗎":
        # write your code here
        pass

    if utterance == "三點到5好嗎":
        # write your code here
        pass

    if utterance == "三點到五點你ok嗎":
        # write your code here
        pass

    if utterance == "三點到五點你可以嗎":
        # write your code here
        pass

    if utterance == "三點到五點你方便嗎":
        # write your code here
        pass

    if utterance == "三點到五點嗎":
        # write your code here
        pass

    if utterance == "三點到五點好嗎":
        # write your code here
        pass

    if utterance == "十點ok嗎":
        # write your code here
        pass

    if utterance == "十點可以嗎":
        # write your code here
        pass

    if utterance == "十點好嗎":
        # write your code here
        pass

    if utterance == "十點方便嗎":
        # write your code here
        pass

    return resultDICT