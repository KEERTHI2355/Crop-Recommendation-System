import openmeteo_requests
from latlon import get_lat_lon
import requests_cache
import pandas as pd
import numpy as np
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below

from datetime import date
from dateutil.relativedelta import relativedelta

start = date.today()
end = start + relativedelta(months=3)
def get_weather(city_name):
	#city_name = 'Bangalore'
	lat, lon = get_lat_lon(city_name, 'XXXXXXXXXXXXXXXXX')
	#add your app code in the place of XXXXXXXXXXXXXXXXX
	url = "https://climate-api.open-meteo.com/v1/climate"
	params = {
		"latitude": lat,
		"longitude": lon,
		"start_date": start.strftime("%Y-%m-%d"),
		"end_date": end.strftime("%Y-%m-%d"),
		"models": ["CMCC_CM2_VHR4", "FGOALS_f3_H", "HiRAM_SIT_HR", "MRI_AGCM3_2_S", "EC_Earth3P_HR", "MPI_ESM1_2_XR", "NICAM16_8S"],
		"daily": ["temperature_2m_mean", "relative_humidity_2m_mean", "precipitation_sum"]
	}
	responses = openmeteo.weather_api(url, params=params)

	# Process first location. Add a for-loop for multiple locations or weather models
	response = responses[0]
	#print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
	#print(f"Elevation {response.Elevation()} m asl")
	#print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
	#print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

	# Process daily data. The order of variables needs to be the same as requested.
	daily = response.Daily()
	daily_temperature_2m_mean = daily.Variables(0).ValuesAsNumpy()
	daily_relative_humidity_2m_mean = daily.Variables(1).ValuesAsNumpy()
	daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()

	daily_data = {"date": pd.date_range(
		start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
		end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
		freq = pd.Timedelta(seconds = daily.Interval()),
		inclusive = "left"
	)}
	daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
	daily_data["relative_humidity_2m_mean"] = daily_relative_humidity_2m_mean
	daily_data["precipitation_sum"] = daily_precipitation_sum

	daily_dataframe = pd.DataFrame(data = daily_data)

	temp=np.mean(daily_dataframe.temperature_2m_mean)
	hum=np.mean(daily_dataframe.relative_humidity_2m_mean)
	rain=(np.sum(daily_dataframe.precipitation_sum))*0.2

	return temp,hum,rain
#(daily_dataframe)
#print(np.mean(daily_dataframe.temperature_2m_mean))
#print(np.mean(daily_dataframe.relative_humidity_2m_mean))
#print(np.sum(daily_dataframe.precipitation_sum))
