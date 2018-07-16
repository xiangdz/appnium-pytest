# encoding: utf-8
# ini
from configparser import  ConfigParser
from config import path



cf = ConfigParser()
cf.read(path.configpath,encoding="utf_8")



#返回所有的section
s = cf.sections()
print("section:",s)

print("*" * 70)


o1 = cf.options("mysql")
print("options:mysql",o1)
o2 = cf.options("个人信息")
print("options:个人信息",o2)


# yaml
import yaml
import codecs

with codecs.open(path.reportconfigpath, 'r',"utf-8") as f:

    temp = yaml.load(f.read())


    print(temp)
    print(temp['projectname'])
    # print(temp['basic_name']['test_name'])
    # print(temp['basic_name']['selected_name'][0])


