import requests as req 
key = "8080882b36004e32b08ad2df8d8d6d05" 
city = "germany" 
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}" 
response = req.get(url) 
if response.status_code == 200: 
    data = response.json() 
    print(f"Temperature:{data['main']['temp']}k") 
    print(f"weather:{data['weather'][0]['description']}") 