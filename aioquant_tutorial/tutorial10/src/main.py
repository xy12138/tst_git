# -*- coding:utf-8 -*-
'''
本期：

介绍order模块 的使用。
NOTE:交易所中各种各样的订单类型，其实都可以转化为限价单，市价单。这两种 几行代码就可以转化。

视频中参考代码节点：

'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 10th tutorial')
    from strategy.strategy10 import Strategy10

    Strategy10()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial10/config.json"
    quant.start(config_file,entrance_function)