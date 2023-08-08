from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
import time
# import requests
from pprint import pprint

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
# # press = driver.find_element(By.XPATH("//*[text()='Get started free']"))
# # press.clickAndHold()
URL = "https://docs.google.com/forms/d/e/1FAIpQLSfNGkwGq-JwqdqB9za25EKMaLrAuPQzO9AF9lhvdS6Hu0oHAQ/viewform?usp=sf_link"
# header = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
#     'Accept-Language': "en-US,en;q=0.9"
# } 
driver.get(url=URL)
# driver.maximize_window()
# # while True:
# #     pass
# target_scroller = driver.find_element(By.CLASS_NAME, "result-list-container")
actions = ActionChains(driver)
# # for i in range(120):
# #     actions.key_down(Keys.TAB).perform()
# for i in range(120):
#     actions.key_down(Keys.ARROW_DOWN).perform()

# response = driver.page_source
# soup = BeautifulSoup(response, "html.parser")
# estate_prices = [price.getText() for price in soup.select(selector=".PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 .PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")]
# estate_addresses = [address.getText() for address in soup.select(selector=".property-card-data address")]
# estate_links = [link.get("href") for link in soup.select(selector=".property-card-data a")]
# with open("Data.txt","a+") as f:
#     for estate_price in estate_prices:
#         f.write(estate_price)
#     for estate_address in estate_addresses:
#         f.write(estate_address)
#     for estate_price in estate_links:
#         f.write(estate_price)
#     f.write(estate_addresses)
#     f.write(estate_links)

# print(len(estate_prices))
# print(len(estate_addresses))
# print(len(estate_links))
# response = requests.get(url=URL, headers=header)
# print(response.status_code)
# response_data = response.text

# soup = BeautifulSoup(response_data, "html.parser")
# estate_price = soup.select(selector=".PropertyCardWrapper__StyledPriceGridContainer-srp__sc-16e8gqd-0 .PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1")
# print(len(estate_price))
# for estate in  estate_price:
#     print(estate.getText())
# for estate in estate_price:
#     print(estate.get)

