import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += os.getcwd()
driver = webdriver.Chrome()

driver.get('https://syntaxprojects.com/basic-first-form-demo.php') #sum test
#driver.get('https://www.folha.uol.com.br') #no_button test
driver.implicitly_wait(5)
try:
	no_button = driver.find_element(By.CLASS_NAME, 'banner-lgpd-consent__accept')
	no_button.click()
except:
	print('No element with this class name. Skipping ....')

sum1 = driver.find_element(By.ID, 'sum1')
sum2 = driver.find_element(By.ID, 'sum2')

sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD5 )
sum2.send_keys(15)

btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
btn.click()