# encoding: utf-8
"""
@author: cxq
@file: create_report.py
@time: 2018/7/16 12:27
"""

import xlrd
from Public.log  import LOG,logger


@logger('读取表格测试数据')
def datacel(path):
    try:
        file=xlrd.open_workbook(path)
        me = file.sheets()[0]
        nrows = me.nrows
        ids = []
        keys = []
        contens = []
        fangshis = []
        names = []
        qiwangs = []
        urls = []
        for i in range(1,nrows):
            ids.append(me.cell(i,0).value)
            keys.append(me.cell(i,2).value)
            contens.append(me.cell(i,3).value)
            urls.append(me.cell(i,4).value)
            names.append(me.cell(i,1).value)
            fangshis.append((me.cell(i,5).value))
            qiwangs.append((me.cell(i,6).value))
        return   ids,keys,contens,fangshis,names,qiwangs,urls
    except :LOG.info('读取表格测试数据失败，原因:%s' %Exception)

@logger('测试数据转化')
def makedata(path):
    ids, keys, contens, fangshis, names, qiwangs,urls=datacel(path)
    make_data=[]
    i=0
    for i in range(len(ids)):
        url = urls[i]
        key = keys[i]
        content = contens[i]
        fangshi = fangshis[i]
        qiwang =qiwangs[i]
        make_data.append({'url': url, 'key': key, 'content': content, 'fangshi': fangshi, 'qiwang': qiwang})
        i += 1
    return make_data

# if __name__ == '__main__':
#     path=path.casedatapath
#     aa=makedata(path)
#     print(aa)
