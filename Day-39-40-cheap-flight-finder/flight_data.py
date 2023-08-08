import os
import requests
from datetime import datetime, timedelta
from pprint import pprint
today_date = datetime.now()
tomorrow_date = today_date + timedelta(1)
six_months_after = tomorrow_date + timedelta(6*30)


class FlightData:
    def __init__(self):
        self.tequila_api_key = os.environ["ENV_API_KEY_TEQUILA"]
        self.flight_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        # print(tomorrow_date.strftime("%d/%m/%Y"))
        # print(six_months_after.strftime("%d/%m/%Y"))
    def get_price(self, prices_detail):
        required_params = {
            "fly_from": "LON",
            "fly_to": prices_detail['iataCode'],
            "date_from": tomorrow_date.strftime("%d/%m/%Y"),
            "date_to": six_months_after.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
            # "price_to": prices_detail['lowestPrice']
        }
        header = {
            'apiKey': self.tequila_api_key
        }
        # print(required_params)
        try:
            response_flight_details = requests.get(url=self.flight_search_endpoint, params=required_params)
            response_flight_details = requests.get(url=response_flight_details.url.replace("%2F","/"), headers=header)
            response_flight_details.raise_for_status()
            data = response_flight_details.json()["data"][0]


        except:
            print(f"Flight not found for {prices_detail['city']}")
            return False
        self.price = data["price"]
        self.origin_city = data["route"][0]["cityFrom"]
        origin_airport = data["route"][0]["flyFrom"],
        self.origin_airport = origin_airport[0]
        destination_city = data["route"][0]["cityTo"],
        self.destination_city = destination_city[0]
        self.destination_airport = data["route"][0]["flyTo"]
        out_date = data["route"][0]["local_departure"].split("T"),
        self.out_date = out_date[0][0]
        self.return_date = data["route"][1]["local_departure"].split("T")[0]
        print(f"{prices_detail['city']}: £{self.price}")
        return True





# flightData = FlightData()
