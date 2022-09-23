# Following program checks whether there exist a person in birthday.csv that has a birthday today
# If yes, choose a random letter template and insert the persons name and send a greeting email to the person

import datetime as dt
import pandas as pd
import smtplib
import random
import os


WEEKDAYS = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
SERVER = "YOUR_SMPT_SERVER_HERE"
EMAIL = "YOUR_EMAIL_HERE"
RECIEVER = "YOUR_EMAIL_HERE"
PASSWORD = os.environ.get("SECRET")
PLACEHOLDER = "[NAME]"
LETTER_TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]


class BirthdayHandler:
    def __init__(self):
        self.df = pd.read_csv("./birthdays.csv")
        # Convert Dataframe to dict
        self.birthday_records = self.df.to_dict(orient="records")
        self.current_birthday_records = []

    def determine_current_birthdays(self):
        self.current_birthday_records = []
        today = dt.datetime.now()
        day = today.day
        month = today.month
        for birthday_record in self.birthday_records:
            if day == birthday_record["day"] and birthday_record["month"] == month:
                self.current_birthday_records.append(birthday_record)


class EmailSender:
    def __init__(self, server, email, reciever_email, password):
        self.server = server
        self.email = email
        self.reciever_email = reciever_email
        self.password = password

    def send_email(self, message):
        with smtplib.SMTP(self.server) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.reciever_email,
                msg=f"Subject:Birthdays\n\n{message}",
            )


email_sender = EmailSender(SERVER, EMAIL, RECIEVER, PASSWORD)
birthday_handler = BirthdayHandler()
birthday_handler.determine_current_birthdays()

if len(birthday_handler.current_birthday_records) > 0:
    for birthday_record in birthday_handler.current_birthday_records:
        letter_name = random.choice(LETTER_TEMPLATES)
        with open(f"./letter_templates/{letter_name}") as data:
            letter = data.read()
        letter = letter.replace(PLACEHOLDER, birthday_record["name"])
        email_sender.send_email(letter)
    else:
        print("No birthdays today")
