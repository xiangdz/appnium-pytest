# encoding: utf-8
"""
@author: cxq
@file: create_report.py
@time: 2018/7/16 12:27
"""
import xlrd
from Public.log import run_log as logger


logger.info('表格测试数据读取并转化')
def makedata(path):
        datas = []
        ids=[]
        keys=[]
        contents=[]
        fangshis=[]
        urls=[]
        qiwangs=[]
        names=[]
        file = xlrd.open_workbook(path)
        me = file.sheets()[0]
        nrows = me.nrows



        for i in range(1, nrows):
            id = me.cell(i, 0).value
            ids = ids.append(id)

            key = me.cell(i, 5).value
            keys = keys.append(key)

            content = me.cell(i, 4).value
            contents = contents.append(content)

            url = me.cell(i, 3).value
            urls = urls.append(url)

            name = me.cell(i, 1).value
            names = names.append(name)


            fangshi = me.cell(i, 2).value
            fangshis = fangshis.append(fangshi)

            qiwang = me.cell(i, 6).value
            qiwangs = qiwangs.append(qiwang)

            datas.append({"id": id, 'key':key,
                          'content':content, 'url': url,
                          'name': name, 'fangshi': fangshi,
                          'qiwang':qiwang})

        return datas,id,key,content,url,name,fangshi,qiwang,ids,keys,contents,urls,names,fangshis,qiwangs

