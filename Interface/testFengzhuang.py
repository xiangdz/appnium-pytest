# -*- coding: utf-8 -*-
# @Time    : 2017/6/4 20:36
# @Author  :
# @Site    :
# @File    : testFengzhuang.py
from Public.test_requests import jiekou
from Public.log import logger



@logger("调用接口去实例化")
class TestApi(object):
	def __init__(self,url,key,connent,fangshi):
		self.url=url
		self.key=key
		self.connent=connent
		self.fangshi=fangshi
		self.reques = jiekou()

	def testapi(self):
		if self.fangshi=='POST':
			self.parem = {'key': self.key, 'info': self.connent}
			self.response=self.reques.post(self.url,self.parem)
		elif self.fangshi=="GET":
			self.parem = {'key': self.key, 'info': self.connent}
			self.response = self.reques.get(url=self.url,params=self.parem)
		return self.response
	def getJson(self):
		json_data = self.testapi()
		return json_data