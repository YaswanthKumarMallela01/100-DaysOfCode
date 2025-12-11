import smtplib
import os

'''SMTP stands for Simple Mail Transfer Protocol'''

'''If A (Gmail account holder) wanted to send email to B (Yahoo account holder), the email will travel
like this    A --> Gmail mail server --> Yahoo mail server --> B. And SMTP acts as a postman that knows
from where to where the mail should travel.'''

'''SMTP Information- For
Gmail - smtp.gmail.com
Hotmail - smtp.live.com
Yahoo - smtp.mail.yahoo.com 
'''

'''my_email = Your email address
my_password = Your APP Password.
To get app password, go to your account settings and turn on 2 step
verification. After that search for App Passwords in account settings, go to that option and create
a new password for you project. Fo this project i named it as "Birthday_Wisher" and generate password.
Copy Paste the generated password here in the code in my_password.'''

MY_EMAIL = os.getenv("MY_EMAIL")  # Remove this and add your mail account in strings
MY_PASSWORD = os.getenv("MY_PASSWORD")  # Remove this and add your mail account App Password in strings
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
'''TLS stands for Transport Layer Security. It's a way of securing connection to email server'''
connection.login(user=MY_EMAIL, password=MY_PASSWORD)
connection.sendmail(from_addr=MY_EMAIL, to_addrs="yashwanthkumarmallela@outlook.com", msg="Hello")
connection.close()

