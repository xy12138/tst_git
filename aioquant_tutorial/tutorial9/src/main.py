# -*- coding:utf-8 -*-
'''
本期：
介绍服务心跳 的使用。
NOTE:视频文字介绍中说,1,服务心跳标志折程序是否还存活;2,是分布式协作的基石;3,支持协程任务的注册与执行
ZX:其中对于“2”视频中说之后会介绍,但是目前有的视频,并没说服务心跳怎么是分布式协作的基石。

'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 9th tutorial')
    from strategy.strategy09 import Strategy09_1,Strategy09_2,Strategy09_3,Strategy09_4

    Strategy09_4()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial9/config.json"
    quant.start(config_file,entrance_function)