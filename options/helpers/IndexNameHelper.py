class IndexNameHelper:
    def __init__(self):
        pass

    def getNameForIndex(self, optionName):
        if optionName == "NIFTY":
            return "NIFTY%2050"
        if optionName == "BANKNIFTY":
            return "NIFTY%20BANK"
        return optionName

    def getNameForOption(self, indexName):
        if indexName == "NIFTY%2050" or indexName == "NIFTY 50":
            return "NIFTY"
        return indexName