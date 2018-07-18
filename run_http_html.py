# -*- coding: utf-8 -*-
# @Author  :
import os
from testCase.case import testinterface
from Public.py_Html import createHtml
from Public.get_excel import makedata
from config import path
from config import time

def start_interface_html_http():
    starttime=time.ctimecuo
    datas,id, key, content, url, name, fangshi,qiwang, ids, keys, contents, urls,names, fangshis, qiwangs = makedata(path.casedatapath)

    list_relust, list_fail, list_pass, list_json,list_exption,list_weizhi = testinterface()

    if os.path.exists(path.reporthtmlpath) is False:
        os.system(r'touch %s' % path.reporthtmlpath)
    endtime=time.ctimecuo
    createHtml(titles=u'接口自动化测试报告',filepath=path.reporthtmlpath,
               starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=ids,name=names,key=keys,coneent=contents,
               url=urls,meth=fangshis,
               yuqi=qiwangs,json=list_json,relusts=list_relust,weizhi=list_weizhi,exceptions=list_exption)

if __name__ == '__main__':
    start_interface_html_http()