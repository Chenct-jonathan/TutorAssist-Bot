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
    userDefinedDICT = {"_asNoun":["連假","線上","進班","遠距","面對面","愉快","線下","到班","實體課程"],"_asOkay":["ok","OK","oK","Ok","Okay","okay","OKAY"],"_asTime":["小時半"],"_asVerb":["改一下","討論一下","調整一下"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_physical_course:
        print("[physical_course] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["physical_course"] = {}
    if utterance == "[先]到[家][中]上課":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]到[家][中]授課":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]到府上課":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]到府授課":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]到班上課":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]到線下":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]實體":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]實體課程":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復到班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復實體":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復實體課程":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復線下":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復進班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復面對面":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]恢復面授":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改到班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改實體":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改實體課程":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改線下":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改進班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改面對面":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]改面授":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]用到班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]用實體":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]用實體課程":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]用線下":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]用進班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]用面對面":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]用面授":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]線下":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]調整為到班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]調整為實體":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]調整為實體課程":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]調整為線下":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]調整為進班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]調整為面授":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]進班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]面對面":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先]面授":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先都]到府":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先都]到班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先都]實體":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先都]實體課程":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先都]線下":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先都]進班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先都]面對面":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "[先都]面授":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "要[先]到班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "要[先]實體":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "要[先]線下":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "要[先]進班":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "要[先]面對面":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "要[先]面授":
        resultDICT["intentLIST"].append("physical_course")
        pass

    if utterance == "要實體課程":
        resultDICT["intentLIST"].append("physical_course")
        pass

    return resultDICT