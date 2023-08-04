import requests
import json

url = "https://ktpai-iee-55b4bd81198e.herokuapp.com/query"

headers = {"Content-Type": "application/json"}

data = {
    "question": "Who is leon jacobson?"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())
