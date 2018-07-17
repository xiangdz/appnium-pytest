# -*- coding: utf-8 -*-
# @Author  :
from  testCase.ddt_case import MyTest
import  unittest
from Public import  BSTestRunner
from config import path
if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(MyTest))
    re_open = open(path.reporthtmlpath, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title='接口测试报告', description='测试结果')
    m=runner.run(suite)
