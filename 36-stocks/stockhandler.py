import requests
from datehandler import DateHandler
from settings import *


class StockHandler:
    def __init__(self, date_handler: DateHandler):
        self.date_handler = date_handler

        self.params = {
            "function": "TIME_SERIES_DAILY",
            "symbol": STOCK_TICKER,
            "outputsize": "compact",
            "apikey": STOCK_API_KEY,
        }

        self.response_stocks = requests.get(STOCK_API_ENDPOINT, params=self.params)
        self.calculate_return()

    def calculate_return(self):

        price_t1 = float(
            self.response_stocks.json()[LABEL_CATEGORY][self.date_handler.dates["T-1"]][
                LABEL_CLOSE
            ]
        )

        price_t2 = float(
            self.response_stocks.json()[LABEL_CATEGORY][self.date_handler.dates["T-2"]][
                LABEL_CLOSE
            ]
        )

        self.stock_return = price_t1 / price_t2 - 1
