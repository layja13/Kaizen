import requests
import random

parameters = {"amount":10, "type": "boolean"}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = []

for i in range(1,11):
    r = random.choice(data["results"])
    question_data.append(r)
