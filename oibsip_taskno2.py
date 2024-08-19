import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    response = requests.get(complete_url)
    
    weather_data = response.json()
    
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temp = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        
        print(f"City: {city_name}")
        print(f"Temperature: {temp}°C")
        print(f"Weather Description: {weather_desc.capitalize()}")
    else:
        print(f"City {city_name} not found.")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = "0a22faf77edb3dcd15c5f6bc4ffc1b9f"
    
    get_weather(city_name, api_key)