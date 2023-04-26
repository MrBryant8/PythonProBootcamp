import requests
from flight_data import FlightData
from twilio.rest import Client
import os
import smtplib

ACC_SID = "YOUR ACC_SID"
AUTH_TOKEN = os.environ.get("AUTH_CODE")

MY_EMAIL = "YOUR_EMAIL"
PASSWORD = os.environ.get("PASSWORD")  #  SMTP PASSWORD

GOOGLE_FLIGHTS_LINK = 'https://www.google.co.uk/flights?hl=en#flt='
SHEETY_USERS_ENDPOINT = 'SHEETY_API_LINK_TO_USERS_TABLE'

bearer_header = {
    "Authorization": "Bearer {}".format(os.environ.get("BEARER"))  # BEARER TOKEN FOR SHEETY
}


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight: FlightData):
        self.notification_body = "Low price alert!Only ${} to fly from {}-{} to {}-{},from {} to {}.".format(
            flight.price,
            flight.origin_city,
            flight.origin_airport,
            flight.destination_city,
            flight.destination_airport,
            flight.out_date,
            flight.return_date,
        )
        self.client = Client(ACC_SID, AUTH_TOKEN)

        self.link = GOOGLE_FLIGHTS_LINK + '{}.{}.{}*{}.{}.{}'.format(
            flight.origin_airport,
            flight.destination_airport,
            flight.out_date,
            flight.destination_airport,
            flight.origin_airport,
            flight.return_date
        )

    def send_sms(self, additional_notification=""):

        message = self.client.messages.create(
            to='RECEIVER_EMAIL',
            from_='SENDER_EMAIL',
            body="{}.{}".format(self.notification_body, additional_notification)
        )
        print(message.status)

    def send_email(self, additional_notification=""):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=bearer_header)
        data = response.json()["users"]
        for user in data:
            with smtplib.SMTP("SMTP_PROVIDER_LINK") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user["email"],
                    msg="Subject:Low Price Flight!\n\n{}{}\n{}".format(
                        self.notification_body,
                        additional_notification,
                        self.link
                    ).encode("utf-8")
                )
