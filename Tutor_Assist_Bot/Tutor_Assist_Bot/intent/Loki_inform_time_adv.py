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
from ArticutAPI import Articut
import os
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_inform_time_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"線上":["線上"],"連假":["連假"],"進班":["進班"],"遠距":["遠距"],"小時半":["小時半"],"面對面":["面對面"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_inform_time_adv:
        print("[inform_time_adv] {} ===> {}".format(inputSTR, utterance))


def getAdvArgs(utterance, inputSTR, groupIndexLIST):
    url = "https://api.droidtown.co/Loki/API/"
    username    = accountDICT["username"]
    articut_key = accountDICT["articut_key"]
    loki_key    = accountDICT["loki-key"]
    payload = {                                                        # 這段範例程式在：https://api.droidtown.co/document/?python#Loki_7
        "username" : username,
        "loki_key" : loki_key,
        "input_str": utterance
    }
    response = post(url, json=payload).json()
    if response["status"] == True:
        articut = Articut(username, articut_key)                      # 由於我已在 Loki 網頁裡把我要的 args 位置用圓括號括起來 (見附圖一)，所以它會被列入 patGroups 之一
        articutResultDICT = articut.parse(inputSTR)
        pat = re.compile(response["results"][0]["pattern"])
        #print(pat)
        #print(articutResultDICT["result_pos"][0])
        patGroups = re.search(pat, articutResultDICT["result_pos"][0])
        args = []
        for i in groupIndexLIST:                                      
            args.append(patGroups.group(i))
        return (response["status"], args)
    else:
        return (response["status"], response["msg"])


def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "8-10":
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
        if len(inputSTR) >=7:
            pass
        else:
            resultDICT["intentLIST"].append("inform_time")
            resultDICT["inform_time_date"] = str(datetime.strptime(articut.parse(inputSTR, level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
            resultDICT["inform_time_time"] = str(articut.parse(inputSTR, level = "lv3")["time"][0][0]["text"])

    if utterance == "八月十六日的5-7":
        
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