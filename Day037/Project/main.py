import datetime
import os
import requests

""" Live Demo: https://pixe.la/v1/users/yaswanth123/graphs/graph1.html """
""" Pixela Documentation: https://docs.pixe.la/ """

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")  # Replace the value with your username
TOKEN = os.getenv("PIXELA_TOKEN")  # Replace the value with your token
GRAPH_ID = "graph1"

"""======================================================================="""
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

'''Run this piece of code only if you want to create a new user account'''
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)
"""======================================================================="""

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

'''Run this piece of code only if you want to create a new graphs by configuring the parameters'''
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
"""======================================================================="""

pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now()
# today = datetime.datetime(month=12, year=2025, day=21)

formatted_date = today.strftime("%Y%m%d")
pixel_params = {
    "date": f"{formatted_date}",  # should be in format: yyyymmdd (20251222)
    "quantity": "5.5",
}

'''Run this piece of code only if you want to post something on the graph'''
# response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
# print(response.text)
"""======================================================================="""

pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

pixel_update_params = {
    "quantity": "10.5",
}

'''Run this piece of code only if you want to update already existing data in the graph'''
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
# print(response.text)
"""======================================================================="""

pixel_delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"

'''Run this piece of code only if you want to delete the data in the graph'''
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
