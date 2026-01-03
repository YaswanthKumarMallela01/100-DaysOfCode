from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Yaswanth Kumar")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Mallela")

email = driver.find_element(By.NAME, value="email")
email.send_keys("yashwanthkumarmallela@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.send_keys(Keys.ENTER)



