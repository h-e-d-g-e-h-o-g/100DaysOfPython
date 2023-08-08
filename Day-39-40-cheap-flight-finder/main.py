# import os
# import requests
# API_KEY = os.environ["ENV_API_KEY"]
# SHEETY_ENDPOINT = f"https://api.sheety.co/{API_KEY}/myFlightDeals/prices"
# response = requests.get(url=SHEETY_ENDPOINT)
# response.raise_for_status()
# print(response.text)
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
dataManager = DataManager()
sheet_data = dataManager.get_data()
prices_details = sheet_data['prices']
flightSearch = FlightSearch()
flightData = FlightData()
notificationManager = NotificationManager()
for city_price_detail in prices_details:
    # iata_code = flightSearch.updating_flight_data(city_price_detail)
    # dataManager.modify_data(city_price_detail, iata_code)
    if flightData.get_price(city_price_detail):
         notificationManager.message_send(city_price_detail['lowestPrice'], flightData)
    else:
         break