estate_prices = ['$2,725+ 1 bd', '$2,980/mo', '$2,810+ 1 bd', '$2,995/mo', '$2,946+ 1 bd', '$2,810+/mo', '$2,515+ 1 bd', '$2,845+ 1 bd', '$2,901/mo', '$2,747+ 1 bd', '$2,657+ 1 bd', '$2,842+ 1 bd', '$2,395/mo', '$2,749/mo', '$2,912/mo', '$2,895+/mo', '$2,295+ 1 bd', '$2,757+ 1 bd', '$2,795+ 1 bd', '$2,795/mo', '$2,960/mo', '$2,995/mo', '$2,799+/mo', '$2,366+ 1 bd', '$2,950+ 1 bd', '$2,795/mo', '$2,770+ 1 bd', '$2,895/mo', '$2,995/mo', '$2,195+ 1 bd', '$2,893/mo', '$2,795/mo', '$2,295+ 1 bd', '$3,000+/mo', '$2,095/mo', '$2,195+/mo', '$2,987/mo', '$2,725+ 1 bd', '$2,399+ 1 bd', '$2,895+ 1 bd', '$2,595+/mo']
print(len(estate_prices))
estate_addresses = ['Parkmerced | 3711 19th Ave, San Francisco, CA', 'L Seven, 1222 Harrison St #5210, San Francisco, CA 94103', 'AVA 55 Ninth | 55 9th St, San Francisco, CA', '923 Folsom, 923 Folsom St APT 703, San Francisco, CA 94107', 'Soma at 788 | 788 Harrison St, San Francisco, CA', 'NorthPoint Apartments, 2211 Stockton St, San Francisco, CA 94133', 'AVA Nob Hill | 965 Sutter St, San Francisco, CA', 'Mission Bay by Windsor | 360 Berry St, San Francisco, CA', 'Olume, 1401 Mission St #1005, San Francisco, CA 94103', 'Olume | 1401 Mission St, San Francisco, CA', 'Ashton San Francisco Apartments | 301 Executive Park Blvd, San Francisco, CA', 'Hanover Soma West | 1140 Harrison St, San Francisco, CA', '828 Franklin, 828 Franklin St #606, San Francisco, CA 94102', 'HQ, 1532 Harrison St #320, San Francisco, CA 94103', 'Edgewater, 355 Berry St APT 440, San Francisco, CA 94158', '747 Geary Street, 747 Geary St, Oakland, CA 94609', 'Mosser Towers Apartments | 455 Eddy St, San Francisco, CA', 'Prism | 1028 Market St, San Francisco, CA', 'Mt. Sutro | 480 Warren Dr, San Francisco, CA', '1158 Montgomery, 1158 Montgomery St #1158, San Francisco, CA 94133', 'Delphine on Diamond, 5285 Diamond Heights Blvd #2-115, San Francisco, CA 94131', '2775 Market St, 2775 Market St APT 102, San Francisco, CA 94114', 'Marina Cove Apartments, 1550 Bay St, San Francisco, CA 94123', '50 Jones | 50 Jones St, San Francisco, CA', '1333 Gough Apartments at Cathedral Hall | 1333 Gough St, San Francisco, CA', 'Slate Residences, 911 Bryant St APT 403, San Francisco, CA 94103', '480 Potrero Ave | 480 Potrero Ave, San Francisco, CA', '947 Bush, 947 Bush St #420, San Francisco, CA 94109', '2000 Post, 2000 Post St #370, San Francisco, CA 94115', "750 O'Farrell St | 750 Ofarrell St, San Francisco, CA", '333 Fremont, 333 Fremont St APT 607, San Francisco, CA 94105', "601 O'Farrell, 601 Ofarrell St APT 514, San Francisco, CA 94109", '676 Geary | 676 Geary St, San Francisco, CA', 'NorthPoint Vistas, 2351 Powell St, San Francisco, CA 94133', '57 Taylor, 57 Taylor St APT 340, San Francisco, CA 94102', '1350 Washington Street, 1350 Washington St, San Francisco, CA 94109', 'One Henry Adams, 1 Henry Adams St UNIT S-508, San Francisco, CA 94103', 'The Terraces | 1330 Bush St, San Francisco, CA', '2133 Stockton Street Apartments | 2133 Stockton St, San Francisco, CA', '990 Geary | 990 Geary St, San Francisco, CA', '125-135 Gardenside, 125 Gardenside Dr, San Francisco, CA 94114']
print(len(estate_addresses))
estate_links = ['https://www.zillow.com/apartments/san-francisco-ca/parkmerced/5XjKHx/', 'https://www.zillow.com/apartments/san-francisco-ca/l-seven/9NJtD7/', 'https://www.zillow.com/apartments/san-francisco-ca/ava-55-ninth/5XkH8X/', 'https://www.zillow.com/apartments/san-francisco-ca/923-folsom/5Yy6Np/', 'https://www.zillow.com/apartments/san-francisco-ca/soma-at-788/5XkGzw/', 'https://www.zillow.com/apartments/san-francisco-ca/northpoint-apartments/5XjLPJ/', 'https://www.zillow.com/apartments/san-francisco-ca/ava-nob-hill/5XkHq6/', 'https://www.zillow.com/apartments/san-francisco-ca/mission-bay-by-windsor/9NM9Sk/', 'https://www.zillow.com/apartments/san-francisco-ca/olume/5Yy6VF/', 'https://www.zillow.com/b/Olume-San-Francisco-CA/37.775043,-122.415955_ll/', 'https://www.zillow.com/apartments/san-francisco-ca/ashton-san-francisco-apartments/5XjLVd/', 'https://www.zillow.com/apartments/san-francisco-ca/hanover-soma-west/9NJsx9/', 'https://www.zillow.com/apartments/san-francisco-ca/828-franklin/5XkH2V/', 'https://www.zillow.com/apartments/san-francisco-ca/hq/9NJthZ/', 'https://www.zillow.com/apartments/san-francisco-ca/edgewater/5XjVQc/', 'https://www.zillow.com/b/747-geary-street-oakland-ca-CYzGVt/', 'https://www.zillow.com/apartments/san-francisco-ca/mosser-towers-apartments/9NJr4f/', 'https://www.zillow.com/apartments/san-francisco-ca/prism/9NJpRh/', 'https://www.zillow.com/apartments/san-francisco-ca/mt.-sutro/5XjVRC/', 'https://www.zillow.com/apartments/san-francisco-ca/1158-montgomery/9NLyBz/', 'https://www.zillow.com/apartments/san-francisco-ca/delphine-on-diamond/5XjTZJ/', 'https://www.zillow.com/apartments/san-francisco-ca/2775-market-st/5XsQ4D/', 'https://www.zillow.com/apartments/san-francisco-ca/marina-cove-apartments/5XjRBB/', 'https://www.zillow.com/apartments/san-francisco-ca/50-jones/Bntcg2/', 'https://www.zillow.com/apartments/san-francisco-ca/1333-gough-apartments-at-cathedral-hall/5XjRmn/', 'https://www.zillow.com/apartments/san-francisco-ca/slate-residences/9NJxjf/', 'https://www.zillow.com/apartments/san-francisco-ca/480-potrero-ave/5mY4JQ/', 'https://www.zillow.com/apartments/san-francisco-ca/947-bush/5XjW9S/', 'https://www.zillow.com/apartments/san-francisco-ca/2000-post/5XjRNn/', "https://www.zillow.com/apartments/san-francisco-ca/750-o'farrell-st/5YXpvZ/", 'https://www.zillow.com/apartments/san-francisco-ca/333-fremont/5gjwKL/', "https://www.zillow.com/apartments/san-francisco-ca/601-o'farrell/5XjMQR/", 'https://www.zillow.com/apartments/san-francisco-ca/676-geary/5XjMgm/', 'https://www.zillow.com/apartments/san-francisco-ca/northpoint-vistas/5XqJsJ/', 'https://www.zillow.com/apartments/san-francisco-ca/57-taylor/5XjPkN/', 'https://www.zillow.com/apartments/san-francisco-ca/1350-washington-street/9NKDS7/', 'https://www.zillow.com/apartments/san-francisco-ca/one-henry-adams/9NJvHk/', 'https://www.zillow.com/apartments/san-francisco-ca/the-terraces/5XjVSb/', 'https://www.zillow.com/apartments/san-francisco-ca/2133-stockton-street-apartments/5Xhzkj/', 'https://www.zillow.com/apartments/san-francisco-ca/990-geary/5XjSTc/', 'https://www.zillow.com/apartments/san-francisco-ca/125.dash.135-gardenside/BjFbbM/']
print(len(estate_links))
estate_details = []

# print(type(estate_data))
for num in range(len(estate_prices)):
    estate_details.append({
        'address': estate_addresses[num],
        'price': estate_prices[num],
        'link': estate_links[num]
    })
estate_content = ['address', 'price', 'link']
# print(estate_details)
# print(estate_prices[1])
# for estate_address in estate_addresses:
#     print(estate_address)
# input_elements = driver.find_elements(By.CSS_SELECTOR, ".Xb9hP input")
# print(len(input_elements))

# while True:
#     pass
for num in range(len(estate_details)):
    driver.get(url=URL)
    for n in range(6):
        actions.send_keys(Keys.TAB).perform()
        if n>=2 and n<5:
            actions.send_keys(estate_details[num][estate_content[n-2]]).perform()
    # for n in range(len(input_elements)):
    #     input_elements[n].click()
    #     input_elements[n].send_keys(estate_details[n][estate_content[n]])
        if n==5:
            actions.send_keys(Keys.ENTER).perform()
    # submit_button = driver.find_element(By.CLASS_NAME, "snByac")
    # submit_button.click()
    time.sleep(2)
