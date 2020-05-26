#Switching between URLs using Selenium Python

import unittest
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select 

class Windowswitching(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://www.sanfoundry.com/python-questions-answers-classes-objects-1/")
    def test_switchwindow(self):
        driver = self.driver
        window_before = driver.window_handles[0]
        driver.execute_script("window.open('https://www.techbeamers.com/python-interview-questions-programmers/','new window')")
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.switch_to.window(window_before)
        #print(driver.title)
        if(driver.title == 'Classes & Objects - Python Questions and Answers - Sanfoundry'):
            print("Test is pass")
        else:
            print("Test is fail")
        time.sleep(2)
	def tearDown(self):
		self.driver.quit()

if __name__=='__main__':
	unittest.main()