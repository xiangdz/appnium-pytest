# encoding: utf-8
"""
@author: cxq
@file: create_report.py
@time: 2018/7/16 12:27
"""
import xlrd
from Public.log  import logger

@logger('表格测试数据读取并转化')
def makedata(path):
        datas = []
        file = xlrd.open_workbook(path)
        me = file.sheets()[0]
        nrows = me.nrows
        for i in range(1, nrows):
            datas.append({"id": me.cell(i, 0).value, 'key': me.cell(i, 2).value,
                          'content': me.cell(i, 3).value, 'url': me.cell(i, 4).value,
                          'name': me.cell(i, 1).value, 'fangshi': me.cell(i, 5).value,
                          'qiwang': me.cell(i, 6).value})
        return datas

