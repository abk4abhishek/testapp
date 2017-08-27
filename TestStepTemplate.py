from corehit import *
from coretests import *


class TestStepTemplate:
	def __init__(self,teststeps):
		self.teststeps=teststeps

	def runnit(self):
		for item in self.teststeps:
		    self.response=Hitit(item["method"],item["url"])
		    test_status_code_it(self.response,item["tests"]['test_status_code']['expected'])