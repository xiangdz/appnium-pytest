""" 
@author: lileilei
@file: get_excel_new.py 
@time: 2018/4/30 11:04 
"""
import xlrd
from config import  path
def datacel(path):
    datas=[]
    file=xlrd.open_workbook(path)
    me=file.sheets()[0]
    nrows=me.nrows
    for i in range(1,nrows):
        datas.append({"id":me.cell(i,0).value,'key':me.cell(i,2).value,
                         'content':me.cell(i,3).value,'url':me.cell(i,4).value,
                         'name':me.cell(i,1).value,'fangshi':me.cell(i,5).value,
                         'assert':me.cell(i,6).value})
    return datas


if __name__ == '__main__':
   aa= datacel(path.casedatapath)
   print(aa)