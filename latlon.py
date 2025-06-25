import requests

def get_lat_lon(city_name, api_key):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if data:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    else:
        return None, None

# Example usage
#api_key = '921e19f4a9efe753614e783829875323'
#city_name = 'Bangalore'
#lat, lon = get_lat_lon(city_name, '921e19f4a9efe753614e783829875323')
#print(f"Latitude: {lat}, Longitude: {lon}")