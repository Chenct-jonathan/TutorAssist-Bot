#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for day_off

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
from ArticutAPI import Articut
import os
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_day_off = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"線上":["線上"],"連假":["連假"],"進班":["進班"],"遠距":["遠距"],"小時半":["小時半"],"面對面":["面對面"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_day_off:
        print("[day_off] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["day_off"] = {}
    if utterance == "[XX][先]休息":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "休息"
        pass

    if utterance == "[XX][先]停課":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "停課"
        pass
        pass

    if utterance == "[XX][先]暫停":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "暫停"
        pass

    if utterance == "[XX][先]病假":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[XX][先]請[病假]":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請{}".format(args[2])
        pass

    if utterance == "[XX][先]請假":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[XX][可能]要[先]休息了":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "休息"
        pass

    if utterance == "[XX][可能]要[先]停課了":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "停課"
        pass

    if utterance == "[XX][可能]要[先]暫停了":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "暫停"
        pass

    if utterance == "[XX][可能]要[先]請假了":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[XX]要[先]休息":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "休息"
        pass

    if utterance == "[XX]要[先]停課":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "停課"
        pass

    if utterance == "[XX]要[先]暫停":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "暫停"
        pass

    if utterance == "[XX]要[先]病假":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[XX]要[先]請假":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[XX]要[先]請病假":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][-1][-1]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[今天][先]休息":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "休息"
        pass

    if utterance == "[今天][先]停課":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "停課"
        pass

    if utterance == "[今天][先]暫停":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "暫停"
        pass

    if utterance == "[今天][先]病假":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "病假"
        pass

    if utterance == "[今天][先]請假":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        try:
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelDate"]= "unknown"
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[今天][先]請病假":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[今天]要[先]休息":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "休息"
        pass

    if utterance == "[今天]要[先]停課":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "停課"
        pass

    if utterance == "[今天]要[先]暫停":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "暫停"
        pass

    if utterance == "[今天]要[先]病假":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[今天]要[先]請假":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[今天]要[先]請病假":
        resultDICT["intentLIST"].append("day_off")
        resultDICT["day_off"]["CancelTimeText"] = args[0]
        resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(args[0], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不上課喔":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不用來":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不用幫[XX]上課":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[1]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不用幫[弟弟]上課":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[1]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[先]不用過來喔":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = "unknown"
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[弟弟][先]休息":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "休息"
        pass

    if utterance == "[弟弟][先]停課":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "停課"
        pass

    if utterance == "[弟弟][先]暫停":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "暫停"
        pass

    if utterance == "[弟弟][先]病假":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    if utterance == "[弟弟][先]請[病假]":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請{}".format(args[2])
        pass

    if utterance == "[弟弟][先]請假":
        resultDICT["intentLIST"].append("day_off")
        infoDICT = articut.parse(inputSTR, level = "lv3")
        try:
            resultDICT["day_off"]["CancelTimeText"] = infoDICT["time"][-1][-1]["text"]
            resultDICT["day_off"]["CancelDate"] = str(datetime.strptime(articut.parse(resultDICT["day_off"]["CancelTimeText"], level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
        except:
            resultDICT["day_off"]["CancelTimeText"] = "unknown"
            resultDICT["day_off"]["CancelDate"] ="unknown"
        resultDICT["day_off"]["Course/Student"] = args[0]
        resultDICT["day_off"]["CancelKeyword"] = "請假"
        pass

    return resultDICT