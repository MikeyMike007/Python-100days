# Following program checks whether today is a pre-defined day e.g. Monday and if this is the case, a quote will be sent to the defined email

import datetime as dt
import smtplib
import random
import os

WEEKDAYS = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
SERVER = "YOUR_SMPT_SERVER_HERE"
EMAIL = "YOUR_EMAIL_HERE"
RECIEVER = "YOUR_EMAIL_HERE"
PASSWORD = os.environ.get("SECRET_PASSWD")


class QuoteGenerator:
    def __init__(self):
        with open("./quotes.txt") as data:
            self.quotes = data.readlines()

    def random_quote(self):
        return random.choice(self.quotes)


class EmailSender:
    def __init__(self, server, email, reciever_email, password):
        self.server = server
        self.email = email
        self.reciever_email = reciever_email
        self.password = password

    def send_email(self, quote):
        with smtplib.SMTP(self.server) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.reciever_email,
                msg=f"Subject:Monday Motivation\n\n{quote}",
            )


class DayChecker:
    def __init__(self, day_to_check):
        self.current_day = dt.datetime.now().weekday()
        self.day_to_check = day_to_check

    def is_day(self):
        return True if WEEKDAYS[self.current_day - 1] == self.day_to_check else False

    def update_current_day(self):
        self.current_day = dt.datetime.now().weekday()


email_sender = EmailSender(SERVER, EMAIL, RECIEVER, PASSWORD)
day_checker = DayChecker("Monday")
quote = QuoteGenerator()

if day_checker.is_day():
    email_sender.send_email(quote.random_quote())
