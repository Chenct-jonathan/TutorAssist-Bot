#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki 3.0 Template For Python3

    [URL] https://api.droidtown.co/Loki/BulkAPI/

    Request:
        {
            "username": "your_username",
            "input_list": ["your_input_1", "your_input_2"],
            "loki_key": "your_loki_key",
            "filter_list": ["intent_filter_list"] # optional
        }

    Response:
        {
            "status": True,
            "msg": "Success!",
            "version": "v223",
            "word_count_balance": 2000,
            "result_list": [
                {
                    "status": True,
                    "msg": "Success!",
                    "results": [
                        {
                            "intent": "intentName",
                            "pattern": "matchPattern",
                            "utterance": "matchUtterance",
                            "argument": ["arg1", "arg2", ... "argN"]
                        },
                        ...
                    ]
                },
                {
                    "status": False,
                    "msg": "No Match Intent!"
                }
            ]
        }
"""

from requests import post
from requests import codes
from ArticutAPI import Articut
import math
import re
import json

try:
    from intent import Loki_online_course
    from intent import Loki_class_arrangement
    from intent import Loki_physical_course
    from intent import Loki_warm_blessing
    from intent import Loki_day_off
except:
    from .intent import Loki_online_course
    from .intent import Loki_class_arrangement
    from .intent import Loki_physical_course
    from .intent import Loki_warm_blessing
    from .intent import Loki_day_off


LOKI_URL = "https://api.droidtown.co/Loki/BulkAPI/"
accountDICT = json.load(open("account.info",encoding="utf-8"))
USERNAME = accountDICT["username"]
LOKI_KEY = accountDICT["loki-key"]
# 意圖過濾器說明
# INTENT_FILTER = []        => 比對全部的意圖 (預設)
# INTENT_FILTER = [intentN] => 僅比對 INTENT_FILTER 內的意圖
INTENT_FILTER = []
INPUT_LIMIT = 20

class LokiResult():
    status = False
    message = ""
    version = ""
    balance = -1
    lokiResultLIST = []

    def __init__(self, inputLIST, filterLIST):
        self.status = False
        self.message = ""
        self.version = ""
        self.balance = -1
        self.lokiResultLIST = []
        # filterLIST 空的就採用預設的 INTENT_FILTER
        if filterLIST == []:
            filterLIST = INTENT_FILTER

        try:
            result = post(LOKI_URL, json={
                "username": USERNAME,
                "input_list": inputLIST,
                "loki_key": LOKI_KEY,
                "filter_list": filterLIST
            })

            if result.status_code == codes.ok:
                result = result.json()
                self.status = result["status"]
                self.message = result["msg"]
                if result["status"]:
                    self.version = result["version"]
                    self.balance = result["word_count_balance"]
                    self.lokiResultLIST = result["result_list"]
            else:
                self.message = "{} Connection failed.".format(result.status_code)
        except Exception as e:
            self.message = str(e)

    def getStatus(self):
        return self.status

    def getMessage(self):
        return self.message

    def getVersion(self):
        return self.version

    def getBalance(self):
        return self.balance

    def getLokiStatus(self, index):
        rst = False
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["status"]
        return rst

    def getLokiMessage(self, index):
        rst = ""
        if index < len(self.lokiResultLIST):
            rst = self.lokiResultLIST[index]["msg"]
        return rst

    def getLokiLen(self, index):
        rst = 0
        if index < len(self.lokiResultLIST):
            if self.lokiResultLIST[index]["status"]:
                rst = len(self.lokiResultLIST[index]["results"])
        return rst

    def getLokiResult(self, index, resultIndex):
        lokiResultDICT = None
        if resultIndex < self.getLokiLen(index):
            lokiResultDICT = self.lokiResultLIST[index]["results"][resultIndex]
        return lokiResultDICT

    def getIntent(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["intent"]
        return rst

    def getPattern(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["pattern"]
        return rst

    def getUtterance(self, index, resultIndex):
        rst = ""
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["utterance"]
        return rst

    def getArgs(self, index, resultIndex):
        rst = []
        lokiResultDICT = self.getLokiResult(index, resultIndex)
        if lokiResultDICT:
            rst = lokiResultDICT["argument"]
        return rst

def runLoki(inputLIST, filterLIST=[]):
    # 將 intent 會使用到的 key 預先設爲空列表
    resultDICT = {
        "intentLIST":[],
       #"key": []
    }
    lokiRst = LokiResult(inputLIST, filterLIST)
    if lokiRst.getStatus():
        for index, key in enumerate(inputLIST):
            for resultIndex in range(0, lokiRst.getLokiLen(index)):
                # online_course
                if lokiRst.getIntent(index, resultIndex) == "online_course":
                    resultDICT = Loki_online_course.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # class_arrangement
                if lokiRst.getIntent(index, resultIndex) == "class_arrangement":
                    resultDICT = Loki_class_arrangement.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # physical_course
                if lokiRst.getIntent(index, resultIndex) == "physical_course":
                    resultDICT = Loki_physical_course.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # warm_blessing
                if lokiRst.getIntent(index, resultIndex) == "warm_blessing":
                    resultDICT = Loki_warm_blessing.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

                # day_off
                if lokiRst.getIntent(index, resultIndex) == "day_off":
                    resultDICT = Loki_day_off.getResult(key, lokiRst.getUtterance(index, resultIndex), lokiRst.getArgs(index, resultIndex), resultDICT)

    else:
        resultDICT = {"msg": lokiRst.getMessage()}
    return resultDICT

def execLoki(content, filterLIST=[], splitLIST=[]):
    """
    input
        content       STR / STR[]    要執行 loki 分析的內容 (可以是字串或字串列表)
        filterLIST    STR[]          指定要比對的意圖 (空列表代表不指定)
        splitLIST     STR[]          指定要斷句的符號 (空列表代表不指定)
                                     * 如果一句 content 內包含同一意圖的多個 utterance，請使用 splitLIST 切割 content

    output
        resultDICT    DICT           合併 runLoki() 的結果，請先設定 runLoki() 的 resultDICT 初始值

    e.g.
        splitLIST = ["！", "，", "。", "？", "!", ",", "
", "；", "　", ";"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？")                      # output => ["今天天氣"]
        resultDICT = execLoki("今天天氣如何？後天氣象如何？", splitLIST=splitLIST) # output => ["今天天氣", "後天氣象"]
        resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"])                # output => ["今天天氣", "後天氣象"]
    """
    contentLIST = []
    if type(content) == str:
        contentLIST = [content]
    if type(content) == list:
        contentLIST = content

    resultDICT = {}
    if contentLIST:
        if splitLIST:
            # 依 splitLIST 做分句切割
            splitPAT = re.compile("[{}]".format("".join(splitLIST)))
            inputLIST = []
            for c in contentLIST:
                tmpLIST = splitPAT.split(c)
                inputLIST.extend(tmpLIST)
            # 去除空字串
            while "" in inputLIST:
                inputLIST.remove("")
        else:
            # 不做分句切割處理
            inputLIST = contentLIST

        # 依 INPUT_LIMIT 限制批次處理
        for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
            lokiResultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)
            if "msg" in lokiResultDICT:
                return lokiResultDICT

            # 將 lokiResultDICT 結果儲存至 resultDICT
            for k in lokiResultDICT:
                if k not in resultDICT:
                    resultDICT[k] = []
                resultDICT[k].extend(lokiResultDICT[k])

    return resultDICT

def testLoki(inputLIST, filterLIST):
    INPUT_LIMIT = 20
    for i in range(0, math.ceil(len(inputLIST) / INPUT_LIMIT)):
        resultDICT = runLoki(inputLIST[i*INPUT_LIMIT:(i+1)*INPUT_LIMIT], filterLIST)

    if "msg" in resultDICT:
        print(resultDICT["msg"])

def testIntent():
    # online_course
    print("[TEST] online_course")
    inputLIST = ['先用線上','先用視訊','先恢復線上','先恢復視訊','先改成線上','先改成視訊','先維持線上','先維持視訊','先調整為線上','先調整為視訊']
    testLoki(inputLIST, ['online_course'])
    print("")

    # class_arrangement
    print("[TEST] class_arrangement")
    inputLIST = ['改8.','改到8.','15.好嗎','改八點','延後到8.','提早到8.','15.你ok 嗎','七點好嗎','改到八點','15.老師ok嗎','三點你ok嗎','15.你方便嗎','延後到八點','延後半小時','提早到八點','提早半小時','三點老師ok嗎','五點你可以嗎','五點你方便嗎','可以改時間嗎','五點老師可以嗎','五點老師方便嗎','需要調整時間嗎','可以改上課時間嗎','禮拜天可以幫XX上課嗎']
    testLoki(inputLIST, ['class_arrangement'])
    print("")

    # physical_course
    print("[TEST] physical_course")
    inputLIST = ['先實體','先到府上課','先到班上課','先恢復到府','先恢復實體','先恢復進班','先改回到府','先改回實體','先改回進班','先進班上課','先恢復面對面','先改回面對面','先面對面上課','先恢復實體課程','先改回實體課程']
    testLoki(inputLIST, ['physical_course'])
    print("")

    # warm_blessing
    print("[TEST] warm_blessing")
    inputLIST = ['祝你','祝老師','假期快樂','假期愉快','中秋節快樂','中秋節愉快']
    testLoki(inputLIST, ['warm_blessing'])
    print("")

    # day_off
    print("[TEST] day_off")
    inputLIST = ['XX先休息','XX先停課','XX先暫停','XX先請假','先不用來','XX先請病假','先讓XX休息','先讓XX停課','先讓XX暫停','先讓XX請假','今天先休息','今天先停課','今天先暫停','今天先病假','今天先請假','今天請病假','先不上課喔','弟弟先休息','弟弟先停課','弟弟先暫停','弟弟先請假','先不用過來喔','先讓弟弟休息','先讓弟弟停課','先讓弟弟暫停','先讓弟弟請假','弟弟先請病假','先不用幫XX上課','先不用幫弟弟上課']
    testLoki(inputLIST, ['day_off'])
    print("")


if __name__ == "__main__":
    # 測試所有意圖
    #testIntent()

    # 測試其它句子
    #filterLIST = []
    #splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"]
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST)            # output => ["今天天氣"]
    #resultDICT = execLoki("今天天氣如何？後天氣象如何？", filterLIST, splitLIST) # output => ["今天天氣", "後天氣象"]
    #resultDICT = execLoki(["今天天氣如何？", "後天氣象如何？"], filterLIST)      # output => ["今天天氣", "後天氣象"]
    resultDICT=runLoki(["牽縈的同學確診了，安全起見，我們都先用視訊上課好嗎!"])
    #for key, value in resultDICT.items():
        #print(key, ' : ', value)
        
    print("\n感謝您通知")
    print(resultDICT)    