import requests
API_key = 'a3b1c010b01d1781b95eeb31f60b40dd'

def get_data(place, days=None):
    url = (f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}')
    response = requests.get(url)
    data = response.json()
    weather_data = data['list']
    num_values = 8 * days
    forecast_data = weather_data[:num_values]
    return forecast_data

if __name__ =='__main__':
    print(get_data(place='Athens',days=3, option='Temperature'))