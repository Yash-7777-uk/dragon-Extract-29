#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6232350725:AAFFT1PF5eKJYgTtuHt_DPFrM_u9kJflals")
    API_ID = int(os.environ.get("API_ID", "23801870"))
    API_HASH = os.environ.get("API_HASH", "9645cfafdfc9be9a7a46fb4874992cf6")
    AUTH_USERS = "5620459682"

