# test_weather.py

import unittest
from unittest.mock import patch
from app.routers.weather import get_temperature, square

class TestWeatherAPI(unittest.TestCase):

    @patch('app.routers.weather.requests.get')  # Patch 'requests.get' inside the weather module
    def test_get_temperature_success(self, mock_get):
        # Mock response object
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'temperature': 25}
        mock_get.return_value = mock_response

        temperature = get_temperature("London")
        self.assertEqual(temperature, 25)
        #mock_get.assert_called_once_with("https://api.weather.com/temp?city=London")

    @patch('app.routers.weather.requests.get')
    def test_get_temperature_failure(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        with self.assertRaises(Exception) as context:
            get_temperature("Paris")

        self.assertIn("API call failed", str(context.exception))


    def test_square_positive(self):
        self.assertEqual(square(5), 25)

    def test_square_zero(self):
        self.assertEqual(square(0), 0)

    def test_square_negative(self):
        self.assertEqual(square(-4), 16)

if __name__ == '__main__':
    unittest.main()
