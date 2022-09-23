# Following program enters a specific instagram page and follows the accounts that the user is following

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

import time

ACCOUNT = ""
USERNAME = ""
PASSWORD = ""

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login")
        user_name = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME,"password")
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        user_name.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login_btn.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{ACCOUNT}")
        follower = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        follower.click()
        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        follow = self.driver.find_elements(By.CSS_SELECTOR, ".isgrP button")
        for button in follow:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_btn.click()
            finally:
                time.sleep(1)

        # self.driver.quit()

instagram = InstaFollower()
instagram.login()
instagram.find_followers()
instagram.follow()
