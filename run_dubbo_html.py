# -*- coding: utf-8 -*-
# @Author  :
import os
from testCase.dubbocase import testdubbointerface
from Public.py_Html import createHtml
from Public.get_excel import datacel
from Public.Dingtalk import send_ding
from config import path
from config import time
def start_dubbo_case():
    starttime=time.ctime
    listid, listkey, listconeent, listurl, listfangshi, listqiwang, listname = datacel(path.dubbocasedatapath)

    listrelust,list_fail,list_pass,list_json,list_exption,list_weizhi = testdubbointerface()

    if os.path.exists(path.reporthtml2path) is False:
        os.system(r'touch %s' % path.reporthtml2path)
    endtime=time.ctime
    createHtml(titles='dubbo接口自动化测试报告',filepath= path.reporthtml2path,starttime=starttime,
               endtime=endtime,passge=list_pass,fail=list_fail,
               id=listid,name=listname,key=listkey,coneent=listconeent,url=listurl,meth=listfangshi,
               yuqi=listqiwang,json=list_json,relusts=listrelust,weizhi=list_weizhi,exceptions=list_exption)
    contec='dubbo接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s'%(list_pass,list_fail,list_exption,list_weizhi,filepath)
    send_ding(content=contec)
if __name__ == '__main__':
    start_dubbo_case()