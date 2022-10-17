# -*- coding:utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath('/aioq'))
# print(sys.path)

from aioquant import quant
from aioquant.utils import logger
from aioquant.tasks import SingleTask,LoopRunTask


# ====================================================part1 :循环任务demo
# demo1: 注册一个函数，每3s运行一次。
class Strategy09_1(object):
    def __init__(self):
        LoopRunTask.register(self.do_sth_per_3s,3,'zx is niubi')
    
    async def do_sth_per_3s(self,txt,*args,**kargs):  # 把*arg去掉，后面这么写 async def do_sth_per_3s(self,txt,**kargs)  也行。
        logger.info("I'm here....",txt,caller=self)
        

# demo2: 注册一个函数，每3s运行一次,"do_sth_per_3s"总共运行4次。如果只加上return那么，运行4次后，心跳服务继续，即每1s打印一次。如果加上quant.stop()那么包括服务心跳都会停止。
class Strategy09_2(object):
    def __init__(self):
        self.count = 4
        LoopRunTask.register(self.do_sth_per_3s,3,'zx is niubi')

    
    async def do_sth_per_3s(self,txt,*args,**kargs):  # 把*arg去掉，后面这么写 async def do_sth_per_3s(self,txt,**kargs)  也行。
        if self.count <= 0:
            quant.stop()  # 如果加上quant.stop()那么包括服务心跳都会停止。
            return
        logger.info("I'm here....",txt,caller=self)
        self.count -= 1
        

# demo3: 注册一个函数，每3s运行一次,"do_sth_per_3s"总共运行4次。运行4次后，心跳服务继续，但是函数"do_sth_per_3s"不会再运行。
# 经过验证加上task.unregister(),----实际运行5次。return----实际运行4次。两个都加上，实际运行4次。 

class Strategy09_3(object):
    def __init__(self):
        self.count = 4
        self._task_id = LoopRunTask.register(self.do_sth_per_3s,3,'zx is niubi')
    
    async def do_sth_per_3s(self,txt,*args,**kargs):  # 把*arg去掉，后面这么写 async def do_sth_per_3s(self,txt,**kargs)  也行。
        if self.count <= 0:
            # LoopRunTask.unregister(self._task_id)
            return
        logger.info("I'm here....",txt,caller=self)
        self.count -= 1


# ====================================================part2 :循环任务执行的任务里，嵌套一个执行一次的程序。


class Strategy09_4(object):
    def __init__(self):
        self.count = 4
        self._task_id = LoopRunTask.register(self.do_sth_per_3s,3,'zx is niubi')
    
    async def do_sth_per_3s(self,txt,*args,**kargs):  # 把*arg去掉，后面这么写 async def do_sth_per_3s(self,txt,**kargs)  也行。
        logger.info("I'm here....",txt,caller=self)
        count = kargs['heart_beat_count']  # 这个参数在heartbeat对象的方法中，这个方法在
        # SingleTask.run(self.do_once,count)
        SingleTask.call_later(self.do_once,1,count)  # ZX:嵌套执行的程序会比服务心跳慢几毫秒。
    
    async def do_once(self,count,*args,**kargs):
        logger.info('hey,just once lol,totol count is :',count,caller =self)