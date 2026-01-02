import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import messagebox

year = str(input("Enter year you want to jump into(yyyy): ")) or "2000"
month = str(input("Enter month(mm): ")) or "01"
day = str(input("Enter day(dd): ")) or "01"


def is_valid_date(y, m, d):
    return (
        y.isdigit() and len(y) == 4 and
        m.isdigit() and 1 <= int(m) <= 12 and
        d.isdigit() and 1 <= int(d) <= 31
    )


if not is_valid_date(year, month, day):
    raise ValueError("Invalid date input. Use YYYY MM DD.")

overall_date = str(year + month + day)

url = f"https://www.officialcharts.com/charts/singles-chart/{overall_date}/"

response = requests.get(url)
webpage = response.text

soup = BeautifulSoup(markup=webpage, features="html.parser")

song_titles = []

song_rows = soup.select(selector="div p a span:nth-of-type(2)")
songs = []
for row in song_rows:
    songs.append(row.get_text(strip=True))

print(songs)

choice = messagebox.askyesno(title="Save as CSV", message="Do you want to save songs data to csv?")

if choice:
    data = pd.DataFrame({"Song Title": songs})
    df = data.to_csv(f"Top_100_songs({day}-{month}-{year})")
    messagebox.showinfo(title="Saved", message=f"Successfully saved as Top_100_songs({day}-{month}-{year})")

'''As you can see in report.png, i couldn't able to create spotify app as it is in underdevelopment
or temporarily closed. So i added few other functions to save all web scrapped songs in CSV format.
I will continuously check if the developer features came back in spotify and will try to create a full
fledged application.
I will also keep full solution by Angela Yu from community page in files.'''
