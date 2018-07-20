# encoding: utf-8
"""
@author: cxq
@file: create_report.py
@time: 2018/7/16 12:27
"""

import xlrd
from Public.log  import LOG,logger

from config import path

file = xlrd.open_workbook(path.casedatapath)

me = file.sheets()[0]
nrows = me.nrows
ids = []
keys = []
datas=[]

for i in range(1, 2):
    ids.append(int(me.cell(i, 0).value))
    # ids.append(int(me.cell(i, 0).value))
    keys.append(me.cell(i, 1).value)
for i in range(1, 2):
    datas[i]=[ids[i], keys[i]]


    datas.append(datas[i])

print(datas)

print(nrows)
print(ids)



