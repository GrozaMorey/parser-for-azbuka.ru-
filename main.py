import requests
from bs4 import BeautifulSoup
from datetime import timedelta
import datetime
import json

dates = datetime.date(2022, 1, 1)


link = "https://azbyka.ru/days/"
data = {}
while dates != datetime.date(2023, 1, 1):
    request = requests.get(link + str(dates)).text
    soup = BeautifulSoup(request, "lxml")
    block = soup.find_all('a', class_="saint-href")
    block_group = soup.find_all('a', class_="saints-group-href")
    saint = []
    for i in block:
         saint.append(i.text)
    for k in block_group:
        saint.append(k.text)
    data[f'{dates}'] = saint
    print(dates)
    dates += timedelta(days=1)

with open("date.json", "w") as outfile:
    json.dump(data, outfile)