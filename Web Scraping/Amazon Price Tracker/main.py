import smtplib
import requests
import os
from bs4 import BeautifulSoup

MY_EMAIL = "YOUR_EMAIL"
PASSWORD = os.environ.get("PASSWORD")

URL = "https://www.amazon.de/-/en/Benjamin-Graham/dp/0060555661/ref=sr_1_1?keywords=der+intelligente+investor+deutsch&qid=1676129344&sprefix=der+intel%2Caps%2C125&sr=8-1"
headers = {
    "User-Agent": "YOUR_USER_AGENT",
    "Accept-Language": "en-US,en;q=0.9,bg;q=0.8"
}

response = requests.get(url=URL, headers=headers)

web_page = BeautifulSoup(response.text, "lxml")
price = float(web_page.find(name="span", class_="a-size-base").getText().split("€")[1])

if price < 17.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ANY_EMAIL",
            msg="Subject:Low Price Book!\n\nThe Intelligent Investor is available on Amazon for just €{}.\n{}".format(
                price,
                URL
            ).encode("utf-8")
        )