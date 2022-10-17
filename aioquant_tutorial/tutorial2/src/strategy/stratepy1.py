# -*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.path.abspath('/bisic_python'))
# print(sys.path)

from aioquant.utils import logger
from aioquant.platform.binance import BinanceRestAPI
from aioquant.tasks import SingleTask

class FirstStrategy: 
    
    def __init__(self):
        access_key = 'NCTtd1PSspmLWZGQz686GezjfqafpRO9S9nnuHgCVvvxY9L7JnZWPxoZqp0qlHO6'
        secret_key = "IFVfrsk3whCZr6ZTKEBnn0DXSyNkZ5vRWzg3BQcm6dHFcXhh4NukODEaTybwUxML"
        self._rest_api = BinanceRestAPI(access_key=access_key,secret_key=secret_key)
        SingleTask.run(self.get_asset_information)
        # SingleTask.run(self.create_new_order)
        # SingleTask.run(self.revoke)
        
    async def get_asset_information(self):
        '''获取账户资产'''
        success, error = await self._rest_api.get_user_account()
        logger.info('success',success, caller=self)
        logger.info('error',error, caller=self)
    
    async def create_new_order(self):
        '''下单'''
        symbol = 'EOSUSDT'
        action = 'BUY'
        price = '0.9'
        quantity = '30'
        success, error = await self._rest_api.create_order(action=action,symbol=symbol,price=price,quantity=quantity)
        logger.info('success',success, caller=self)
        logger.info('error',error, caller=self)
        
        
    async def revoke(self):
        '''撤销订单'''
        symbol = 'EOSUSDT'
        order_id = '3254361627'
        success, error = await self._rest_api.revoke_order(symbol=symbol,order_id=order_id)
        logger.info('success',success, caller=self)
        logger.info('error',error, caller=self)