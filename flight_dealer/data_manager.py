import os
import requests

SHEETY_PRICES_ENDPOINT = "SHEETY_API_ENDPOINT_PRICES_TABLE"

bearer_header = {
    "Authorization": "Bearer {}".format(os.environ.get("BEARER"))
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_flights(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=bearer_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_iatacodes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(url=SHEETY_PRICES_ENDPOINT + "/{}".format(city["id"]), json=new_data)
