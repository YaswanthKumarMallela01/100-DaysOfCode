import datetime as dt
import random
import pandas as pd
import smtplib
import os

now = dt.datetime.now()
month = now.month
day = now.day
today = (month, day)

MY_EMAIL = os.getenv("MY_EMAIL")  # Remove this and add your mail account in strings
MY_PASSWORD = os.getenv("MY_PASSWORD")  # Remove this and add your mail account App Password in strings

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
