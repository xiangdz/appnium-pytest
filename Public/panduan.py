# -*- coding: utf-8 -*-
# @Date    : 2017-08-02 21:54:08
# @Author  :
from Public.fengzhuang_dict import res

from Public.log import run_log as logger

logger.info('测试结果断言1')
def assert_in(qiwangjson,resjson):
    if len(qiwangjson.split('=')) > 1:
        data = qiwangjson.split('&')
        result = dict([(item.split('=')) for item in data])
        value1=([(str(res(resjson,key))) for key in result.keys()])
        value2=([(str(value)) for value in result.values()])
        if value1==value2:
            return  { 'code':0,"result":'pass'}
        else:
            return {'code':1,'result':'fail'}
    else:
        logger.info('测试预期值1')
        return  {"code":2,'result':'测试预期值返回1'}
logger.info('测试结果断言2')
def assertre(qiwangjson):
    if len(qiwangjson.split('=')) > 1:
        data = qiwangjson.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        logger.info('测试预期值2')
        try:
           raise {"code":1,'result':'测试预期值2'}
        except:
           return "测试预期值返回2"


# if __name__ == '__main__':
