from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "SOF"

data_manager = DataManager()
sheet_data = data_manager.get_flights()
flight_searcher = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_searcher.get_iatacode(row["city"])


data_manager.destination_data = sheet_data
data_manager.update_destination_iatacodes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_searcher.search_flights(ORIGIN_CITY_CODE,
                                            destination["iataCode"],
                                            from_time=tomorrow,
                                            to_time=six_months_from_today)
    if not flight:
        continue

    if flight.price < destination["lowestPrice"]:
        notification = NotificationManager(flight)
        destination["lowestPrice"] = flight.price
        if flight.stop_overs > 0:
            additional_text = "\nFlight has {} stop over, via {}".format(
                flight.stop_overs,
                flight.via_city
            )
            notification.send_sms(additional_notification=additional_text)
            notification.send_email(additional_notification=additional_text)
        else:
            notification.send_sms()
            notification.send_email()
