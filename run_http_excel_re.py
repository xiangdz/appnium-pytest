# encoding: utf-8
"""
@author:
@file: run_http_excel_re.py
@time:
"""
from config import path
from config import time
from  Public.pyreport_excel import create
import os
from testCase.case import testinterface
from  Public.get_excel import datacel

# filepath = os.path.join(path.reportpath, '%s-result.xls' % time.ctime)
def start_excel_report_http():
    listid,listkey,listconeent,listurl,listfangshi,listqiwang,listname=datacel(path.casedatapath)
    listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi =testinterface()
    print(list_json)
    filepath = os.path.join(path.reportpath,'%s-result.xls'%time.ctime)
    print(os.path.exists(filepath))
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' %filepath)
    create(filename=filepath,list_fail=list_fail, list_pass=list_pass, list_json=list_json, listurls=listurl,
           listkeys=listkey,listconeents=listconeent, listfangshis=listfangshi, listqiwangs=listqiwang,
           listids=listid, listrelust=listrelust, listnames=listname)
    # contec = 'dubbo接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
    # list_pass, list_fail, list_exption, list_weizhi, filepath)
    # send_ding(content=contec)
if __name__ == '__main__':
    start_excel_report_http()