from datetime import datetime

class StockRecord:
    def __init__(self, l):
        l = l.split(",")
        self.Symbol = l[0]
        self.Series = l[1]
        self.Date = datetime.strptime(str(l[2].replace('"','')), '%d-%b-%Y')
        self.PrevClose = self.safeFloatParse(l[3])
        self.Open = self.safeFloatParse(l[4])
        self.High = self.safeFloatParse(l[5])
        self.Low = self.safeFloatParse(l[6])
        self.Last = self.safeFloatParse(l[7])
        self.Close = self.safeFloatParse(l[8])
        self.Vwap = self.safeFloatParse(l[9])

    def __str__(self):
        return str(self.Date) + " " + str(self.Close)

    def __repr__(self):
        return self.__str__()

    def safeFloatParse(self, number):
        try:
            return float(number.replace('"',''))
        except ValueError:
            return 0.0