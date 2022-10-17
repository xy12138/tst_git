# -*- coding:utf-8 -*-
'''
本期：

介绍market模块 的使用。
NOTE:1,aioquant只支持全仓模式，不支持逐仓模式。2,空单时候，quantity = "-10"

视频中参考代码节点：
26.13
27.40

'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 13th tutorial')
    from strategy.strategy13 import Strategy13

    Strategy13()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial13/config.json"
    quant.start(config_file,entrance_function)