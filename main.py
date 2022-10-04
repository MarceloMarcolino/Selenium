import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += os.getcwd()
driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/howto/howto_css_download_button.asp")
driver.implicitly_wait(30) #time.sleep(30)
my_element = driver.find_element(By.CLASS_NAME, 'w3-right')
my_element.click()