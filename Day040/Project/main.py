import time
import os
import requests
from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

SHEETY_HEADERS = {
    "Authorization": f"Bearer {os.environ['SHEETY_PASSWORD']}",
    "Content-Type": "application/json"
}

ORIGIN_CITY_IATA = "IXC"  # Chandigarh


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
notification_manager = NotificationManager()

users_response = requests.get(
    url=os.environ['SHEETY_USERS_ENDPOINT'],
    headers=SHEETY_HEADERS
)
users_response.raise_for_status()

users_data = users_response.json()["users"]

customer_email_list = [user["whatIsYourEmailAddress?"] for user in users_data]

print(f"Customer emails loaded: {customer_email_list}")

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)  # Prevent API rate limit

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()


# ===================== SEARCH FLIGHTS =====================

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=180)

for destination in sheet_data:
    print(f"Checking flights to {destination['city']}")

    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    cheapest_flight = find_cheapest_flight(flights)

    print(
        f"Cheapest price: {cheapest_flight.price} | "
        f"Threshold: {destination['lowestPrice']}"
    )

    if cheapest_flight.price == "N/A":
        continue

    if cheapest_flight.price < destination["lowestPrice"]:

        if cheapest_flight.stops == 0:
            message = (
                f"Low price alert! Only INR {cheapest_flight.price} to fly direct "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
            )
        else:
            message = (
                f"Low price alert! Only INR {cheapest_flight.price} to fly "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"with {cheapest_flight.stops} stop(s), "
                f"from {cheapest_flight.out_date} to {cheapest_flight.return_date}."
            )

        print(f"Deal found for {destination['city']} → notifying users")

        # WhatsApp notification
        notification_manager.send_whatsapp(message_body=message)

        # Email notification
        notification_manager.send_emails(customer_email_list, message)
