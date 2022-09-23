# See if stock has decreased in value and if true, send a sms with news about the company

from datehandler import DateHandler
from stockhandler import StockHandler
from newshandler import NewsHandler
from sms import Sms
from settings import *



date_handler = DateHandler()
stock_handler = StockHandler(date_handler)
news_handler = NewsHandler(date_handler, stock_handler)
if (
    stock_handler.stock_return <= -RETURN_THRESHOLD
    or stock_handler.stock_return >= RETURN_THRESHOLD
):
    sms = Sms(news_handler)
    sms.send_sms_news()

else:
    print("Nothing to report today - Not sending SMS")
