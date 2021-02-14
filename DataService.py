

class DataService:

    def __init__(self, data={}):
        self.data = data

    def isIncreaseInPrice(self):
        openPrice = float(self.data['1. open'])
        closePrice = float(self.data['4. close'])
        return True if closePrice - openPrice > 0 else False
