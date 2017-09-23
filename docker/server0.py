#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zerorpc
from cardbin import cardbin

class RPCServer(object):
    def check(self, num):
        return cardbin(num)

if __name__ == '__main__':
    s = zerorpc.Server(RPCServer())
    s.bind("tcp://0.0.0.0:4242")
    s.run()
