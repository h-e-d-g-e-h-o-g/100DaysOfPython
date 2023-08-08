from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

USERNAME = "raholverma20 "
PASSWORD = "rv2345678"
SIMILAR_ACCOUNT = "chefsteps"

class InstaFollower:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(url="https://www.instagram.com/")
    
    def login(self) -> None:
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(10)
        no_noifications = self.driver.find_element(By.CLASS_NAME, "_a9_1")
        no_noifications.click()

    def find_followers(self) -> None:
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        time.sleep(10)
        followers_label = self.driver.find_element(By.CLASS_NAME, "x1i10hfl")
        followers_label.click()
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(10)
        popup_window = self.driver.find_element(By.CLASS_NAME, "_aano")
        popup_window.click()
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup_window)
            time.sleep(2)
        
    def follow(self) -> None:
        try:
            follow_buttons = self.driver.find_elements(By.TAG_NAME, "button")
            for follow_button in follow_buttons:
                follow_button.click()
                time.sleep(2)
        except ElementClickInterceptedException:
            pass

insta_bot = InstaFollower()
time.sleep(10)
insta_bot.login()
time.sleep(10)
insta_bot.find_followers()
insta_bot.follow()
while True:
    pass