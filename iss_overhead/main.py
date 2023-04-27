import smtplib
import requests
from datetime import datetime as dt
import time

MY_LAT = 42.194947
MY_LNG = 24.336280

MY_EMAIL = "YOUR_EMAIL"
PASSWORD = "SMTP_PASSWORD"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return abs(iss_latitude - MY_LAT) == 5 and abs(iss_longitude - MY_LNG) == 5


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.now().hour

    return time_now not in range(sunrise, sunset + 1)


while True:
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ANY_EMAIL",
            msg="Subject:Look up!\n\nThe ISS is above you in the sky"
        )
    time.sleep(60)
