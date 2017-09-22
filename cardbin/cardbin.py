import json,os
import pickle

from stdnum import luhn

BASEDIR = os.path.dirname(os.path.realpath(__file__))
BANKBIN = pickle.load(open(os.path.join(BASEDIR, 'cardbin.pkl'), 'rb'))

def cardbin(card):
    if not luhn.is_valid(card):
        return False
        
    key = BANKBIN.get(card[:7]) if BANKBIN.get(card[:7]) else BANKBIN.get(card[:6], None)

    if key:
        key = key.split('|')
        return {'bank': key[0], 'type': key[1]}
    else:
        return {'bank': '未知银行卡', 'type': key[1]}

# if __name__ == '__main__':
#     cardbin('6228480402564890018')
