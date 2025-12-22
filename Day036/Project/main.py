import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"  # 4 lettered stock name
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv("STOCKS_API"),
}


response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:  # > 0 is a sample measure to test the code
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percentage = round((difference / float(day_before_yesterday_closing_price)) * 100)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if abs(diff_percentage) < 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percentage}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
    client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="whatsapp:" + os.getenv("TWILIO_WHATSAPP_NO"),
            to="whatsapp:" + os.getenv("MY_NO")
        )
        print(message.body)

