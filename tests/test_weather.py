import datetime
import unittest
import my_toolkit.weather_forecast


class TestWeather(unittest.TestCase):
    def test_search_city_for_paris(self):
        city = my_toolkit.weather_forecast.search_city('Paris')
        self.assertEqual(city['title'], 'Paris')
        self.assertEqual(city['woeid'], 615702)

    def test_search_city_for_london(self):
        city = my_toolkit.weather_forecast.search_city('London')
        self.assertEqual(city['title'], 'London')
        self.assertEqual(city['woeid'], 44418)

    def test_search_city_for_unknown_city(self):
        city = my_toolkit.weather_forecast.search_city('Rouen')
        self.assertEqual(city, None)

    def test_search_city_ambiguous_city(self):
        my_toolkit.weather_forecast.input = lambda _: "1"
        city = my_toolkit.weather_forecast.search_city('San')
        self.assertEqual(city['title'], 'San Francisco')

    def test_weather_forecast(self):
        forecast = my_toolkit.weather_forecast.weather_forecast(44418)
        self.assertIsInstance(forecast, list, "Did you select the `consolidated_weather` key?")
        self.assertEqual(forecast[0]['applicable_date'], datetime.date.today().strftime('%Y-%m-%d'))
