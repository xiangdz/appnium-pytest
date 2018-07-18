"""
@author:
@file: case.py
@time: 2018/3/29 12:47
"""
from Interface.testFengzhuang import TestApi
from  Public.get_excel import makedata
from Public.log import run_log as logger

from Public.panduan import assertre
import ddt,unittest
from config import path

@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        logger.info('测试用例开始执行')
    def tearDown(self):
        logger.info('测试用例执行完毕')


    # @ddt.data(*dataall)
    def test_api(self):
        datas, id, key, content, url, name, fangshi, qiwang, ids, keys, contents, urls, names, fangshis, qiwangs = makedata(path.casedatapath)

        api = TestApi(url, key, content, fangshi)
        logger.info('读取请求参数：url:%s,key:%s,canshu:%s,postorget:%s'%(url,key,content,fangshi))

        resjson = api.getJson()

        logger.info('返回结果:%s'%resjson)
        qingwang=assertre(qiwangjson=qiwang)
        self.assertNotEqual(qingwang,resjson,msg='预期和返回不一致')
if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    suite.run()


