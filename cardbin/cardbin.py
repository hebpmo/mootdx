import json
import pickle

from stdnum import luhn

BANKBIN = pickle.load(open('card.pkl','rb'))

def cardbin(card):
    if not luhn.is_valid(card):
        print ('卡号不合法')
        return False
    key = BANKBIN.get(card[:7]) if BANKBIN.get(card[:7]) else BANKBIN.get(card[:6], None)

    if key:
        key = key.split('|')
        print({'bank':key[0],'type':key[1]})
        return {'bank':key[0],'type':key[1]}
    else:
        print('未知银行卡')
        return False

# if __name__ == '__main__':
#     cardbin('6228480402564890018')
