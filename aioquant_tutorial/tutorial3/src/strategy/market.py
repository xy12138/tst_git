# -*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant.tasks import SingleTask
from aioquant.platform.binance import BinanceRestAPI

class MyMarket:
    def __init__(self):
        access_key =''
        secret_key =''
        self._rest_api=BinanceRestAPI(access_key=access_key,secret_key=secret_key)
            
        # SingleTask.run(self.get_binance_kline)
        # SingleTask.run(self.get_binance_trade)
        SingleTask.run(self.get_binance_orderbook)
                       
    async def get_binance_kline(self):
        # ""获取币安的K线数据""
        symbol="EOSUSDT"
        success,error=await self._rest_api.get_kline(symbol,limit=10)
        
    async def get_binance_trade(self):
        # ""获取币安的逐笔成交数据"
        symbol="EOSUSDT"
        success,error=await self._rest_api.get_trade(symbol,20)
    async def get_binance_orderbook(self):
        # "w"获取市安的订单薄数据"
        symbol="EOSUSDT"
        success,error=await self._rest_api.get_orderbook(symbol,20)