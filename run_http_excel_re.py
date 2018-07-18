# encoding: utf-8
"""
@author:
@file: run_http_excel_re.py
@time:
"""
from config import path

from  Public.pyreport_excel import create
import os
from testCase.case import testinterface
from  Public.get_excel import makedata

def start_excel_report_http():

    ids, keys, contens, fangshis, names, qiwangs,urls=makedata(path.casedatapath)

    relusts, fails, passs, jsons, exptions, weizhis =testinterface()

    # if os.path.exists(path.reportxlspath) is False:
    #     os.system(r'touch %s' %path.reportxlspath)
    #
    create(path.reportxlspath,fails, passs, jsons,
           urls,keys,contens, fangshis, qiwangs,
           ids, relusts, names)
#
# if __name__ == '__main__':
#     start_excel_report_http()