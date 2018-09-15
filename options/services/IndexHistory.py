import requests
from bs4 import BeautifulSoup
from ..helpers.IndexNameHelper import IndexNameHelper
from ..domain.IndexRecord import IndexRecord
from .HttpService import HttpService
from ..helpers.DateHelper import DateHelper

class IndexHistory:
    def __init__(self):
        self.url = "https://www.nseindia.com/products/dynaContent/equities/indices/historicalindices.jsp?"

    def query(self, optionName, fromDate, toDate):
        url = self.getUrl(optionName, fromDate, toDate)
        records = HttpService().query(url)
        indexRecords = [IndexRecord(l) for l in records]
        # print(indexRecords)
        return indexRecords
    
    def dayPrice(self, optionName, cdate):
        url = self.getUrl(optionName, cdate, cdate)
        print(url)
        records = HttpService().query(url)
        indexRecords = [IndexRecord(l) for l in records]
        # print(indexRecords)
        return indexRecords[0]

    def getUrl(self, optionName, fromDate, toDate):
        url = self.url + "indexType=" + IndexNameHelper().getNameForIndex(optionName)
        url = url + "&fromDate=" + fromDate.strftime("%d-%m-%Y")
        url = url + "&toDate=" + toDate.strftime("%d-%m-%Y")
        return url

