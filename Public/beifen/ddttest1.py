import  ddt,yaml



@ddt.data(*data_test)
def test_Login(self,data_test):
LOG.info(data_test['name'])
apijson = TestApi(url=data_test['url'],parem=data_test['parem'],fangshi=data_test['fangshi']).getJson()
if '登录成功' in data_test['name']:
logininfotoYAML(apijson,data_test['name'])

def logininfotoYAML(apijson,usertype):
token = apijson['model']['loginToken']
uid = apijson['model']['userId']
with open(fname, "r")as f:
newinfo = yaml.load(f)
if '老用户' not in usertype:
newinfo['newuser'] = {"uid":uid,"token":token}
with open(fname, "w")as f:
yaml.dump(newinfo,f)
f.close()
else:
newinfo['olduser'] = {"uid":uid,"token":token}
with open(fname, "w")as f:
yaml.dump(newinfo,f)
f.close()