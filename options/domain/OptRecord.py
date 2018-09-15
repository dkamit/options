from datetime import datetime

class OptRecord:
    def __init__(self, l):
        l = l.split(",")
        self.Symbol = str(l[0].replace('"',''))
        self.Date = datetime.strptime(str(l[1].replace('"','')), '%d-%b-%Y')
        self.Expiry = datetime.strptime(str(l[2].replace('"','')), '%d-%b-%Y')
        self.OptionType = str(l[3].replace('"',''))
        self.StrikePrice = self.safeFloatParse(l[4])
        self.Open = self.safeFloatParse(l[5])
        self.High = self.safeFloatParse(l[6])
        self.Low = self.safeFloatParse(l[7])
        self.Close = self.safeFloatParse(l[8])
        self.LTP = self.safeFloatParse(l[9])
        self.SettlePrice = self.safeFloatParse(l[10])
        self.NoContracts = self.safeFloatParse(l[11])
        self.TurnoverLaks = self.safeFloatParse(l[12])
        self.PremiumTurnover = self.safeFloatParse(l[13])
        self.OpenInt = self.safeFloatParse(l[14])
        self.ChangeInOI = self.safeFloatParse(l[15])
        self.UnderlyingValue = self.safeFloatParse(l[16])
            
    def getSymbol(self):
        return self.Symbol

    def __str__(self):
        return (str(self.Symbol) + " " + str(self.Close))

    def __repr__(self):
        return self.__str__()

    def safeFloatParse(self, number):
        try:
            return float(number.replace('"',''))
        except ValueError:
            return 0.0