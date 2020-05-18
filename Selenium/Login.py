#Facebook Login using Python

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
username="XXXX@gmail.com"
password="xxxxx"

class FaceBook(unittest.TestCase):
	def setUp(self):
		option = webdriver.ChromeOptions()
		option.add_argument("--incongito")
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(20)
		self.driver.maximize_window()
		self.driver.get("https://www.facebook.com/")
	def test1_Login(self):
		timeout = 30
		driver = self.driver
		try:
			WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//i[@class='fb_logo img sp_du42O1kxVP5 sx_3e3332']")))
		except TimeoutException:
			print("wait till the page is not loaded")
		login = driver.find_element_by_id("email")
		login.clear()
		login.send_keys(username)
		login = driver.find_element_by_id("pass")
		login.clear()
		login.send_keys(password)
		login = driver.find_element_by_xpath("//input[@value='Log In']").click()
        
	def tearDown(self):
		self.driver.close()
if __name__=='__main__':
	unittest.main()
