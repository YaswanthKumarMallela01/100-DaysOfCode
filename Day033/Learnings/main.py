import requests
from datetime import *


'''An API (Application Programming Interface) is a set of rules and tools that lets 
different software applications communicate and share data, acting as a "middleman" 
or contract between them, like a waiter taking your order (request) to the kitchen 
(server) for food (data). '''

'''API endpoint is, the specific URL where an application programming interface (API) 
receives requests and sends responses.An API endpoint is more than just a URL. 
It's a structured address that includes several important parts'''

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)  # It prints response code of 200

'''A response code, or HTTP status code, is a three-digit number sent by a 
server in response to a client's request (like a web browser or API client)'''
'''If you see something like:
        1XX - Hold On
        2XX - Here you go
        3XX - Go Away(You don't have permission)
        4XX - You Screwed Up(May be the website doesn't exist)
        5XX - I Screwed Up(Server side problem)'''

response.raise_for_status()  # Checks for any other response codes and raises an exception

data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (latitude, longitude)

'''API parameters are options or variables passed with an API request to influence 
the response or behavior of the API endpoint. They serve as inputs that allow the 
client to filter data, specify the format, handle authentication, or identify specific resources.'''

'''API parameters of sunrise and sunset api(https://api.sunrise-sunset.org/json)Looks like:
        API with Parameters: https://api.sunrise-sunset.org/json?lan=20.593683&lng=78.962883&formatted=0
        Before starting the parameters, '?' symbol should be kept.
        Each parameters(lan, lng, formatted) is separated by '&' without any spaces.
        The names of the parameters are mentioned in the respected api webpage'''

parameters = {
    "lat": 20.593683,
    "lng": 78.962883,
    "formatted": 0
}

response_sun = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()
data_sun = response_sun.json()

'''The actual out put for sunrise and sunset is:
        2025-12-13T01:10:08+00:00
        2025-12-13T12:06:30+00:00
which is not in a format that we can use.
By splitting the sunrise and sunset by 'T' which is in the middle, then output looks like:
        ["2025-12-13", "01:10:08+00:00"]
        ["2025-12-13", "12:06:30+00:00"]
Again splitting index 1 data with ':' seperator the data looks like:
        ['01', '10', '08+00', '00']
        ['12', '06', '30+00', '00']
And we need to get number at index 0, which represents the sunrise and sunset hours, that's why
we specified [0] at the end.'''

sunrise = data_sun["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data_sun["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
