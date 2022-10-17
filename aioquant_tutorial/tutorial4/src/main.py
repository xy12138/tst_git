# -*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 4th tutorial')
    from strategy.strategy04 import Strategy04
    Strategy04()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial4/config.json"
    quant.start(config_file,entrance_function)