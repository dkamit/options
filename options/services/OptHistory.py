import requests
from bs4 import BeautifulSoup
from ..domain.OptRecord import OptRecord
from .HttpService import HttpService

class OptHistory:
    def __init__(self):
        pass 

    def query(self, symbol, expiryDate, optionType, strikePrice, fromDate, toDate):
        url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?instrumentType=OPTIDX"
        url = url + "&symbol=" + str(symbol)
        url = url + "&expiryDate=" + expiryDate.strftime("%d-%m-%Y")
        url = url + "&optionType=" + str(optionType)
        url = url + "&strikePrice=" + str(strikePrice)
        url = url + "&dateRange=&fromDate=" + fromDate.strftime("%d-%b-%Y")
        url = url + "&toDate=" + toDate.strftime("%d-%b-%Y")
        url = url + "&segmentLink=9&symbolCount="
        records = HttpService().query(url)
        optRecords = [OptRecord(l) for l in records]
        # print(optRecords)
        return optRecords

    def queryStock(self, symbol, expiryDate, optionType, strikePrice, fromDate, toDate):
        url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?instrumentType=OPTSTK"
        url = url + "&symbol=" + str(symbol)
        url = url + "&expiryDate=" + expiryDate.strftime("%d-%m-%Y")
        url = url + "&optionType=" + str(optionType)
        url = url + "&strikePrice=" + str(strikePrice)
        url = url + "&dateRange=&fromDate=" + fromDate.strftime("%d-%b-%Y")
        url = url + "&toDate=" + toDate.strftime("%d-%b-%Y")
        url = url + "&segmentLink=9&symbolCount="
        records = HttpService().query(url)
        optRecords = [OptRecord(l) for l in records]
        # print(optRecords)
        return optRecords