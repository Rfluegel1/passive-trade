import unittest

from DateTimeService import DateTimeService


class TestDateTimeService(unittest.TestCase):
    def setUp(self):
        self.dateTimeService = DateTimeService()

    def test_is_within_trading_hours(self):
        # Is within trading hours
        self.dateTimeService.date = '12:42:33'

        actualIsWithinTradingHours = self.dateTimeService.isWithinTradingHours()
        expectedIsWithinTradingHours = True
        self.assertEqual(actualIsWithinTradingHours, expectedIsWithinTradingHours)

        # Is not within trading hours
        self.dateTimeService.date = '00:42:33'

        actualIsWithinTradingHours = self.dateTimeService.isWithinTradingHours()
        expectedIsWithinTradingHours = False
        self.assertEqual(actualIsWithinTradingHours, expectedIsWithinTradingHours)
