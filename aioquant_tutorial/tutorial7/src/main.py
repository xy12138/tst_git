# -*- coding:utf-8 -*-
'''
本期：
介绍config模块

参考代码时间点：
'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 7th tutorial')
    from strategy.strategy07 import Strategy07

    Strategy07()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial7/config.json"
    quant.start(config_file,entrance_function)