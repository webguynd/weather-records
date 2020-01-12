import requests
import sqlite3

"""
You will need to supply your own API key!
See openweathermap.org
"""

#######################
#    CONFIGURATION    #
#######################

CITY_CODE = 5804127
TEMP_UNIT = "f" #Accepts 'f'(fahrenheit), 'c' celsius, or 'k' kelvin
DB_PATH = "weather-records.db"
API_KEY = ""

URL = "http://api.openweathermap.org/data/2.5/weather"
PARAMS = {"id" : CITY_CODE, "APPID" : API_KEY}

def retrieve_weather_data():
    request = requests.get(url = URL, params = PARAMS)
    results = request.json()

    currentConditions = results['weather'][0]['main']
    currentTemp = results['main']['temp']
    currentWind = results['wind']['speed']
    currentPercip = results['rain']['1h']

    INSERT_DATA = 'INSERT INTO weather VALUES(NULL, "{}", {}, {}, {})'.format(currentConditions, currentTemp,currentWind,currentPercip)

    if(TEMP_UNIT == "f"):
        currentTemp = (currentTemp - 273.15) * 9/5 +32
    elif(TEMP_UNIT == "c"):
        currentTemp = currentTemp - 273.15
    else:
        currentTemp = currentTemp
    
    #DEBUG
    print(currentConditions) 
    print(currentTemp) 
    print(currentWind) 
    print(currentPercip)
    
    try:
        sqlCon = sqlite3.connect(DB_PATH)
        cursor = sqlCon.cursor()
    except sqlite3.Error as error:
        print("Error: ", error)
    finally:
        if(sqlCon):
            cursor.execute(INSERT_DATA)
            sqlCon.commit()
            cursor.close()
            sqlCon.close()








    




