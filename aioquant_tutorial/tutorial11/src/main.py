# -*- coding:utf-8 -*-
'''
本期：

介绍trade模块 的使用。
NOTE:重点：1，将 现货 和 期货 交易方式合并。
2，**kwargs：可以根据不同交易所的特殊情况，进行赋值。 
3，trade.revoke_order() 撤销任意的订单。
4，查看 目前未成交的订单。 trade.orders() ----这是一个本地维护为准的。 vs  trade.get_open_order_ids()----这是一个以交易所为准的。
-----前者稍微慢 几毫秒。且没有消耗rest api请求限制。

视频中参考代码节点：

'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 11th tutorial')
    from strategy.strategy11 import Strategy11

    Strategy11()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial11/config.json"
    quant.start(config_file,entrance_function)