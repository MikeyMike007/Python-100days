from datehandler import DateHandler
from stockhandler import StockHandler
import requests
from settings import *



class NewsHandler:
    def __init__(self, date_handler: DateHandler, stock_handler: StockHandler):
        self.date_handler = date_handler
        self.stock_handler = stock_handler

        self.params = {
            "q": COMPANY_NAME,
            "from": self.date_handler.dates["T-1"],
            "to": self.date_handler.dates["T-1"],
            "sortBy": "popularity",
            "apiKey": NEWS_API_KEY,
        }

        self.response = requests.get(NEWS_API_ENDPOINT, params=self.params)
        self.articles = []
        self.read_news(SMS_NR_ARTICLES)

    def read_news(self, nr_articles):

        for article_nr in range(0, nr_articles):
            title = self.response.json()["articles"][article_nr]["title"]
            description = self.response.json()["articles"][article_nr]["description"]

            news = f""" \
            {STOCK_TICKER}: {"🔺" if self.stock_handler.stock_return > 0 else "🔻" } {round(self.stock_handler.stock_return * 100, 2)}% \

            Headline: {title}

            Brief: 
            ----------------------------------
            {description}
            """

            self.articles.append(news)
