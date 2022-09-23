from twilio.rest import Client
from newshandler import NewsHandler
from settings import *


class Sms:
    def __init__(self, news_handler: NewsHandler):
        self.news_handler = news_handler
        # self.client = Client(ACCOUNT_SID, ACCOUNT_TOKEN)
        self.messages = []

    def send_sms_news(self):

        for article in self.news_handler.articles:
            # Code to send sms
            message = self.client.messages.create(
                body=article,
                from_=NR_FROM,
                to=NR_TO,
            )

            self.messages.append(message)
