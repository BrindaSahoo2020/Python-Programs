#Handeling Javascript pop up

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

signin = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(1)
alert = driver.switch_to_alert()
print(alert.text)
#alert.dismiss()
#alert.accept()
driver.quit()

#Handeling Frames
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://www.londonfreelance.org/courses/frames/")

#driver.switch_to.frame(2) #by index
#driver.switch_to.frame('main')
frame_elem = driver.find_element(By.NAME,'main')
driver.switch_to.frame(frame_elem)
header = driver.find_element_by_css_selector("body > h2")
print(header.text)

#Authentication pop up

#driver.get("http://Username:Password@SiteURL")

#Handeling File upload

driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")
elem = driver.find_element(By.XPATH,"//input[@type='file']")
elem.send_keys("/home/brinda/Brinda/200+ Selenium Interview Questions .docx")

driver.find_element(By.XPATH,"//input[@type='submit']").click()
driver.quit()