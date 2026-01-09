import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

url = "https://appbrewery.github.io/gym/"
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
wait = WebDriverWait(driver, 2)

admin_login = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
admin_login.click()

admin_email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
admin_email_input.clear()
admin_email_input.send_keys("admin@test.com")

admin_password_input = wait.until(ec.presence_of_element_located((By.ID, "password-input")))
admin_password_input.clear()
admin_password_input.send_keys("admin123")

admin_register = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
admin_register.click()

time_machine = wait.until(ec.element_to_be_clickable((By.ID, "advance-3-days")))
time_machine.click()

log_out = wait.until(ec.element_to_be_clickable((By.ID, "logout-button")))
log_out.click()

login = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login.click()

submit = wait.until(ec.element_to_be_clickable((By.ID, "toggle-login-register")))
submit.click()

name_input = wait.until(ec.presence_of_element_located((By.ID, "name-input")))
name_input.clear()
name_input.send_keys("Yaswanth")

email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys("yashwanthkumarmallela@gmail.com")

password_input = wait.until(ec.presence_of_element_located((By.ID, "password-input")))
password_input.clear()
password_input.send_keys("@Snacks15960")

register = wait.until(ec.element_to_be_clickable((By.ID, "submit-button")))
register.click()

group_days = wait.until(
    ec.presence_of_all_elements_located(
        (
            By.XPATH,
            "//div[starts-with(@id,'day-group-tue') or starts-with(@id,'day-group-thu')]"
        )
    )
)
six_pm_classes = None
for days in group_days:
    six_pm_classes = days.find_elements(By.XPATH, ".//div[contains(@data-class-id,'1800')]")

# six_pm_classes = group_days.find_elements(
#     By.XPATH, ".//div[contains(@data-class-id,'1800')]"
# )

booked_count = 0
waitlist_count = 0
already_booked_count = 0

processed_classes = []
for day in group_days:

    day_title = day.find_element(By.TAG_NAME, "h2").text

    six_pm_classes = day.find_elements(
        By.XPATH, ".//div[contains(@data-class-id,'1800')]"
    )

    for cls in six_pm_classes:

        class_name = cls.find_element(
            By.CSS_SELECTOR, "h3[id^='class-name-']"
        ).text

        book_btn = cls.find_element(
            By.XPATH,
            ".//button[normalize-space()='Book Class' or normalize-space()='Join Waitlist' or normalize-space()='Booked' or normalize-space()='Waitlisted']"
        )

        action = book_btn.text.strip()

        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", book_btn
        )
        class_info = f"{class_name} on {day_title}"

        if action == "Booked":
            print(f"Already booked: {class_name} on {day_title}")
            already_booked_count += 1
            processed_classes.append(f"[Booked] {class_info}")

        elif action == "Waitlisted":
            print(f"Already waitlisted: {class_name} on {day_title}")
            already_booked_count += 1
            processed_classes.append(f"[Waitlisted] {class_info}")

        elif action == "Book Class":
            driver.execute_script("arguments[0].click();", book_btn)
            print(f"Successfully booked: {class_name} on {day_title}")
            booked_count += 1
            processed_classes.append(f"[New Booking] {class_info}")
            time.sleep(0.5)

        elif action == "Join Waitlist":
            driver.execute_script("arguments[0].click();", book_btn)
            print(f"Joined waitlist: {class_name} on {day_title}")
            waitlist_count += 1
            processed_classes.append(f"[New Waitlist] {class_info}")
            time.sleep(0.5)

print("\n--- BOOKING SUMMARY ---")
print(f"New bookings: {booked_count}")
print(f"New waitlist entries: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday & Thursday 6pm classes: {booked_count + waitlist_count + already_booked_count}")

print("\n--- DETAILED CLASS LIST ---")
for class_detail in processed_classes:
    print(f"  • {class_detail}")

my_bookings = driver.find_element(By.LINK_TEXT, "My Bookings")
my_bookings.click()

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))

verified_count = 0
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("SUCCESS: All bookings verified!")
else:
    print(f"MISMATCH: Missing {total_booked - verified_count} bookings")

# book_class = wait.until(ec.presence_of_all_elements_located((By.XPATH, "//button[normalize-space()='Book Class']")))
# for classes in book_class:
#     classes.click()

