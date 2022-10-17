# -*- coding:utf-8 -*-
'''
本期：
处理程序异常停止后，之前所挂订单。
方法一：单独写一个脚本，执行取消所有订单的操作。`
方法二：初始化时候，发现上次异常停止程序的订单，执行取消操作。

参考代码时间点：
'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 6th tutorial')
    from strategy.strategy06 import Strategy06

    Strategy06()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial6/config.json"
    quant.start(config_file,entrance_function)