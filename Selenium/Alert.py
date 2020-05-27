#Handeling Alert message using Selenium Python

import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

class Alert(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome("/usr/bin/chromedriver")
		self.driver.implicitly_wait(7)
		self.driver.maximize_window()
		self.driver.get("http://www.teachmeselenium.com/automation-practice");
	def test1(self):
		driver = self.driver				
 		driver.find_element_by_link_text("Click Me to get Alert").click()
		alert = driver.switch_to_alert()
 		strAlertText = alert.text
		print(strAlertText) 
		alert.accept()
        time.sleep(2)
   	
	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	unittest.main()
		