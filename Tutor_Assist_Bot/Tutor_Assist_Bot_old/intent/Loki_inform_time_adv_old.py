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
import requests

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

DEBUG_inform_time_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_asNoun":["連假","線上","進班","遠距","面對面","愉快","線下","到班","實體課程"],"_asOkay":["ok","OK","oK","Ok","Okay","okay","OKAY"],"_asTime":["小時半"],"_asVerb":["改一下","討論一下","調整一下"]}

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
    response = requests.post(url, json=payload).json()
    if response["status"] == True:
        articut = Articut(username, articut_key)                      # 由於我已在 Loki 網頁裡把我要的 args 位置用圓括號括起來 (見附圖一)，所以它會被列入 patGroups 之一
        articutResultDICT = articut.parse(inputSTR)
        pat = re.compile(response["results"][0]["pattern"])
        patGroups = re.search(pat, articutResultDICT["result_pos"][0])
        args = []
        for i in groupIndexLIST:                                      
            args.append(patGroups.group(i))
        return (response["status"], args)
    else:
        return (response["status"], response["msg"])

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["inform_time"]={}
    if utterance == "8-10":
        if len(inputSTR) > 10:
            pass
        else:
            resultBOOL, args = getAdvArgs(utterance, inputSTR, [1])     # 利用 pythex 一類的網頁工具，我知道我要抓的 args 位置在第 10 個 group (見附圖二)。故 groupIndexLIST 裡放了 [10]
        if resultBOOL == True:
            resultDICT["inform_time"]["inform_time_time"].extend(args)
        else:
            resultDICT["error_msg"] = utterance

    if utterance == "8/16的8-10":
        # write your code here
        pass

    if utterance == "8/16的8.":
        # write your code here
        pass

    if utterance == "8/16的8:00":
        # write your code here
        pass

    if utterance == "8/16的8:00-10:00":
        # write your code here
        pass

    if utterance == "8/16的八點":
        # write your code here
        pass

    if utterance == "8/16的八點到十點":
        # write your code here
        pass

    #if utterance == "9/15":
        #if len(inputSTR) > 10:
            #pass
        #else:
            #resultDICT["intentLIST"].append("inform_time")
            #resultBOOL, args = getAdvArgs(utterance, inputSTR, [0])     # 利用 pythex 一類的網頁工具，我知道我要抓的 args 位置在第 10 個 group (見附圖二)。故 groupIndexLIST 裡放了 [10]
        #if resultBOOL == True:
            #resultDICT["inform_time"]["startTime"].extend(args)
        #else:
            #resultDICT["error_msg"] = utterance

    if utterance == "八月16的8-10":
        # write your code here
        pass

    if utterance == "八月16的8.":
        # write your code here
        pass

    if utterance == "八月16的8:00":
        # write your code here
        pass

    if utterance == "八月16的8:00-10:00":
        # write your code here
        pass

    if utterance == "八月16的五點到七點":
        # write your code here
        pass

    if utterance == "八月十六日":
        if len(inputSTR) > 6:
            pass
        else:
            resultDICT["intentLIST"].append("inform_time")
            try:
                resultDICT["inform_time"]["inform_time_date"] = str(datetime.strptime(articut.parse(inputSTR, level = "lv3")["time"][0][0]["datetime"], '%Y-%m-%d %H:%M:%S').date())
                resultDICT["inform_time"]["inform_time_time"] = str(articut.parse(inputSTR, level = "lv3")["time"][0][0]["text"])
            except:
                #resultDICT["inform_time"]["inform_time_date"] = inputSTR
                resultDICT["inform_time"]["inform_time_time"] = inputSTR

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