# -*- coding: utf-8 -*-
# @Date    :
# @Author  :
import  time


print(time.time())

print(time.localtime(time.time()))

print(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
from datetime import  datetime
print(datetime.now())
ctimecuo=datetime.now()
# day= time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
ctime=datetime.now().strftime("%Y%m%d%H%M%S")
print(datetime.now().strftime("%Y%m%d%H%M%S"))






