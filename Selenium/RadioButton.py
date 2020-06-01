import unittest
from selenium import webdriver

class Radiobutton(unittest.TestCase):
	def setUp(self):
		option = webdriver.ChromeOptions()
		option.add_argument("--incongito")
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(20)
		self.driver.maximize_window()
		self.driver.get("file:///home/siba/restart/HTML/radibutton.html")
	def test_radiobutton(self):
		driver = self.driver
		ele = driver.find_element_by_id("savingsaccount")
		if ele.is_displayed():
			print("This pageis found")
		else:
			print("Error")
		# To find whether the radio button element is selected or not
		isSelected = driver.find_element_by_id("savingsaccount").get_attribute("checked")
		if isSelected is not None:
   			print("Element checked - ", isSelected)
		else:
			print("Element checked - false")

		# To find whether the radio button element is selected or not
		result = driver.find_element_by_id("savingsaccount").is_selected()
		print("radio button status - ", result)
        # Select radio button. This check is not mandatory
		result = driver.find_element_by_id("savingsaccount").is_selected()
		if result:
			print('radio button already selected')
		else:
			driver.find_element_by_id("savingsaccount").click()
			print('radio button selected')
	def tearDown(self):
		self.driver.quit()
if __name__=='__main__':
	unittest.main()