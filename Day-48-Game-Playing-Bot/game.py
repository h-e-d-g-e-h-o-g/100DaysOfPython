from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

five_seconds = time.time() + 5
five_minutes = time.time() + 60*5
cookie_button = driver.find_element(By.ID, "cookie")
add_ons = driver.find_elements(By.CSS_SELECTOR, "#store div")
add_ons_id = [add_on.get_attribute("id")for add_on in add_ons[:-1]]

def buy_upgrade():
    cookie_count_element = driver.find_element(By.ID, "money")
    cookie_count = int(cookie_count_element.text.replace(",", ""))
    all_prices = [int(price.text.split("-")[1].strip().replace(",", "")) for price in driver.find_elements(By.CSS_SELECTOR, "#store b")[:-1]]
    for number in range(len(all_prices)-1, -1, -1):
        if cookie_count > all_prices[number]:
            upgrade_element = driver.find_element(By.ID, add_ons_id[number])
            upgrade_element.click()
            break

while True:
    cookie_button.click()
    if time.time() > five_seconds:
        five_seconds = time.time() + 5
        buy_upgrade()

    if time.time() > five_minutes:
        cookie_per_second = driver.find_element(By.ID, "cps")
        print(cookie_per_second.text)
        break

driver.quit()