# Handeling cooies using SeleniumPython

import unittest
from selenium import webdriver

class Cookies(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://www.amazon.in")
	def test1_cookies(self):
		driver = self.driver
		cookie = {'name':'foo','value':'bar'}
		driver.add_cookie(cookie)
		output = driver.get_cookies()
		print(output)
		print(len(output))
		output1 = driver.delete_all_cookies()
		driver.delete_cookie('foo')

	def tearDown(self):
		self.driver.quit()
if __name__=='__main__':
	unittest.main()
	