# Programs extracts property listings and extracts data from them and then inserts all data into a google form


from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from property import Property
import time

URL_SF_PROPERTY = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
URL_GOOGLE_FORM = ("YOUR_GOOGLE_FORM")

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}


properties = []


# Get the HTML page
response = requests.get(url=URL_SF_PROPERTY, headers=headers)

# Make soup
soup = BeautifulSoup(response.text, "html.parser")

# Find all property containers
list_items = soup.find_all(class_="ListItem-c11n-8-69-2__sc-10e22w8-0")


# Get adresses
addresses = [
    item.find("address").get_text()
    for item in list_items
    if item.find("address") is not None
]


# Get links
links = [
    item.find("a").get("href")
    for item in list_items
    if item.find("a") is not None and item.find("a").has_attr("href")
]


# Data cleaning of links
for index in range(0, len(links) - 1):
    if links[index][0:4] != "http":
        temp = links[index][:]
        links[index] = f"https://www.zillow.com{temp}"


# Get prices and clean data
prices = [
    item.find("span").get_text().split("+")[0]
    for item in list_items
    if item.find("span") is not None
    and item.find("span").has_attr("data-test")
    and item.find("span")["data-test"] == "property-card-price"
]


# Save all the Propery instances
for adress, price, link in zip(addresses, prices, links):
    properties.append(Property(adress, price, link))


# Initaiate webdriver
driver = webdriver.Firefox()

# Loop through all properties
for property in properties:
    driver.get(URL_GOOGLE_FORM)

    form_price = driver.find_element(
        By.XPATH,
        "/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )

    form_link = driver.find_element(
        By.XPATH,
        "/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )

    form_address = driver.find_element(
        By.XPATH,
        "/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input",
    )

    btn_send = driver.find_element(
        By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div"
    )

    form_price.send_keys(property.price)
    form_link.send_keys(property.link)
    form_address.send_keys(property.address)
    time.sleep(0.5)
    btn_send.click()
    time.sleep(0.5)


driver.close()
