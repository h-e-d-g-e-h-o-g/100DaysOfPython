import requests
import os

class FlightSearch:
    def __init__(self):
        self.flight_search_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.API_KEY_TEQUILA = os.environ["ENV_API_KEY_TEQUILA"]

    def updating_flight_data(self, prices_detail):
        city_name = prices_detail['city']
        required_params = {
            'term': city_name
        }
        header = {
            'apikey': self.API_KEY_TEQUILA
        }
        response_IATA = requests.get(url=self.flight_search_endpoint, params=required_params, headers=header)
        response_IATA.raise_for_status()
        data = response_IATA.json()
        IATA_CITY_CODE = data["locations"][0]["code"]
        return IATA_CITY_CODE

    # def flight_price(self):


