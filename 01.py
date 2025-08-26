import requests

city_name = input("Enter the city name : ")
city_name = city_name.capitalize()
API_key = '81803dda60468b87287a879ab670f0b5'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"

try:
    response = requests.get(url)

    # if response.status_code == 200:
    #     print("yee! we hit the API")

    data = response.json()
    if data.get("cod") == "404":
        print("City not found. Please check the spelling")


    print(f"\nTemperature : {data["main"]["temp"]} deg Celcius") 
    print("Humidity :",data["main"]["humidity"]) 
    print("weather description : ",data["weather"][0]["description"]) 

except requests.exceptions.ConnectionError:
    print("❌ No internet connection. Please check your network.")