import requests
import random

form = ["education", "social", "recreational", "relaxation", "busywork", "diy"]

parameters = {"type": random.choice(form),
              "participants": 1}

data = requests.get(url="http://www.boredapi.com/api/activity", params=parameters)
data.raise_for_status()
activity = data.json()["activity"]

