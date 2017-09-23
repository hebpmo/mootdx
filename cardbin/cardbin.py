# -*- coding: utf-8 -*-

import json
import os
import pickle

from stdnum import luhn
from .bankbin import BANKBIN

def valid(card):

    if not luhn.is_valid(card):
        return False
        
    key = BANKBIN.get(card[:7]) if BANKBIN.get(card[:7]) else BANKBIN.get(card[:6], None)

    if key:
        key = key.split('|')
        return {'bank': key[0], 'type': key[1]}
       
    return {'bank': u'未知银行卡', 'type': key[1]}