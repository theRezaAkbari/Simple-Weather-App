import requests
api_key="f5d61d63f50b997df9361bbdb365277d"

def get_weather(city):
    complete_url=f"http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=f5d61d63f50b997df9361bbdb365277d"
    respone=requests.get(complete_url)

    if respone.status_code==200:
        data=respone.json()

        weather=data["weather"][0]["description"]
        temp=data["main"]["temp"]
        temp_celsius=round(temp-273.15,2)
        humidity=data["main"]["humidity"]
        wind_speed=data["wind"]["speed"]

        print(f"City: {city}")
        print(f"weather: {weather}")
        print(f"Temperature: {temp_celsius}")
        print(f"Hunidity: {humidity}")
        print(f"wind speed:{wind_speed}")
    else:
        print("Error. please try again")

city=input("Enter a city name: ")

get_weather(city)