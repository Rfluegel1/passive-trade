from datetime import datetime


class DateTimeService:

    def __init__(self, date=datetime.now()):
        self.date = date

    def isWithinTradingHours(self):
        pass
