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
    resultDICT["physical_course"] = {}
    if utterance == "[先][面對面]上課":
        if args[1] not in ["線上","視訊","遠距"] and "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]到[府]上課":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]到班上課":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]實體":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復[面對面]":
        if args[1] not in ["線上","視訊","遠距"]and "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復到[府]":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復實體":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復實體課程":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復進班":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改回[面對面]":
        if args[1] not in ["線上","視訊","遠距"]and "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改回到[府]":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改回實體":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改回實體課程":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改回進班":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]進班上課":
        if "線上" not in inputSTR and "視訊" not in inputSTR and "遠距" not in inputSTR:
            resultDICT["intentLIST"].append("physical_course")
        pass

    return resultDICT