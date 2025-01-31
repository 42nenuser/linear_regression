import requests

url = "http://127.0.0.1:8000/api/predict/"
data = {"km": 120000}
response = requests.post(url, json=data)
print(response.json())
