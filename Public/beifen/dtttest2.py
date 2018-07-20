
#usr/bin/python#us
#encoding:utf-8
import time
from appium import webdriver
from ddt import ddt,data,unpack
import unittest


class MyTestCase(unittest.TestCase):
    #这个相当于我们初始化的方法,或者类比web自动化的testNg中的beforeClass
    def setUp(self):
        desired_caps = {}
        #操作的设备类型
        desired_caps['platformName'] = 'Android'
        #设备版本
        desired_caps['platformVersion'] = '6.0'
        #设备名称
        desired_caps['deviceName'] = 'emulator-5554'
        #操作设备App的包名
        desired_caps['appPackage'] = 'com.ss.android.article.news'
        #启动页activity
        desired_caps['appActivity'] = '.activity.SplashBadgeActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        #appium配置
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    #类比函数
    @data(("b2d",False),("b22",True))
    @unpack
    def testLogin(self,idName,expectedResult):
        self.driver.find_element_by_id(idName).click()
        try:
            if self.driver.find_element_by_id("b2d").is_displayed():
               exist=True
        except Exception as e:
            # 如果这个按钮没有显示,那么我们代表上面的if判断失败，执行下面的语句
            exist = False
        #断言比较
        self.assertEqual(exist,expectedResult)
    def tearDown(self):
        # 释放资源
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()