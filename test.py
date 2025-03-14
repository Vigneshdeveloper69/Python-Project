import requests

def get_weather(city):
    api_key = "235f57d5370f7a4be2332cf46cefd2f5"  # Replace with your OpenWeather API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return f"Error: {response.status_code}, {response.json().get('message', 'Unknown error')}"

# Example usage
city_name = input("Enter city name: ")
weather_info = get_weather(city_name)

if isinstance(weather_info, dict):
    print(f"Weather in {weather_info['city']}:")
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Humidity: {weather_info['humidity']}%")
    print(f"Condition: {weather_info['description']}")
else:
    print(weather_info)
