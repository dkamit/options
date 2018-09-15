from datetime import datetime , timedelta, date
import dateutil.relativedelta

class DateHelper:
    def __init__(self):
        pass
    
    def getFirstWorkingday(self, fdate):
        if fdate.weekday() == 5:
            c = fdate + timedelta(days = 2)
            return c
        if fdate.weekday() == 6:
            c = fdate +timedelta(days = 1)
            return c
        return fdate

    def getThursdays(self, year, month):
        first = date(year, month, 1)
        thursdays = []
        cdate = first
        while cdate.month == month:
            if cdate.weekday() == 3:
                thursdays.append(cdate)
            cdate += timedelta(days=1)
        return thursdays

    def getNextDate(self, currentDate):
        currentDate += timedelta(days = 1)
        return currentDate

    def getLastThursday(self, year, month):
        return self.getThursdays(year, month)[-1]

    def getPrevExpiryDate(self, expiryDate):
        previousMonth = date(expiryDate.year, expiryDate.month, 1) - dateutil.relativedelta.relativedelta(months=1)
        s= self.ensureNotHoliday(self.getLastThursday(previousMonth.year, 
            previousMonth.month))
        return s

    def ensureNotHoliday(self, currentDate):
        if currentDate.month == 1 and currentDate.day == 26:
            newDate =currentDate - timedelta(days=1)
            return newDate
        elif currentDate.month ==12 and currentDate.day == 25:
            newDate =currentDate - timedelta(days=1)
            return newDate
        elif currentDate.month ==3 and currentDate.day == 29:
            newDate =currentDate - timedelta(days=1)
            return newDate
        elif currentDate.month ==11 and currentDate.day == 23:
            newDate =currentDate - timedelta(days=1)
            return newDate
        elif currentDate.month == 4 and currentDate.day == 24 and currentDate.year == 2014:
            newDate =currentDate - timedelta(days=1)
            return newDate
        elif currentDate.month == 2 and currentDate.day == 27 and currentDate.year ==2014:
            return currentDate - timedelta(days=1)
        return currentDate