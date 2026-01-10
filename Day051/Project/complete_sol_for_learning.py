from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0
        self.wait = WebDriverWait(self.driver, 5)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        privacy_button = self.wait.until(ec.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
        time.sleep(2)
        privacy_button.click()

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(50)

        self.up = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'
        ).text

        self.down = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span'
        ).text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)

        email = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
        )
        password = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
        )

        email.send_keys(TWITTER_EMAIL)
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(6)

        tweet_compose = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
        )

        tweet = (
            f"Hey Internet Provider, why is my internet speed "
            f"{self.down}down/{self.up}up when I pay for "
            f"{PROMISED_DOWN}down/{PROMISED_UP}up?"
        )
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]'
        )
        tweet_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
