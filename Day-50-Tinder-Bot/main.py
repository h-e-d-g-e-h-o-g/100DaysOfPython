from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url="https://tinder.com/")
time.sleep(5)
decline_cookies = driver.find_element(By.XPATH, '//*[@id="t1951895747"]/div/div[2]/div/div/div[1]/div[2]/button')
decline_cookies.click()

create_account_button = driver.find_element(By.XPATH, '//*[@id="t1951895747"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
create_account_button.click()
time.sleep(2)
facebook_button = driver.find_element(By.XPATH, '//*[@id="t223514671"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_button.click()
# accept_cookies = driver.find_element(By.CSS_SELECTOR, ".My(8px) button")
# accept_cookies.click() 
windows = driver.window_handles
base_window = windows[0]
facebook_login_window = windows[1]
driver.switch_to.window(facebook_login_window)
print(driver.title)
# Confirming the window on which we are targeting currently
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("raholverma20@gmail.com")
password_input = driver.find_element(By.ID, "pass")
password_input.send_keys("rv2345678")
login_button = driver.find_element(By.NAME, "login")
login_button.click()
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(15)
allow_location = driver.find_element(By.XPATH, '//*[@id="t223514671"]/main/div/div/div/div[3]/button[1]')
allow_location.click()
time.sleep(5)
not_interested = driver.find_element(By.XPATH, '//*[@id="t223514671"]/main/div/div/div/div[3]/button[2]')
not_interested.click()
time.sleep(5)
counter = 0
while (counter<=100):
    time.sleep(2)
    try:
        actions = ActionChains(driver)
        actions.send_keys(Keys.ARROW_RIGHT)
        actions.perform()
        counter = counter + 1
    except (NoSuchElementException, ElementClickInterceptedException):
        print("error")
        driver.quit()

