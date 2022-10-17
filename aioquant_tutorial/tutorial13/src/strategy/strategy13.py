# -*- coding:utf-8 -*-
from ast import Pass
import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant.const import BINANCE
from aioquant import quant
from aioquant import const
from aioquant.utils import logger
from aioquant.tasks import SingleTask,LoopRunTask
from aioquant.platform.binance import BinanceRestAPI
from aioquant.trade import Trade
from aioquant.order import Order,ORDER_STATUS_FILLED,ORDER_STATUS_PARTIAL_FILLED,ORDER_STATUS_FAILED,ORDER_STATUS_CANCELED
from aioquant.error import Error
from aioquant.configure import config
from aioquant.market import Market,Orderbook
from aioquant.utils.decorator import async_method_locker

class Strategy13(object):
    def __init__(self):

        self._order_id = None
        self._price = None
        
        self._is_ok = False
        
        params ={
        "strategy":config.strategy,
        "platform": config.platform,
        "symbol":config.symbol,
        "account":config.account,
        "access_key":config.access_key,
        "secret_key":config.secret_key,
        
        "order_update_callback":self.on_order_update_callback,
        "init_callback":self.on_init_callback,
        "error_callback":self.on_error_callback
        }
        self._trade = Trade(**params)

        # 第一次参数：MARKET_TYPE_TRADE，const.MARKET_TYPE_ORDERBOOK，MARKET_TYPE_KLINE，分别对应不同的返回类型。
        Market(const.MARKET_TYPE_ORDERBOOK,const.OKEX_FUTURE, config.sysmbol,self.on_event_orderbook_update)

    
    async def on_event_orderbook_update(self,orderbook:Orderbook):
        logger.info("orderbook:",orderbook,caller=self)

        asks8 =  float(orderbook.asks[1][0])
        asks10 = float(orderbook.asks[3][0])

        await self.process(asks8,asks10)

    # NOTE:如果不使用锁，那么由于okex返回的orderbook信息太快，所以每次返回的信息都会造成一次下单。为了处理这种情况，同时降低api使用频次，需要用锁。false---每次只处理最新返回的订单，剩余的不处理。
    @async_method_locker("Strategy13.process",False)            
    async def process(self,asks8,asks10):
        avg_price = round((asks8 + asks10)/2,3)
        logger.info('avg_price:',self.avg_price,avg_price,caller=self)
        
        if self._order_id and self._price:
            if (self._price >= asks8)and (self._price <=asks10):
                return
            
        if self._order_id:
            await self.revoke_binance_order(self._order_id)

        await self.create_binance_order(avg_price)
    
    async def create_order(self,avg_price):
        # 注意这里是挂空单！！！！！！！！
        action = "SELL"
        price = avg_price
        qunatity = "-12"
        # NOTE:使用trade 模块下的crate_order 进行下单
        order_id,error = await self._trade.create_order(action=action,price=price,quantity=qunatity)
        if error:
            return
        self._order_id = order_id
        self._price = price
        logger.info('order_id:',self._order_id,'price:',price,caller=self)
    
    async def revoke_order(self,order_id):
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
        
        elif order.status == ORDER_STATUS_CANCELED:
        # 订单取消
            self._order_id = None
            self._price = None
            
        else:
            return
    
    async def on_init_callback(self,success:bool,**kwargs):
        logger.info('success:',success,caller=self)
        
        if not success:
            return
        
        success, error = await self._trade.revoke_order()
        if error:
            return
        
        self._is_ok = True

    async def on_error_callback(self,error:Error,**kwargs):
        logger.info('error',error,caller=self)
        self._is_ok = error
        # NOTE: 可以根据eror的不同程度，加上报警，打电话
        quant.stop()