# encoding: utf-8
"""
@author: cxq
@file: create_report.py
@time: 2018/7/16 12:27
"""
from Public.log import LOG,logger
@logger('保存测试结果')
def save_result(testtime,toial,passnum,fail):
    try:
        f=open('result.txt','a')
        f.write("%s= %s=%s=%s \n"%(testtime,toial,passnum,fail))
        f.close()
    except:
        LOG.info('保存测试失败原因：%s'%Exception)
