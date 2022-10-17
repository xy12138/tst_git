# -*- coding:utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath('/bisic_python'))
# print(sys.path)


from aioquant.utils import logger
from aioquant.tasks import SingleTask,LoopRunTask
from aioquant.platform.binance import BinanceRestAPI

class Strategy04(object):
    def __init__(self):
        access_key = 'NCTtd1PSspmLWZGQz686GezjfqafpRO9S9nnuHgCVvvxY9L7JnZWPxoZqp0qlHO6'
        secret_key = "IFVfrsk3whCZr6ZTKEBnn0DXSyNkZ5vRWzg3BQcm6dHFcXhh4NukODEaTybwUxML"
        self._rest_api = BinanceRestAPI(access_key=access_key,secret_key=secret_key)
        self._symbol = "LUNAUSDT"
        self._order_id = None
        self._price = None
        self._quantity = 4

        # SingleTask.call_later(self.create_binance_order,3)
        # SingleTask.call_later(self.revoke_binance_order,3,"3254639751")
        # SingleTask.call_later(self.get_biannce_order_list,3)
        LoopRunTask.register(self.get_binance_orderbook,2)
        
    async def get_binance_orderbook(self,*args,**kwargs):
        success,error =await self._rest_api.get_orderbook(self._symbol,10)
        logger.info("success:", success,caller=self)
        bids8 =  float(success ["bids"][8][0])
        bids10 = float(success ["bids"][9][0])
        avg_price = round((bids8 + bids10)/2,4)
        logger.info("average price:",avg_price,caller=self)
        
        if self._order_id and self._price:
            if (self._price <= bids8)and (self._price >=bids10):
                return
            
        if self._order_id:
            await self.revoke_binance_order(self._order_id)

        await self.create_binance_order(avg_price)
    
    async def create_binance_order(self,avg_price):
        action = "BUY"
        symbol = self._symbol 
        price = avg_price
        qunatity = "4"
        success,error = await self._rest_api.create_order(action,symbol,price,qunatity)
        self._order_id = str(success['orderId'])
        self._price = price
        logger.info('order_id:',self._order_id,'price:',price,caller=self)
    
    async def revoke_binance_order(self,order_id):
        # ZX：如果订单已经全部成交那么这里会报错，无法撤销订单。需要注意。
        await self._rest_api.revoke_order(self._symbol, order_id)
        logger.info('order_id:',order_id,caller=self)
        
    async def get_biannce_order_list(self):
        success,error =  await self._rest_api.get_all_orders(self._symbol)