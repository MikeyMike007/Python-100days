# Example of use of selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://en.wikipedia.org/wiki/Main_Page"
driver = webdriver.Firefox()

driver.get(URL)

# Can also use find_element(By.CSS_SELECTOR, "#articlecount a")
stat = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(stat.text)

all_portals = driver.find_element(By.LINK_TEXT, "Commons")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
