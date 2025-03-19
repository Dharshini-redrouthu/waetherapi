import requests as req

key = "8080882b36004e32b08ad2df8d8d6d05" 
city = "germany" 
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

response = req.get(url)

if response.status_code == 200:
    data = response.json()
    temp_k = data['main']['temp']
    temp_c = temp_k - 273.15
    weather_desc = data['weather'][0]['description']
    print(f"Temperature: {temp_c:.2f}°C")
    print(f"Weather: {weather_desc}")
else:
    print("Failed to get the weather data. Please check the city name or API key.")
