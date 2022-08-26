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
from ArticutAPI import Articut
import re
from requests import post

accountDICT = json.load(open("account.info",encoding="utf-8"))

DEBUG_class_arrangement_adv = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"愉快":["愉快"],"線上":["線上"],"連假":["連假"],"進班":["進班"],"遠距":["遠距"],"小時半":["小時半"],"面對面":["面對面"]}

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_class_arrangement_adv:
        print("[class_arrangement_adv] {} ===> {}".format(inputSTR, utterance))
        

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
        if "class_arrangement" in resultDICT["intentLIST"]: pass
        else:
            resultDICT["class_arrangement"] = {}
            resultDICT["intentLIST"].append("class_arrangement")
            resultBOOL, args = getAdvArgs(utterance, inputSTR, [3])     # 利用 pythex 一類的網頁工具，我知道我要抓的 args 位置在第 10 個 group (見附圖二)。故 groupIndexLIST 裡放了 [10]
            if resultBOOL == True:
                resultDICT["class_arrangement"]["AlterTime"] = "".join(args)
            else:
                resultDICT["error_msg"] = utterance

    if utterance == "3-5ok嗎":
        if "class_arrangement" in resultDICT["intentLIST"]: pass
        else:
            resultDICT["class_arrangement"] = {}
            resultBOOL, args = getAdvArgs(utterance, inputSTR, [7])     # 利用 pythex 一類的網頁工具，我知道我要抓的 args 位置在第 10 個 group (見附圖二)。故 groupIndexLIST 裡放了 [10]
            if resultBOOL == True:
                resultDICT["class_arrangement"]["AlterTime"].extend(args)
            else:
                resultDICT["error_msg"] = utterance
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