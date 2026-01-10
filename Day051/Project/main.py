import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

'''Twitter is a JavaScript-heavy platform with aggressive bot-detection mechanisms.
The DOM structure is highly dynamic and frequently changes, making locators unstable.
Most meaningful interactions require authentication, increasing automation failure risk. I have done
the project till getting internet speeds and redirecting to X formally known as Twitter. I kept 
complete code in complete_sol_for_learning.py which is written few years back for learning. I am
feeling bad to end this project here.'''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

speed_test_url = "https://www.speedtest.net/"
driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 5)
driver.get(speed_test_url)
privacy_button = wait.until(ec.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
time.sleep(2)
privacy_button.click()

test_speed = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')))
test_speed.click()
time.sleep(50)
download_speed = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))).text
print(f"Download Speed: {download_speed}")
upload_speed = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))).text
print(f"Upload Speed: {upload_speed}")

twitter_url = "https://x.com/home"
driver.get(twitter_url)

twitter_mail = ""
twitter_pass = ""
# time.sleep(10)
# email_fill = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
# email_fill.send_keys(twitter_mail)

