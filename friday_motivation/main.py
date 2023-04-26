import smtplib
import random
import datetime as dt

my_email = "YOUR_EMAIL"
password = "YOUR_SMTP_PASSWORD"

if dt.datetime.now().weekday() == 5:
    with open("quotes.txt") as file:
        content = file.readlines()
        message = random.choice(content)

    with smtplib.SMTP("SMTP_PROVIDER_ADDRESS") as connection:
        connection.starttls()  # Makes the connection encrypted
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="SENDER_EMAIL",
            msg="Subject:A lil bit a motivation\n\n{}".format(message))



