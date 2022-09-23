from datetime import datetime, timedelta
from settings import *



class DateHandler:
    def __init__(self):
        self.today_dt = datetime.now()

        # Lets say we look at Fridays stock market on Sundays as well
        if self.is_sunday():
            self.today_dt -= timedelta(days=1)

        self.yestersday_dt = self.today_dt - timedelta(days=1)
        self.day_before_yesterday_dt = self.today_dt - timedelta(days=2)

        self.today_date = str(self.today_dt.date())
        self.yestersday_date = str(self.yestersday_dt.date())
        self.day_before_yesterday_date = str(self.day_before_yesterday_dt.date())
        self.dates = {
            "T": self.today_date,
            "T-1": self.yestersday_date,
            "T-2": self.day_before_yesterday_date,
        }

    def is_sunday(self):

        return True if DAYS[self.today_dt.weekday()] == "Sunday" else False
