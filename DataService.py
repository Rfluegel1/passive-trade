

class DataService:

    def __init__(self, data={}):
        self.data = data

    def isIncreaseInPrice(self):
        open = float(self.data['1. open'])
        close = float(self.data['4. close'])
        return True if close - open > 0 else False
