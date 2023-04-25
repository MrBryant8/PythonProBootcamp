import random
import datetime as dt
import smtplib
import pandas

MY_EMAIL = 'YOUR_EMAIL'
PASSWORD = 'YOUR_SMTP_PASSWORD'

df = pandas.read_csv("birthdays.csv")
bday_dict = df.to_dict("records")

today = dt.datetime.now()

# Another cool way of making the birthday dictionary
# birthdays = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in df.iterrows()}

for person in bday_dict:
    if person["month"] == today.month and person["day"] == today.day:  #
        file_path = "letter_templates/letter_{}.txt".format(random.randint(1, 3))  # choose a random template
        with open(file_path) as file:
            letter = file.read()
            wish = letter.replace("[NAME]", person["name"]).format(
                year=str(today.year-int(person["year"]))
            )

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg="Subject:Birthday wish\n\n{}".format(wish))
