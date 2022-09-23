# Stock API settings
# -----------------------
import os

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_API_ENDPOINT = "https://www.alphavantage.co/query"

FUNCTION = "TIME_SERIES_DAILY"

STOCK_TICKER = "TSLA"

LABEL_CATEGORY = "Time Series (Daily)"
LABEL_CLOSE = "4. close"


# News API settings
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
COMPANY_NAME = "Tesla Inc"
SMS_NR_ARTICLES = 2


# SMS Api settings
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
ACCOUNT_TOKEN = os.environ.get("ACCOUNT_TOKEN")
NR_FROM = os.environ.get("NR_FROM")
NR_TO = os.environ.get("NR_TO")

# Main settings
RETURN_THRESHOLD = 0.02
DAYS = ["Monday", "Tuesday", "Wednsday", "Thurday", "Friday", "Satuday", "Sunday"]
