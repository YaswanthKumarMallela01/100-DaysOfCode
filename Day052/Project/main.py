import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import os

'''Done so much research and experiments to get this full fledged working code. 
The INSTAGRAM when we don't on 2 step verification can be scrapable with some efforts.
I am happy to building this.'''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

insta_url = "https://www.instagram.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(insta_url)

wait = WebDriverWait(driver, 20)

email = os.getenv("BOT_EMAIL")
password = os.getenv("BOT_EMAIL_PASSWORD")

email_entry = wait.until(ec.presence_of_element_located((By.NAME, 'username')))
email_entry.send_keys(email)

password_entry = wait.until(ec.presence_of_element_located((By.NAME, 'password')))
password_entry.send_keys(password)

login_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button')))
login_button.click()

search_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "svg[aria-label='Search']")))
search_button.click()

search_text = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search input']")))
search_text.send_keys("ezsnippet")

driver.get("https://www.instagram.com/ezsnippet/")
time.sleep(2)

following = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/ezsnippet/following/']")))
following.click()

time.sleep(2)

for _ in range(10):
    buttons = driver.find_elements(By.XPATH, "//div[normalize-space()='Follow']")

    for btn in buttons:
        try:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1.5)
        except:
            pass

    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(2)

