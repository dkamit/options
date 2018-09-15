from datetime import datetime

class IndexRecord:
    def __init__(self, l):
        l = l.split(",")
        self.Date = datetime.strptime(str(l[0].replace('"','')), '%d-%b-%Y')
        self.Open = float(l[1].replace('"',''))
        self.High = float(l[2].replace('"',''))
        self.Low = float(l[3].replace('"',''))
        self.Close = float(l[4].replace('"',''))
        self.SharesTraded = float(l[5].replace('"',''))
        self.Turnover =  float(l[6].replace('"',''))

    def __str__(self):
        return str(self.Date) + " " + str(self.Close)

    def __repr__(self):
        return self.__str__()