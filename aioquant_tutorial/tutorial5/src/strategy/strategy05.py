# -*- coding:utf-8 -*-
from ast import Pass
import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant.const import BINANCE
from aioquant import quant
from aioquant.utils import logger
from aioquant.tasks import SingleTask,LoopRunTask
from aioquant.platform.binance import BinanceRestAPI
from aioquant.trade import Trade
from aioquant.order import Order,ORDER_STATUS_FILLED,ORDER_STATUS_PARTIAL_FILLED,ORDER_STATUS_FAILED
from aioquant.error import Error

class Strategy05(object):
    def __init__(self):
        access_key = 'NCTtd1PSspmLWZGQz686GezjfqafpRO9S9nnuHgCVvvxY9L7JnZWPxoZqp0qlHO6'
        secret_key = "IFVfrsk3whCZr6ZTKEBnn0DXSyNkZ5vRWzg3BQcm6dHFcXhh4NukODEaTybwUxML"
        self._rest_api = BinanceRestAPI(access_key=access_key,secret_key=secret_key)
        
        self._symbol = "EOSUSDT"
        self._order_id = None
        self._price = None
        self._quantity = 12
        
        self._is_ok = True
        
        params ={
        "strategy":"issue_5",
        "platform": BINANCE,
        "symbol":"EOS/USDT",
        "account":"issue5@gmail.com",
        "access_key":access_key,
        "secret_key":secret_key,
        "order_update_callback":self.on_order_update_callback,
        "init_callback":self.on_init_callback,
        "error_callback":self.on_error_callback
        }
        
        self._trade = Trade(**params)


        LoopRunTask.register(self.get_binance_orderbook,2)

                
    async def get_binance_orderbook(self,*args,**kwargs):
        
        if not self._is_ok:
            return
            
        success,error =await self._rest_api.get_orderbook(self._symbol,10)
        
        if error:
            # NOTE: 可以根据eror的不同程度，加上报警，打电话
            self._is_ok =False
            return
            
        logger.info("success:", success,caller=self)
        bids8 =  float(success ["bids"][8][0])
        bids10 = float(success ["bids"][9][0])
        avg_price = round((bids8 + bids10)/2,3)
        logger.info("average price:",avg_price,caller=self)
        
        if self._order_id and self._price:
            if (self._price <= bids8)and (self._price >=bids10):
                return
            
        if self._order_id:
            await self.revoke_binance_order(self._order_id)

        await self.create_binance_order(avg_price)
    
    async def create_binance_order(self,avg_price):
        action = "BUY"
        price = avg_price
        qunatity = "12"
        # NOTE:使用trade 模块下的crate_order 进行下单
        order_id,error = await self._trade.create_order(action=action,price=price,quantity=qunatity)
        if error:
            return
        self._order_id = order_id
        self._price = price
        logger.info('order_id:',self._order_id,'price:',price,caller=self)
    
    async def revoke_binance_order(self,order_id):
        success,error = await self._trade.revoke_order(order_id)  # NOTE:可以传入order_id列表,可以传入一个order_id。什么都不传，代表取消全部订单。
        if error:
            return
        logger.info('order_id:',order_id,caller=self)
        
    async def on_order_update_callback(self,order:Order):
        logger.info('order:',order,caller=self)
        if order.status == ORDER_STATUS_FILLED:
            # 完全对冲
            self._order_id = None
            self._price = None
            pass
        elif order.status == ORDER_STATUS_PARTIAL_FILLED:
            # 部分对冲
            pass
        
        elif order.status == ORDER_STATUS_FAILED:
            # 报警
            pass
        
        else:
            return
    
    async def on_init_callback(self,success:bool,**kwargs):
        logger.info('success:',success,caller=self)
        
    async def on_error_callback(self,error:Error,**kwargs):
        logger.info('error',error,caller=self)
        self._is_ok = error
        # NOTE: 可以根据eror的不同程度，加上报警，打电话
        quant.stop()