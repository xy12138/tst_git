# -*- coding:utf-8 -*-
'''
本期：

介绍position模块 的使用。
NOTE:okex不能同时持 多/空 仓。


视频中参考代码节点：38.37

'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 14th tutorial')
    from aioquant_tutorial.tutorial14.src.strategy.strategy14 import Strategy14

    Strategy14()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial14/config.json"
    quant.start(config_file,entrance_function)