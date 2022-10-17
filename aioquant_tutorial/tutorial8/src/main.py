# -*- coding:utf-8 -*-
'''
本期：
使用log模块

{
    "LOG":{
        "console":true,
        "level":"INFO",
        "path":"var/log/servers/aioquant",
        "name":"quant.log",
        "clear":true,
        "backup_count":5
        }

}

console boolean是否打印到控制台，true打印到控制台/false打印到文件，可选，默认为true
level string日志打印级别DEBUG/INFo,可选，默认为DEBUG
path string日志存储路径，可选，默认为/var/1og/servers./aioquant
name string日志文件名，可选，默认为quant.log
clear boolean初始化的时候，是否清理之前的日志文件，true清理/false不清理，可选，默认为false
backup_.count int保存按天分割的日志文件个数，默认O为永久保存所有日志文件，可选，默认为0

'''

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant


def entrance_function():
    print('hey 8th tutorial')
    from strategy.strategy08 import Strategy08

    Strategy08()
    

if __name__=="__main__":
    config_file = "/aioq/aioquant_tutorial/tutorial8/config.json"
    quant.start(config_file,entrance_function)