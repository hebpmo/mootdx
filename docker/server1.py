#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cardbin import cardbin
from bottle import route, run

@route('/<num>')
def check(num):
    return cardbin(num)

run(host='0.0.0.0', port=8080, server='gunicorn', workers=4)

