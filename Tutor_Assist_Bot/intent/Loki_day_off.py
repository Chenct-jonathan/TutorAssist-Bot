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
import os

DEBUG_day_off = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_day_off:
        print("[day_off] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[xx][今天][先]休息":
        # write your code here
        pass

    if utterance == "[xx][今天][先]休息 [一次]":
        # write your code here
        pass

    if utterance == "[xx][今天][先]暫停":
        # write your code here
        pass

    if utterance == "[xx][今天][先]暫停[一次]":
        # write your code here
        pass

    if utterance == "[xx][今天][先]請假":
        # write your code here
        pass

    if utterance == "[xx][今天][先]請假[一次]":
        # write your code here
        pass

    if utterance == "[xx][今天]休息":
        # write your code here
        pass

    if utterance == "[xx][今天]休息 [一次]":
        # write your code here
        pass

    if utterance == "[xx][今天]暫停[一次]":
        # write your code here
        pass

    if utterance == "[xx][今天]請假":
        # write your code here
        pass

    if utterance == "[xx][今天]請假[一次]":
        # write your code here
        pass

    if utterance == "[xx][先]暫停[一次]":
        # write your code here
        pass

    if utterance == "[xx]休息":
        # write your code here
        pass

    if utterance == "[xx]休息 [一次]":
        # write your code here
        pass

    if utterance == "[xx]暫停[一次]":
        # write your code here
        pass

    if utterance == "[xx]請假":
        # write your code here
        pass

    if utterance == "[xx]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天][xx][先]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天][xx][先]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天][xx][先]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天][xx]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天][xx]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天][xx]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天][他][先]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天][他]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天][先]不用來幫[xx]上課喔":
        # write your code here
        pass

    if utterance == "[今天][先]不用幫[xx]上課喔":
        # write your code here
        pass

    if utterance == "[今天][先]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天][先]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天][先]給[xx]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天][先]給[xx]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天][先]給[xx]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天][先]給[他]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天][先]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天][先]讓[xx]休息":
        # write your code here
        pass

    if utterance == "[今天][先]讓[xx]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天][先]讓[xx]暫停 [一次]":
        # write your code here
        pass

    if utterance == "[今天][先]讓[xx]請假":
        # write your code here
        pass

    if utterance == "[今天][先]讓[xx]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天][先]讓[他]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天][老師][先]不用來喔":
        # write your code here
        pass

    if utterance == "[今天][老師]不用來喔":
        # write your code here
        pass

    if utterance == "[今天][老師]不用來幫[xx]上課喔":
        # write your code here
        pass

    if utterance == "[今天]不用來喔":
        # write your code here
        pass

    if utterance == "[今天]不用來幫[xx]上課喔":
        # write your code here
        pass

    if utterance == "[今天]休息":
        # write your code here
        pass

    if utterance == "[今天]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天]暫停":
        # write your code here
        pass

    if utterance == "[今天]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天]給[xx][先]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天]給[xx][先]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天]給[xx]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天]給[xx]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天]給[xx]請假":
        # write your code here
        pass

    if utterance == "[今天]給[xx]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天]給[他]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天]請假":
        # write your code here
        pass

    if utterance == "[今天]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天]讓[xx][先]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天]讓[xx][先]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天]讓[xx]休息 [一次]":
        # write your code here
        pass

    if utterance == "[今天]讓[xx]暫停[一次]":
        # write your code here
        pass

    if utterance == "[今天]讓[xx]請假[一次]":
        # write your code here
        pass

    if utterance == "[今天]讓[他]暫停[一次]":
        # write your code here
        pass

    if utterance == "[他][先]暫停[一次]":
        # write your code here
        pass

    if utterance == "[他]暫停[一次]":
        # write your code here
        pass

    if utterance == "[老師][今天][先]不用來喔":
        # write your code here
        pass

    if utterance == "[老師][今天][先]不用來幫[xx]上課喔":
        # write your code here
        pass

    if utterance == "[老師][今天][先]不用幫[xx]上課喔":
        # write your code here
        pass

    if utterance == "[老師][今天]不用來喔":
        # write your code here
        pass

    if utterance == "[老師][今天]不用來幫[xx]上課喔":
        # write your code here
        pass

    if utterance == "[老師][今天]不用幫[xx]上課喔":
        # write your code here
        pass

    if utterance == "[老師]不用[過]來喔":
        # write your code here
        pass

    if utterance == "[老師]不用來喔":
        # write your code here
        pass

    return resultDICT