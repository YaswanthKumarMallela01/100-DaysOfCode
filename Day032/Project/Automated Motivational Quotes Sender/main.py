import random
import smtplib
import datetime as dt
import os

MY_EMAIL = os.getenv("MY_EMAIL")  # Remove this and add your mail account in strings
MY_PASSWORD = os.getenv("MY_PASSWORD")  # Remove this and add your mail account App Password in strings

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 3:
    with open("quotes.txt", "r") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    '''STARTTLS is the handshake Gmail is rejecting in our environment.
       You must switch to implicit SSL (port 465) instead of STARTTLS (port 587).'''
    '''TLS negotiation on port 587 (STARTTLS) sometimes fails due to:
            Windows OpenSSL provider mismatch
            Python 3.12 TLS defaults
            Gmail refusing weak cipher negotiation attempts
       But port 465 uses implicit SSL from the beginning, eliminating the negotiation phase entirely.'''

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Thursday Motivation!\n\n{quote}"
        )
    '''This uses:
            Direct SSL connection
            No STARTTLS negotiation
            More stable handshake
            Fully compatible with Gmail + Python 3.12'''




