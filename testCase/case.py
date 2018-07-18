# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:15
# @Author  :
# @File    : case.py
from Interface.testFengzhuang import TestApi
from  Public.get_excel import makedata

from  Public.log import run_log as logger
from config import path



from Public.panduan import assert_in
logger.info('测试数据')
def testinterface():


    datas, id, key, content, url, name, fangshi, qiwang, ids, keys, contents, urls, names, fangshis, qiwangs=makedata(path.casedatapath)

    passs = 0
    fails = 0
    jsons = []
    relusts=[]
    weizhis=0
    exptions=0
    import  json
    print(len(datas))
    print(ids)
    print(fangshis)
    print(fangshi)
    # print(len(ids))
    # for i in range(len(json.loads(datas))):
    for i in range(len(datas)):

        api = TestApi(url, key, content, fangshi)


        apijson = api.getJson()
        print(apijson)
        if apijson['code'] == 0:
            logger.info('请求:%s, url:%s ,返回:%s,预期:%s' % (content, url, apijson, qiwang))
            assert_re = assert_in(qiwangjson=qiwang, resjson=apijson)
            if assert_re['code'] == 0:
                jsons.append(apijson['result'])
                relusts.append('pass')
                passs += 1
            elif assert_re['code'] == 1:
                fails += 1
                relusts.append('fail')
                jsons.append(apijson['result'])
            elif assert_re['code'] == 2:
                exptions += 1
                relusts.append('exception')
                jsons.append(assert_re['result'])
            else:
                weizhis += 1
                relusts.append('未知错误')
                jsons.append('未知错误')
        else:
            exptions += 1
            relusts.append('exception')
            jsons.append(apijson['result'])
            continue
    return relusts, fails, passs, jsons, exptions, weizhis

# if __name__ == '__main__':
#  testinterface()