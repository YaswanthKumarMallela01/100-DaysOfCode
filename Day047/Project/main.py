import requests
from bs4 import BeautifulSoup
import smtplib
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

url = "https://www.amazon.in/soundcore-Bluetooth-Headphones-Cancelling-Personalization/dp/B0C3HCD34R/ref=sr_1_3?crid=20709VJBWOG5K&dib=eyJ2IjoiMSJ9.XnLGUahQuULqZX_hQ_GIZ5s9bgIzggQl_k-j6dCfOG1GgwU0q219aRD11FaIvUJvyXdUHtnEviEc9Q89ipOXxo1HslAY-xdc8K3fI7eb1I-6OtnaJUPEiY8vnt1Fk4gPU4NbStRbm1OhTpOEGco5b1gL1wncMnCm60O6iMfZQ4uLzR9KB5G0ml8lqStMRTvIzYlAfcU2pqRX317H8MLNCZdOSQOdrpRzhNNfnzXe9Jg.GsyPM3RNgZ8QPYOpaYA_hkmNa3oBXH1BBDudvKoFWZI&dib_tag=se&keywords=soundcore%2Bq20i&nsdOptOutParam=true&qid=1767361060&sprefix=%2Caps%2C439&sr=8-3&th=1"
response = requests.get(url, headers=headers)
website = response.text

soup = BeautifulSoup(website, "html.parser")

price_text = soup.select_one(selector=".aok-offscreen").get_text().split(" ")[1]
price = float(price_text.replace("₹", "").replace(",", "").strip())
print(price)

product_title = " ".join(
    soup.select_one("#productTitle").get_text().split()
)

if not price or not product_title:
    raise RuntimeError("Required page elements not found")

BUY_PRICE = 4000
if price < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        my_email = os.getenv("MY_EMAIL")
        connection.login(user=my_email, password=os.getenv("MY_PASSWORD"))
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Price Alert!\n\n{product_title}\nPrice has been reduced to ₹{price}. Grab the deal. Visit {url} for more product details.")
        print("Message Sent successfully!")
else:
    print("The price didn't dropped.")

