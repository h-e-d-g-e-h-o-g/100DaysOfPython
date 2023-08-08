from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import time

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = "raholverma20@gmail.com"
TWITTER_PASSWORD = "rv2345678"

class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service=service)
        self.promised_download_speed = PROMISED_DOWN
        self.promised_upload_speed = PROMISED_UP

    def get_internet_speed(self) -> None:
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(2)
        accept_cookies_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        accept_cookies_button.click()
        start_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        start_button.click()
        time.sleep(40)
        download_speed_element = self.driver.find_element(By.CLASS_NAME, "download-speed")
        upload_speed_element = self.driver.find_element(By.CLASS_NAME, "upload-speed")
        self.download_speed = float(download_speed_element.text)
        self.upload_speed = float(upload_speed_element.text)

    def tweet_at_provider(self) -> None:
        self.driver.get(url="https://twitter.com/")
        time.sleep(10)
        try:
            email_input_button = self.driver.find_element(By.NAME, "text")
            email_input_button.send_keys("raholverma20@gmail.com")
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(2)
            username_input = self.driver.find_element(By.NAME, "text")
            username_input.send_keys("rahol24000")
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(4)
            password_input_button = self.driver.find_element(By.NAME, "password")
            password_input_button.send_keys("rv2345678")
            time.sleep(4)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(10)
            tweet = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
            tweet.click()
            tweet.send_keys(f"Hey internet provider, why is my internet speed {self.download_speed}down/{self.upload_speed}up when i pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
            tweet_button.click()
        except NoSuchElementException:
            pass


internet_speed = InternetSpeedTwitterBot()
internet_speed.get_internet_speed()
if internet_speed.download_speed < PROMISED_DOWN or internet_speed.upload_speed < PROMISED_UP:
    internet_speed.tweet_at_provider()

internet_speed.driver.quit()
#internet_speed.tweet_at_provider()
