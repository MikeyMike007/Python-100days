
# Example of use of selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.amazon.se/SONGMICS-sammetsgalgar-lastkapacitet-vridbara-CRF026P03/dp/B089NGXH6T?ref_=Oct_DLandingS_D_2b8fed81_64&smid=A3W1YAJZVE78ZY"

driver = webdriver.Firefox()
driver.get(URL)

price = driver.find_element(By.CLASS_NAME, "apexPriceToPay")
print(price.text)
print(price.get_attribute("data-a-size"))  # Other attributes in the HTML tag


# XPATH can be used if there is no unique id or class that defines the data we want to scrape
price = driver.find_element(
    By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]'
)
print(price.text)


driver.close()
