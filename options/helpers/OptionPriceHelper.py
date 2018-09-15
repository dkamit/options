class OptionPriceHelper:
    def __init__(self):
        pass

    def atTheMoney(self, symbol, price):
        gap = self.getGap(symbol)
        rem = price % gap
        q = int(price / gap)
        if rem > gap/2:
            return (q + 1) * gap
        else:
            return q * gap


    def getGap(self, symbol):
        gap = 10
        if symbol == "BANKNIFTY":
            gap = 100
        if symbol == "NIFTY":
            gap = 50
        return gap

    def outTheMoney(self, symbol, atTheMoneyPrice, optionType):
        gap = self.getGap(symbol)
        if optionType == "CE":
            return atTheMoneyPrice + gap
        return atTheMoneyPrice - gap

    def inTheMoney(self, symbol, atTheMoneyPrice, optionType):
        gap = self.getGap(symbol)
        if optionType == "PE":
            return atTheMoneyPrice + gap
        return atTheMoneyPrice - gap