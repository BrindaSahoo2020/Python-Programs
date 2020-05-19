#Search a word in google,print the same then verify it

import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Google(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(6)
		self.driver.maximize_window()
		self.driver.get("https://www.google.co.in/")
	def test_search(self):
		driver = self.driver
		search = driver.find_element_by_name('q')
		search.send_keys("brinda")
		search.submit()
		time.sleep(5)
		print (driver.title)
		if (driver.title == "brinda - Google Search"):
				print("Test case is pass")
		else:
				print("Test case is fail")
	def tearDown(self):
		self.driver.quit()
if __name__=='__main__':
	unittest.main()