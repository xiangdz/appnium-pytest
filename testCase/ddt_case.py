"""
@author:
@file: case.py
@time: 2018/3/29 12:47
"""
from Interface.testFengzhuang import TestApi
from  Public.get_excel import makedata
from  Public.log import LOG
from Public.panduan import assertre
import ddt,unittest
from config import path

@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        LOG.info('测试用例开始执行')
    def tearDown(self):
        LOG.info('测试用例执行完毕')

    dataall = makedata(path.casedatapath)

    @ddt.data(*dataall)
    def test_api(self,dataall):
        url = dataall['url']
        key = dataall['key']
        canshu = dataall['content']
        fangshi = dataall['fangshi']
        api = TestApi(url, key, canshu, fangshi)
        LOG.info('读取请求参数：url:%s,key:%s,canshu:%s,postorget:%s'%(url,key,canshu,fangshi))

        resjson = api.getJson()

        LOG.info('返回结果:%s'%resjson)
        qingwang=assertre(qiwangjson=dataall['qiwang'])
        self.assertNotEqual(qingwang,resjson,msg='预期和返回不一致')
# if __name__ == '__main__':
#
#     suite = unittest.TestSuite()
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
#     suite.run()


