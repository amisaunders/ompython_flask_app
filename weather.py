# weather.py
# -*- coding: utf-8 -*-
local_encoding = 'cp850' 

import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_weather(address):
	api_key = os.environ['WEATHER_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	return "{} and {}° in {}".format(summary, temperature, address)

#  \xb0 \N{DEGREE SIGN      , other ways to express ° degree symbol

# print(get_weather())


#######################################
#  local_encoding = 'cp850'    # adapt for other encodings
# deg = u'\xb0'.encode(local_encoding)
# print(deg)
# degreeChar = u'\N{DEGREE SIGN}'
# deg = u'\xc2\xb0'.encode(local_encoding)
# print(degreeChar)

#forecast = forecastio.load_forecast(api_key, lat, lng).currently()
#print("{} and {}".format(forecast.summary, forecast.temperature))



	# forecast = forecastio.load_forecast(api_key, lat, lng)
	# print(forecast.currently())
	# print(forecast.currently().summary)
	# print(forecast.currently().temperature)
	# print(forecast.currently().precipProbability)

	#print (forecast.hourly())
	# print(forecast.hourly().temperature)




