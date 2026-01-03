from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

'''li:nth-of-type(2) finds 2nd li in the id = #articlecount'''
articles_en = driver.find_element(By.CSS_SELECTOR, value="#articlecount li:nth-of-type(2) a")
print(articles_en.text)
# articles_en.click()

'''Finds the link by text and click on that text'''
community_portal = driver.find_element(By.LINK_TEXT, value="Community portal")
# community_portal.click()

search_button = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
search_button.click()

'''Send key to the input box and presses enter'''
search = driver.find_element(By.NAME, value="search")  # In HTML code type attribute is also known as NAME
search.send_keys("Python", Keys.ENTER)
