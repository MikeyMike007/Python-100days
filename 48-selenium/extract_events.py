# Example of use of selenium webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By

dates = []

# Print all upcoming events from wwww.python.org
URL = "https://www.python.oorg/"

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

event_table = driver.find_element(
    By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul'
)


links = event_table.find_elements(By.TAG_NAME, "a")
date_data = event_table.find_elements(By.TAG_NAME, "time")

# The date exists in an atttribute called datetime inside the time bracket
for date in date_data:
    dates.append(date.get_attribute("datetime"))

# Print out all data
for link, date in zip(links, dates):
    print(f"Date: {date[:10]} - Event: {link.text}")
