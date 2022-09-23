# Following program monitors a product on Amazon for price changes.
# If the price declines under a threshold price, an email will be sent to user

from bs4 import BeautifulSoup
import requests
import smtplib
import os

URL = "https://www.amazon.se/SONGMICS-sammetsgalgar-lastkapacitet-vridbara-CRF026P03/dp/B089NGXH6T?ref_=Oct_DLandingS_D_2b8fed81_60&smid=A3W1YAJZVE78ZY"
PARSER = "html.parser"
PRICE_TARGET = 300
EMAIL = "YOUR_EMAIL"
SMTP_ADRESS = "YOUR_SMTP_SERVER"
APP_PASSWORD = os.environ.get("SECRET_PASSWORD")
TITLE = "TITLE OF PRODUCT"

respond = requests.get(url=URL, headers={"User-Agent": "Defined"})

soup = BeautifulSoup(respond.text, PARSER)

price_data = soup.find_all(name="span", class_="a-price-whole")
price = int(price_data[0].getText().strip(","))
print(price)

if price < PRICE_TARGET:
    message = f"{TITLE} is now {price}"

    with smtplib.SMTP(SMTP_ADRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, APP_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}",
        )
