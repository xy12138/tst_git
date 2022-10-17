# -*- coding:utf-8 -*-

'''
本期：
1,用了wss进行连接
2,优化报错。换成回调函数on_error_callback
3,使用trade模块将现货,期货等所有交易类型全部统一化
4,使用order,回调订单状态
'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 5th tutorial')
    from strategy.strategy05 import Strategy05
    Strategy05()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial5/config.json"
    quant.start(config_file,entrance_function)