import unittest
import json

from DataService import DataService

with open('VOO.json') as VOOJsonFile:
    VOOJson = json.load(VOOJsonFile)


class TestDataService(unittest.TestCase):
    def setUp(self):
        self.dataService = DataService()

    def test_initial_data(self):
        self.assertEqual(self.dataService.data, {})

    def test_is_increase_in_price(self):
        # Decrease
        self.dataService.data = {
            "1. open": "358.0200",
            "2. high": "358.0200",
            "3. low": "357.8500",
            "4. close": "357.8800",
            "5. volume": "12932"
        }
        actualIsIncreaseInPrice = self.dataService.isIncreaseInPrice()
        expectedIsIncreaseInPrice = False
        self.assertEqual(actualIsIncreaseInPrice, expectedIsIncreaseInPrice)

        # Increase
        self.dataService.data = {
            "1. open": "356.0200",
            "2. high": "358.0200",
            "3. low": "355.8500",
            "4. close": "357.8800",
            "5. volume": "12932"
        }
        actualIsIncreaseInPrice = self.dataService.isIncreaseInPrice()
        expectedIsIncreaseInPrice = True
        self.assertEqual(actualIsIncreaseInPrice, expectedIsIncreaseInPrice)
