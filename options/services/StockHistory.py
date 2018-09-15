import requests
from bs4 import BeautifulSoup
from ..helpers.IndexNameHelper import IndexNameHelper
from ..domain.StockRecord import StockRecord
from .HttpService import HttpService
from ..helpers.DateHelper import DateHelper

class StockHistory:

    def __init__(self):
        pass

    def queryStock(self, symbolName, atDate):
        toDate = DateHelper().getNextDate(atDate).strftime("%d-%m-%Y")
        fromDate = atDate.strftime("%d-%m-%Y")
        url = "https://www.nseindia.com/products/dynaContent/common/productsSymbolMapping.jsp?symbol=%s&segmentLink=3&symbolCount=1&series=EQ&dateRange=+&fromDate=%s&toDate=%s&dataType=PRICEVOLUME" % (symbolName, fromDate, toDate)
        records = HttpService().query(url)
        stockRecords = [StockRecord(l) for l in records]
        # print(stockRecords)
        return stockRecords[0]
