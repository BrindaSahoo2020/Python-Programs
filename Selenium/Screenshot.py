#Take Screenshot,navigate back and fro using Selenium Python

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

class Screenshot(unittest.TestCase):
    def setUp(self):
		self.driver = webdriver.Chrome()
		driver = self.driver
		driver.maximize_window()
		driver.implicitly_wait(5)
		driver.get("https://www.google.co.in/")
    def test1(self):
        #Take screenshot
        self.driver.get_screenshot_as_file("screenshot.png")
        time.sleep(2)
        #Web page navigations(back,forward)
        self.driver.get("https://timesofindia.indiatimes.com/")
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.driver.forward()

    def tearDown(self):
		self.driver.quit()
if __name__=='__main__':
	unittest.main()