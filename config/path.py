from configparser import  ConfigParser

import os


# configpath=os.path.dirname(__file__)

configj=os.path.abspath(os.path.dirname(__file__))

print(configj)
# configpath=os.path.dirname(__file__)
# print(configpath)
gendir=os.path.dirname(configj)

# gendir=os.path.join(configpathj,os.path.pardir)

print(gendir)

imgpath=os.path.join(gendir,"img")
print(imgpath)

interfacepath=os.path.join(gendir,"Interface")
logpath=os.path.join(gendir,"log")
publicpath=os.path.join(gendir,"Public")
datapath=os.path.join(gendir,"test_case_data")
reportpath=os.path.join(gendir,"test_Report")
casepath=os.path.join(gendir,"testCase")
configpath=os.path.join(configj,"config.ini")
reportconfigpath=os.path.join(configj,"test_report.yaml")

print(configpath)