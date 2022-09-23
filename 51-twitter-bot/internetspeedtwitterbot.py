from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

EMAIL = ""
PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.driver = webdriver.Firefox()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):

        # Go to site
        self.driver.get("https://www.speedtest.net/")
        time.sleep(20)

        # Accept terms
        accept_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        time.sleep(10)
        accept_btn.click()

        # Find "Go" button
        time.sleep(10)
        go_button = self.driver.find_element(
            By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a"
        )
        go_button.click()

        # Get speeds
        time.sleep(40)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

    def login(self):
        self.driver.get("https://twitter.com/login")

        # Click "Sign in with Google"
        time.sleep(5)
        google_login_button = self.driver.find_element_by_css_selector(
            ".S9gUrf-YoZ4jf iframe"
        )
        google_login_button.click()

        # There is a new Google Sign in window. Switch to it
        time.sleep(3)
        window_base = self.driver.window_handles[0]
        window_google = self.driver.window_handles[1]
        self.driver.switch_to.window(window_google)

        # Enter username and press enter
        time.sleep(2)
        login_field = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        login_field.send_keys(EMAIL)
        login_field.send_keys(Keys.ENTER)

        # Enter password and press enter
        time.sleep(2)
        password_field = self.driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input'
        )
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.ENTER)

        # Switch to main window
        time.sleep(3)
        self.driver.switch_to.window(window_base)

    def tweet(self, message):
        time.sleep(3)

        # Get tweetfield
        tweet_field = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div['
            "2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div"
        )

        # Send message to tweetfield
        tweet_field.send_keys(message)

        # Get tweet button
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div['
            "2]/main/div/div/div/div/div/div[2]/div/div[2]/div["
            "1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]"
        )

        # Click on tweet button
        tweet_button.click()
        self.driver.close()
