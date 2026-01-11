import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.select(selector=".StyledPropertyCardDataArea-anchor")
property_links = []
for link in links:
    property_links.append(link.get(key="href").strip())

addresses = soup.select(selector="article div div a address")
property_addresses =[]
for address in addresses:
    property_addresses.append(address.text.strip())

rents = soup.select(selector=".PropertyCardWrapper__StyledPriceLine")
property_rents = []
for rent in rents:
    property_rents.append(rent.text.strip().replace("+/mo", "").replace("/mo", "").replace("+ 1bd", "").replace("+ 1 bd", ""))

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSe_z3DBwXwqhjXM0ncqgO0blnyo2xxazAbiMxzDi3ybbIjcmw/viewform?usp=sharing&ouid=106909517235174732780"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(form_url)

wait = WebDriverWait(driver, 10)

for info in range(0, len(property_links)-1):
    address_fill = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_fill.send_keys(property_addresses[info])

    rent_fill = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    rent_fill.send_keys(property_rents[info])

    link_fill = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_fill.send_keys(property_links[info])

    submit_form = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
    submit_form.click()

    submit_another_response = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Submit another response")))
    submit_another_response.click()
    time.sleep(1)

driver.quit()
