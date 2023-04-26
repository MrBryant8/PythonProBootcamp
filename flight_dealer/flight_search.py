import requests
from flight_data import FlightData
import os
from pprint import pprint

KIWI_ENDPOINT = "https://api.tequila.kiwi.com"
KIWI_API = os.environ.get("KIWI_API")

headers = {
    "apikey": KIWI_API
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_iatacode(self, name):
        params = {
            "term": name,
            "location_types": "city"
        }

        data = requests.get(url=KIWI_ENDPOINT + "/locations/query", params=params, headers=headers).json()
        return data["locations"][0]["code"]

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "one_for_city": 1,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "curr": "USD",
            "flight_type": "round",
        }
        response = requests.get(url=KIWI_ENDPOINT + "/v2/search", headers=headers, params=query)  # Url for searching
        pprint(response.json())

        try:
            data = response.json()['data'][0]

        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(url=KIWI_ENDPOINT + "/v2/search", headers=headers, params=query)
            try:
                data = response.json()['data'][0]
            except IndexError:
                print("No flights found for {}.".format(destination_city_code))
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][1]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data['route'][0]["cityTo"]
                )
                print("{}: ${}".format(flight_data.destination_city[0], flight_data.price[0]))
                return flight_data

        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print("{}: ${}".format(flight_data.destination_city, flight_data.price))
            return flight_data
