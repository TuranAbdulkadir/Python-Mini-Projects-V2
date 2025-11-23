import requests
url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_demo_key&currencies=TRY,USD"
res = requests.get(url).json()
print(f"1 USD = {res['data']['TRY']:.2f} TRY")