#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json
import re
from datetime import datetime
from pprint import pprint

from Tutor_Assist_Bot import runLoki

logging.basicConfig(level=logging.DEBUG)


with open("account.info", encoding="utf-8") as f: #讀取account.info
    accountDICT = json.loads(f.read())

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    resultDICT = runLoki(inputLIST, filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

class BotClient(discord.Client):
    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = self.templateDICT
        templateDICT["updatetime"] = datetime.now()
        return templateDICT

    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))
        ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                            "latestQuest": "",
                            "msgSTR":""#,
                            #"replySTR":""
                            
               }
        self.mscDICT = { #userid:templateDICT
               }
               # ####################################################################################
        

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None
        elif message.content.lower().replace(" ", "") in ("bot點名"):
            await message.reply("有！")

        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            elif msgSTR.lower() in ["哈囉","嗨","你好","您好","hi","hello"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "嗨嗨，我們好像見過面，但卓騰的隱私政策不允許我記得你的資料，抱歉！"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[message.author.id]["latestQuest"] 
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = "您好，我是Bot Assistant，我會在老師不在時幫忙處理課程異動事宜喔!(現在尚無法處理課程時間異動問題)"#msgSTR.title()

# ##########非初次對話：這裡用 Loki 計算語意
            else: #開始處理正式對話
                #從這裡開始接上 NLU 模型
                self.mscDICT[message.author.id]["msgSTR"] = msgSTR
                resultDICT = getLokiResult(msgSTR)
                logging.debug("######\nLoki 處理結果如下：")
                logging.debug(resultDICT)
                if len(resultDICT["intentLIST"]) == 1: 
                    if "day_off" in resultDICT["intentLIST"]:
                        if resultDICT["day_off"]['CancelTimeText']== "unknown":
                            replySTR= "不好意思，您什麼時間要請假呢?"
                            
                        elif resultDICT["day_off"]['CancelKeyword']== "unknown":
                            replySTR= "不好意思，您想要請假對嗎?"
                        else:
                            replySTR = "您好，跟您確認一下時間喔!\n{}{}對嗎?\n確切日期: {}".format(resultDICT["day_off"]['CancelTimeText'], resultDICT["day_off"]['CancelKeyword'], resultDICT["day_off"]['CancelDate'])
                    elif "warm_blessing" in resultDICT["intentLIST"]:
                        if resultDICT["warm_blessing"]["Holiday"] == "unknown":
                            replySTR = "謝謝您的祝福! 祝您事事順心!"
                        else: 
                            replySTR = "謝謝您的祝福!也祝您{}快樂喔!".format(resultDICT["warm_blessing"]["Holiday"])
                    elif "physical_course" in resultDICT["intentLIST"]:
                        replySTR = "好的，下次課程恢復實體喔!"
                    elif "online_course" in resultDICT["intentLIST"]:
                        replySTR = "好的，下次課程改為線上喔!"
                else:
                    replySTR ="感謝您的告知，我已轉告老師，為保險起見，會請老師看過後盡速跟您確認喔!"
        await message.reply(replySTR)


if __name__ == "__main__":
    client = BotClient()
    client.run(accountDICT["discord_token"])