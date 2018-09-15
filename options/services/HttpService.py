import requests
from bs4 import BeautifulSoup

class HttpService:
    def __init__(self):
        pass

    def query(self, url):
        headers = {
			'Host': 'www.nseindia.com',
			'Referer': 'https://www.nseindia.com/products/content/equities/equities/eq_security.htm'
            }
        # print(url)
        resp = requests.get(url, headers=headers)
        # print(resp.content)
        soup = BeautifulSoup(resp.content, features="html.parser")
        x = soup.find(id="csvContentDiv")
        records = x.string.split(':')[1:-1]
        return records