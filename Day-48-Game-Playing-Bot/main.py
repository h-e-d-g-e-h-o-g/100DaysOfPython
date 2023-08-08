# Selenium WebDriver is an automation and testing tool for the web developers.
# Now, why we need Selenium at first, when we already have beautiful soup.
# The reason is, we don't have the same capabilites that browsers have such as searching and clicking on something.
# To do such tasks, we need Selenium WebDriver.
# Selenium automates the browser to do such tasks.
# In order to automate it, we need to define the tasks first on the script.
# It's like creating a robot and ordering it to do such tasks.

from selenium import webdriver
# With the help of webdriver module, we will create WebDriver that will drive the chrome browser and automate all our tasks.
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
# Now what is chrome driver?
# As, we know the selenium package contains the code that helps us to interact with the browser of our choice.
# It can interact with chrome, safari, or firefox.
# In order to make it work specifically with the chrome broswer, we need chrome driver.
# Chrome driver acts as a bridge to bridge the selenium package codes with the chrome browser.
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url="https://www.python.org/")
# The driver will load the webpage whose url is mentioned.
# Now, how to use driver to locate the html elements on the web page that we are loading.
# Selenium web driver provides us with a bunch of methods to search the elements such as by id, by css selectors or by name etc.
# When selenium finds an html element, it return it as selenium element, in order to get particular information, you need to tap into its attributes.
# Even all methods fails, then you can go for "XPath".
# XPath is a way of locating a particular html element by path structure.
# The path structure will navigate to the specific html element in which we are interested.
time_date_content = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

time_dates = [time_text.text.split("\n") for time_text in time_date_content]

event_dict = {}
for num in range(len(time_dates)):
    event_dict[num] = {'time': time_dates[num][0],
                       'name': time_dates[num][1]}

print(event_dict)
# Now, how to interact with the elements that you found. Like typing or clicking on a button?
# In order to click the element that we found, we can use click() on the element that we found.
# There is also a specific find method to find the element which contains link text such as (By.LINK_TEXT)
# If you want to type something on the element that you hold down, you can do this through send_keys().
# You need to pass the keys from the keyboards between the paranthesis mainly letter, numbers or symbols keys.
# If you want to pass keys excluding the keys mentioned above such as enter key, shift key or tab key.
# You need to import them first through selenium.webdriver.common.key module which has Key class.
# Key class contains bunch of constants.
driver.quit()
# quit() method is used to shut down the entire browser once the webpage is loaded.