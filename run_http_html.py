# -*- coding: utf-8 -*-
# @Author  : leizi
import os
from testCase.case import testinterface
from Public.py_Html import createHtml
from Public.get_excel import datacel
from config import path
from config import time

def start_interface_html_http():
    starttime=time.ctimecuo

    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path.casedatapath)
    listrelust, list_fail, list_pass, list_json,list_exption,list_weizhi = testinterface()

    if os.path.exists(path.reporthtmlpath) is False:
        os.system(r'touch %s' % path.reporthtmlpath)
    endtime=time.ctimecuo
    createHtml(titles=u'接口自动化测试报告',filepath=path.reporthtmlpath,
               starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust,weizhi=list_weizhi,exceptions=list_exption)

# if __name__ == '__main__':
#     start_interface_html_http()