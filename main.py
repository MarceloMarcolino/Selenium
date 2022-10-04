import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += os.getcwd()
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/howto/howto_js_popup.asp")
driver.implicitly_wait(8)
my_element = driver.find_element(By.CLASS_NAME, 'popup')
my_element.click()

WebDriverWait(driver, 30).until(
	EC.text_to_be_present_in_element(
		(By.ID, 'myPopup') , # Element filtration
		'A Simple Popup!'# The expected text
	)
)