"""
@author:
@file: dubbocase.py
@time: 2018/3/29 12:47
"""
from Interface.testFengzhuang import TestApi
from  Public.get_excel import makedata
from  Public.log import LOG
from Public.panduan import assertre
import ddt,unittest
dataall=makedata()
# @ddt.ddt
@ddt.ddt
class MyTest(unittest.TestCase):
    def setUp(self):
        LOG.info('测试用例开始执行')
    def tearDown(self):
        LOG.info('测试用例执行完毕')
    @ddt.data(*dataall)
    def test_api(self,dataall):
        url = dataall['url']
        key = dataall['key']
        canshu = dataall['coneent']
        fangshi = dataall['fangshi']

        api = TestApi(url, key, canshu, fangshi)

        LOG.info('url:%s,key:%s,canshu:%s,postorget:%s'%(url,key,canshu,fangshi))
        print(api.connent)

        apijson = api.getJson()
        LOG.info('返回结果:%s'%apijson)

        qingwang=assertre(asserqingwang=dataall['qiwang'])


        # zjij
        # self.assertNotEqual(dict(qingwang),dict(apijson),msg='预期和返回不一致')
        self.assertNotEqual(qingwang,apijson,msg='预期和返回不一致')
if __name__ == '__main__':


    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    suite.run()


