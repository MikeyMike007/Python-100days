# Example of use of selenium webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)
cookie = driver.find_element(By.ID, "langSelect-EN")
time.sleep(5)
cookie.click()
time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")

while True:
    cookie.click()
