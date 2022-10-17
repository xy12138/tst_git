# -*- coding:utf-8 -*-

import sys
import os

sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant

def first_strategy():
    print("i'm here...")
    from strategy.stratepy1 import FirstStrategy
    FirstStrategy()
    
          
if __name__ ==  "__main__":
    config_file = None  
    quant.start(config_file,first_strategy)