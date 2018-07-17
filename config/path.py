
import os
from config import time


configdir=os.path.abspath(os.path.dirname(__file__))

print(configdir)

gendir=os.path.dirname(configdir)


print(gendir)

imgdir=os.path.join(gendir,"img")
print(imgdir)

interfacedir=os.path.join(gendir,"Interface")
logdir=os.path.join(gendir,"log")
name="x"

logpath=os.path.join(logdir, '%s.log' % name)

publicdir=os.path.join(gendir,"Public")
datadir=os.path.join(gendir,"test_case_data")
casedatapath=os.path.join(datadir,"case.xlsx")
dubbocasedatapath=os.path.join(datadir,"dubbocase.xlsx")



# baogao
reportdir=os.path.join(gendir,"test_Report")

reporthtmlpath = os.path.join(reportdir, (time.ctime + '.html'))

casedir=os.path.join(gendir,"testCase")
configinipath=os.path.join(configdir,"config.ini")
reportyamlpath=os.path.join(configdir,"test_report.yaml")
reportxlspath = os.path.join(reportdir, '%s-report.xls' % time.ctime)
reporthtml2path = os.path.join(reportdir + '%s-result.html' %time.ctime)













