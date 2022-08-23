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
    userDefinedDICT = {"愉快":["愉快"],"連假":["連假"],"進班":["進班"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_online_course:
        print("[online_course] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["online_course"] = {}
    if utterance == "[先]恢復[線上]":
        if args[1] in ["線上","視訊","遠距"]:
            resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]恢復視訊":
        resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]改成[線上]":
        if args[1] in ["線上","視訊","遠距"]:
            resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]改成視訊":
        resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]用[線上]":
        if args[1] in ["線上","視訊","遠距"]:
            resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]用視訊":
        resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]維持[線上]":
        if args[1] in ["線上","視訊","遠距"]:
            resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]維持視訊":
        resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]調整為[線上]":
        if args[1] in ["線上","視訊","遠距"]:
            resultDICT["intentLIST"].append("online_course")
        pass

    if utterance == "[先]調整為視訊":
        resultDICT["intentLIST"].append("online_course")
        pass

    return resultDICT