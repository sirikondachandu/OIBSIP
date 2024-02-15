import requests
api_key='11d156e2eaec4ca6948fcbc05ad889a1'
user_input=input("Enter city:")
base_url="http://api.openweathermap.org/data/2.5/weather?"
complete_url=base_url+"appid="+api_key+"&q="+user_input
weather_data=requests.get(complete_url)

if weather_data.json()['cod']=='404':
    print(f"No city found")
else:
    weather=weather_data.json()['weather'][0]['main']
    temp=round(weather_data.json()['main']['temp'])
    print(f"The weather in {user_input} is:{weather}")
    print(f"The Temperature in {user_input} is:{temp} Fahrehit")



