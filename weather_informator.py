import requests


def get_weather_now(city):
    city_name_url = 'http://api.openweathermap.org/geo/1.0/direct'
    name_params = {
        'q': city,
        'appid': 'cb4c7397def9eea2d33909d8ecdc5bc5'
    }
    city_res = requests.get(city_name_url, params=name_params).json()
    latitude = city_res[0]['lat']
    longitude = city_res[0]['lon']

    weather_url = 'https://api.openweathermap.org/data/2.5/weather'
    weather_params = {
        'lat': latitude,
        'lon': longitude,
        'appid': 'cb4c7397def9eea2d33909d8ecdc5bc5',
        'units': 'metric'
    }
    weather_res = requests.get(weather_url, params=weather_params).json()
    temperature = weather_res['main']['temp']
    if temperature <= 5:
        advice = ('Brr... It\'s cold outside. '
                  'Don\'t forget your mittens and a warm cap!')
    elif temperature >= 20:
        advice = ('Ooofff... What a heat! '
                  'Wish I had a swimming pool of icy water right here!')
    else:
        advice = ('Hmmm... Not hot, not cold. '
                  'Dress according to the weather and take care.')
    answer_template = ('Current temperature in {}: {} Celcius.'
                       '\nWeather advice: {}')
    return answer_template.format(city, weather_res['main']['temp'], advice)


# city = input('Please, type the name of city: ')
print(get_weather_now('Rostov-on-Don'))
print(get_weather_now('Moscow'))
print(get_weather_now('Ubud'))
