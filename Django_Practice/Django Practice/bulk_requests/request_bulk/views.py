from django.shortcuts import render
import aiohttp
import asyncio
import requests
import time
import json
async def request1(request):
    city_list=['Lahore','Faisalabad','Rawalpindi','Multan','Gujranwala','Hyderabad','Peshawar','Islamabad','Quetta','Sargodha','Sialkot','Bahawalpur','Sukkur','Larkana','Sheikhupura','Mardan','Gujrat','Kasur','Sahiwal','Okara','Mingora','Chiniot','Nawabshah','Kamoke','Burewala','Jhelum','Sadiqabad','Khanewal','Hafizabad','Kohat','Jacobabad','Shikarpur','Muzaffargarh','Khanpur','Gojra']
    # async def get_data(session,url):
    #     async with session.get(url) as res:
    #         city_data=await res.json()
    #         return city_data
    # start_time=time.time()
    # actions=[]
    # async with aiohttp.ClientSession() as session:
    #     for city in city_list:
    #         url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=94c2916267a83950fd712c538d8d3a6e'
    #         actions.append(asyncio.ensure_future(get_data(session,url)))
    #         print('_--'*8)
    #         print(city['main']['temp'])
    #     city_res=await asyncio.gather(*actions)
        # for num in range(len(city_res)):
    weather_date=[]
    count=0
    start_time=time.time()
    for city in city_list:
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=94c2916267a83950fd712c538d8d3a6e'
        city_weather=requests.get(url).json()
        if bool(city_weather['main']['temp']) == True:
            weather={
                'city':city,
                'temperature':city_weather['main']['temp'],
                'description':city_weather['weather'][0]['description'],
                'icon':city_weather['weather'][0]['icon'],
                'humidity':city_weather['main']['humidity'],
                'pressure':city_weather['main']['pressure'],
                'windspeed':city_weather['wind']['speed'],
            }
            print('_-'*8)

            count=count+1   
            print(count, weather['temperature'])
            weather_date.append(weather)
        else:
            print('_-'*8)

            print(city)
    total_time=time.time()-start_time
    context={'weather_data':weather_date,'time':round(total_time,2)}
    return render(request,'hello.html',context)
