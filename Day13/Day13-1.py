import json
import requests
fruit = input("Which fruit you want to know better? ")
url = "https://www.fruityvice.com/api/fruit/" + fruit
response = requests.get(url)
print(response.status_code)
print(response.text)
data_from_url = response.json()

with open("data_from_url.json", mode="w") as write_file:
    json.dump(data_from_url, write_file, indent=4)


import time

for i in range(10):
    print(i)
    time.sleep(0.3)

