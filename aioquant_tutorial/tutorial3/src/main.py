# -*- coding:utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant

def first_market():
    print('hey 3rd tutorial')
    from strategy.market import MyMarket
    MyMarket()


if __name__ == "__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial3/config.json"
    quant.start(config_file, first_market)