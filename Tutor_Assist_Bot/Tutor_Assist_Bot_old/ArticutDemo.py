#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import Articut
import json
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

demoSTR = articut.parse("九月三十日的十點-十二點", level = "lv3")
print(demoSTR)

print("8:30-10.".split(":"))
print("8:30-10.".split(":")[1].split("-"))