import sys
import requests

BASE_URI = "https://www.metaweather.com"


def search_city(query):
    '''Function search_city looking for a city in the API and returning its corresponding dict'''
    response = requests.get(f"{BASE_URI}/api/location/search/?query={query}").json()
    if not response:
        return None
    return response[0]


def weather_forecast(woeid):
    '''Function weather_forecast taking a woeid and returning \
     the consolidated_weather dict from API'''
    response = requests.get(f"{BASE_URI}/api/location/{woeid}").json()
    return response['consolidated_weather']


def get_weather_forecast():
    '''Final function returning formatted \
    weather forecast for the next 5 days'''
    query = input("City?\n> ")
    if not search_city(query):
        print('This city is not handled, sorry...')
    city = search_city(query)
    print(f"Here's the weather in {query}")
    for forecast in weather_forecast(city['woeid'])[1:6]:
        print(f"{forecast['applicable_date']}: \
        {forecast['weather_state_name']} {forecast['the_temp']}")


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)