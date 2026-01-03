from selenium import webdriver
from selenium.webdriver.common.by import By

'''The 2 lines below are used to keep the opened tab of the webpage intact without closing it automatically'''
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

'''driver.get("https://www.flipkart.com/nike-air-max-alpha-trainer-5-training-gym-shoes-men/p/itm5d258607a895e?pid=SHOHFCUJPUQDZ3XG&lid=LSTSHOHFCUJPUQDZ3XGFUW3KK&marketplace=FLIPKART&q=nike+shoes&store=osp%2Fcil&srno=s_1_13&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_ps&fm=search-autosuggest&iid=58da2de2-cfc3-4fed-b97c-414f5d4bedb9.SHOHFCUJPUQDZ3XG.SEARCH&ppt=sp&ppn=sp&ssid=vaaov9w9og0000001767412706373&qH=2d7d99166bc4a50f")
price_text = int(driver.find_element(By.CLASS_NAME, value="QiMO5r").text.replace("₹", "").replace(",", ""))
print(f"The price is {price_text}")'''

driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

'''In value, div is a tag and remaining 2 are classes in the div, and it finds anchor tag in this path'''
docs_link = driver.find_element(By.CSS_SELECTOR, value="div.small-widget.documentation-widget a")
print(docs_link.get_attribute("href"))

'''XPATH is a unique way to identifying path of a particular tag of a HTML. Right click on the tag and
you can see options in copy, select copy as XPATH to get the value and keep that in single quotes.'''
submit_website_bug = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_website_bug.get_attribute("href"))

# Challenge | Need to find all the dates and names of the events from Upcoming events

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events_dict = {n: {"Date": dates[n].text, "Event": event_names[n].text} for n in range(len(dates))}
print(events_dict)


# driver.close()  # Closes that particular tab
driver.quit()  # Closes or quit all the tabs and Chrome browser

