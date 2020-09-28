import requests
import pytemperature
from geopy.geocoders import Nominatim
import pandas as pd
import datetime



def get_weather_data(city, country=None):

    """ Takes a city as argument and return the current temperature, pressure, huminity and what the sky looks like"""

    try:
        tempObject = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=5a0bffb1cd038523e6b4a23076521bab&lang=nl").json()
        temp = round(pytemperature.k2c(float(tempObject['main']['temp'])),2)
        pressure = tempObject['main']['pressure']
        huminity = tempObject['main']['humidity']
        sky = tempObject['weather'][0]['description']
        wind = round((tempObject['wind']['speed'] * 3.6))
        try:
            rain = tempObject['rain']['1h']
            return  temp , pressure, huminity, sky, wind, rain
        except KeyError:
            None

        return temp , pressure, huminity, sky, wind
        return tempObject

    except KeyError:
        return False

def get_hourly_forecast(city,country=None):
    """ Function that takes a city name ans hourly/daily as input and outputs a dataframe with wather data"""

    def to_celcius(kelvin):
        return round(pytemperature.k2c(float(kelvin)),2)

    def time_convert(stamp):
        fmt = "%H:%M %d-%m"
        t = datetime.datetime.fromtimestamp(float(stamp))
        return t.strftime(fmt)

    try:
        geolocator = Nominatim(user_agent='myapplication')
        location = geolocator.geocode(city)
        lat = location.latitude
        lon = location.longitude
        try:
            forcastObject = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,daily&appid=5a0bffb1cd038523e6b4a23076521bab").json()
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            df = pd.DataFrame.from_dict(forcastObject)
            dataColumns = pd.json_normalize(df['hourly'])

            dataColumns['temp'] = dataColumns['temp'].apply(to_celcius)
            dataColumns['dt']  = dataColumns['dt'].apply(time_convert)
            dataColumns['index'] = dataColumns.index

            return dataColumns[['index','temp']]


        except KeyError:
            return "False"

    except AttributeError:
        "False"



def get_daily_forecast(city,country=None):

    def to_celcius(kelvin):
        return round(pytemperature.k2c(float(kelvin)),2)

    """ Function that takes a city name ans hourly/daily as input and outputs a dataframe with weather data"""

    try:
        geolocator = Nominatim(user_agent='myapplication')
        location = geolocator.geocode(city)
        lat = location.latitude
        lon = location.longitude
        try:
            forcastObject = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly&appid=5a0bffb1cd038523e6b4a23076521bab").json()
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            df = pd.DataFrame.from_dict(forcastObject)
            dataColumns =   pd.json_normalize(df['daily'])

            dataColumns['index'] = dataColumns.index
            dataColumns['temp.day'] = dataColumns['temp.day'].apply(to_celcius)
            dataColumns['temp.night'] = dataColumns['temp.night'].apply(to_celcius)
            return dataColumns[['temp.day','temp.night','humidity','clouds','rain','wind_speed']]

        except KeyError:
            return "False"

    except AttributeError:
        "False"


print(get_daily_forecast('Amsterdam',country=None))
