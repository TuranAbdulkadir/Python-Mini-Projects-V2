# Requirement: pip install requests
import requests

API_KEY = "bd5e378503939ddaee76f12ad7a97608" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric&lang=en"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    
    print(f"\n--- {city.upper()} WEATHER ---")
    print(f"Status: {weather.capitalize()}")
    print(f"Temperature: {temp}°C")
else:
    print("Error: City not found or connection issue.")