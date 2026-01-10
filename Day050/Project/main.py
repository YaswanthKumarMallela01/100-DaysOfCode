from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

'''As today's websites are more secure, they always ask for OTP to phone number or Approving from
email or getting a text message to whatsapp. It is not possible to automate all that using selenium.
I have built this project upto authenticating to Facebook. If you want complete program which was 
written few years back for learning i will provide in complete_sol_for_learning.py file.'''

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://tinder.com/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

wait = WebDriverWait(driver, 20)
base_window = driver.window_handles[0]

agreement = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="q-1329786438"]/div/div[2]/div/div[2]/div[1]/div[1]/button')))
agreement.click()

login_home = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="q-1329786438"]/div/div[1]/div/main/div[1]/div/div/div/div/div[1]/header/div/div[2]/div[2]/a')))
login_home.click()

login_with_facebook = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="q-1108446002"]/div/div[1]/div/div[2]/div/div/div[2]/div[2]/span/div[2]/button')))
login_with_facebook.click()

fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

number = wait.until(ec.presence_of_element_located((By.ID, "email")))
number.send_keys("Your_Email_Or_Phone_Number")

password = wait.until(ec.presence_of_element_located((By.ID, "pass")))
password.send_keys("Your_Facebook_Password")

fb_login = wait.until(ec.element_to_be_clickable((By.NAME, "login")))
fb_login.click()
# print(driver.current_url)

WebDriverWait(driver, 15).until(
    ec.url_contains("privacy/consent")
)

# print(driver.current_url)

continue_as = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="mount_0_0_Rz"]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div/div/div/div')))
continue_as.click()

# old_url = driver.current_url
# print(old_url)
# new_url = wait.until(ec.url_changes(old_url))
# print(driver.current_url)

# driver.switch_to.window(base_window)
# print(driver.title)
