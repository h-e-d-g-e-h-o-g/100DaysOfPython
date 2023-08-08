from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3649770269&f_AL=true&geoId=102713980&keywords=python%20developer&location=India&refresh=true")
time.sleep(4)
sign_in_button_option = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in_button_option .click()
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("negiarpit2003@gmail.com")
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Arpit26@")
sign_in_button = driver.find_element(By.CSS_SELECTOR, "form button")
sign_in_button.click()
time.sleep(25)
job_posts = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")
print(len(job_posts))
for job_post in job_posts:
    job_post.click()
    time.sleep(7)
    apply_job = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
    apply_job.click()
    name_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
    name_button.click()
    time.sleep(5)
    submit_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
    if submit_button.text == "Submit application":
        submit_button.click()
    else:
        cross_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        cross_button.click()
        discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
        discard_button.click()

    
    

