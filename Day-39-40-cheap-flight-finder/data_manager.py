import os
import requests
# from pprint import pprint
API_KEY = os.environ["ENV_API_KEY"]

class DataManager:
    def __init__(self):
        self.SHEETY_ENDPOINT = f"https://api.sheety.co/{API_KEY}/myFlightDeals/prices"
        # self.UPDATE_ENDPOINT = f"{self.SHEETY_ENDPOINT}/{row_id}"

    def get_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT)
        response.raise_for_status()
        self.data = response.json()
        return self.data

    def modify_data(self, prices_detail, iata_code):
        row_id = prices_detail["id"]
        update_endpoint = f"{self.SHEETY_ENDPOINT}/{row_id}"
        update_params = {
            'price': {
                'iataCode': iata_code
            }
        }
        response_update = requests.put(url=update_endpoint, json=update_params, auth=("Arhog", "Arpit26@"))
        response_update.raise_for_status()
        # pprint(response_update.text)

    # def modify_data(self):
    #     update_params = {
    #         "price": {
    #             'iataCode': "TESTING"
    #         }
    #     }
    #     self.response_update = requests.put(url=self.UPDATE_ENDPOINT, json=update_params)
    #     self.response_update.raise_for_status()


# dataManger.get_data()