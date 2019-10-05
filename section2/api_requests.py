import requests

APP_ID = "0636e1c7348b402c8bac4c8b0c178f6b"
END_POINT = "https://openexchangerates.org/api/latest.json"
BASE = "INR"

url = f"{END_POINT}?app_id={APP_ID}&base={BASE}"

response = requests.get(url)

exchange_rate = response.json()
print(exchange_rate)