import requests, json 
import Griffin
	# enter your api key here 
api_key = "b73770542be8e14c0c9fb12173dd6198"

def weather():
        Griffin.speak("tell me the city in which you want to know the weather")
        city_name=Griffin.input_speech()
        #city_name=input("Enter city name.....")
        complete_url="http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&APPID="+api_key
        response=requests.get(complete_url)
        x=response.json()
        print(x)
        if x['cod'] != '404':
                y=x["main"]
                w=x["wind"]
                z=x["weather"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                weather_description = z[0]["description"]
                Griffin.speak("there is "+weather_description+" in "+city_name)
                Griffin.speak("the average temprature is "+str(int(current_temperature-273.15))+" degree celsius")
                Griffin.speak("the humidity is "+str(current_humidity)+" per cent")
        else:
                Griffin.speak("City not found!!!!")

