from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Arpit")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Negi")
email_name = driver.find_element(By.NAME, "email")
email_name.send_keys("negiarpit2003@gmail.com")
button_select = driver.find_element(By.TAG_NAME, "button")
button_select.click()

driver.quit()

