# -*- coding: utf-8 -*-
# @Author  : leizi
from  testCase.ddt_case import MyTest
import  unittest,os
from Public import  BSTestRunner
from config import time,path
# from  Public.Dingtalk import send_ding
if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    file = os.path.join(path.reportpath, (time.ctime + '.html'))
    re_open = open(file, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='pc站点接口测试报告', description='测试结果')
    m=runner.run(suite)
    # contec = 'http接口自动化测试完成，测试通过:%s,测试失败：%s，未知错误：%s,详情见：%s' % (m.success_count,m.failure_count, m.error_count,file)
    # send_ding(content=contec)