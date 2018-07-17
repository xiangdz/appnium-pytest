# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  :
# @File    : case.py
from Interface.testFengzhuang import TestApi
from  Public.get_excel import datacel

from  Public.log import LOG,logger
from config import path

ids, keys, contens, fangshis, names, qiwangs, urls = datacel(path.casedatapath)

from Public.panduan import assert_in
@logger('测试cxq')
def testinterface():
    datacel(path.casedatapath)
    passs = 0
    fails = 0
    jsons = []
    relusts=[]
    weizhis=0
    exptions=0

    for i in range(len(urls)):
        url = urls[i]
        key = keys[i]
        connent = contens[i]
        fangshi = fangshis[i]
        qiwang=qiwangs[i]
        api=TestApi(url,key,connent,fangshi)

        apijson=api.getJson()
        if apijson['code']==0:
            LOG.info('请求:%s, url:%s ,返回:%s,预期:%s'%(connent,url,apijson,qiwang))
            assert_re=assert_in(qiwangjson=qiwang,resjson=apijson)
            if assert_re['code']==0:
                jsons.append(apijson['result'])
                relusts.append('pass')
                passs += 1
            elif assert_re['code']==1:
                fails+=1
                relusts.append('fail')
                jsons.append(apijson['result'])
            elif assert_re['code']==2:
                exptions+=1
                relusts.append('exception')
                jsons.append(assert_re['result'])
            else:
                weizhis+=1
                relusts.append('未知错误')
                jsons.append('未知错误')
        else:
            exptions += 1
            relusts.append('exception')
            jsons.append(apijson['result'])
            continue
    return  relusts,fails,passs,jsons,exptions,weizhis

if __name__ == '__main__':
 testinterface()