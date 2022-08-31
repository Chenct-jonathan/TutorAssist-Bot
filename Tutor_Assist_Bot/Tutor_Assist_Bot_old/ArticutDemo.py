#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from ArticutAPI import Articut
import json
import re
from datetime import datetime

accountDICT = json.load(open("account.info",encoding="utf-8"))
articut = Articut(username=accountDICT["username"],apikey=accountDICT["articut_key"])

demoSTR = articut.parse("八月三十日", level = "lv3")
print(demoSTR)