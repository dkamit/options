from cement import Controller, ex
from time import strftime
from ..services.OptHistory import OptHistory
from ..helpers.DateHelper import DateHelper
from ..services.IndexHistory import IndexHistory
from ..services.StockHistory import StockHistory
from ..helpers.OptionPriceHelper import OptionPriceHelper
from datetime import datetime , timedelta, date

class Strategy(Controller):
    class Meta:
        label = 'strategy'
        stacked_type = 'nested'
        # stacked_on = 'base'

    @ex(
        help='long strangle',
        arguments=[
            ( ['--symbol'],
              {'help': 'symbol',
               'action': 'store',
               'dest': 'symbol' }
            ),
            ( ['--year'],
              {'help': 'year to back test',
               'action': 'store', 'type': int,
               'dest': 'year' }
            )
        ],
    )
    def longStrangle(self):
        self.app.log.info(self.app.pargs.symbol)
        self.app.log.info(self.app.pargs.year)
        dateHelper = DateHelper()
        symbol = self.app.pargs.symbol
        yearlyProfit = 0
        for i in range(1, 13):
            try:
                currentExpiryDate = dateHelper.getLastThursday(self.app.pargs.year,i)
                currentExpiryDate = dateHelper.ensureNotHoliday(currentExpiryDate)
                self.app.log.info("for current expiry date of " + str(currentExpiryDate))
                prevExpiryDate = dateHelper.getPrevExpiryDate(currentExpiryDate)
                indexRecord = IndexHistory().dayPrice(symbol, prevExpiryDate)
                strikePrice = OptionPriceHelper().atTheMoney(symbol, indexRecord.Close)
                optHistory = OptHistory()
                callRecords = optHistory.query(symbol, currentExpiryDate, "CE", 
                    strikePrice, prevExpiryDate, currentExpiryDate)
                putRecords = optHistory.query(symbol, currentExpiryDate, "PE", 
                    strikePrice, prevExpiryDate, currentExpiryDate)
                buyPrice = (callRecords[0].Close + putRecords[0].Close) * 40
                sellPrice = (callRecords[-1].Close + putRecords[-1].Close) * 40
                profit = sellPrice - buyPrice
                if buyPrice < sellPrice:
                    self.app.log.info("Profit : "+ str(profit))
                else:
                    self.app.log.error("Stop Loss : "+ str(profit))
                self.app.log.info("Buy Price : "+ str(buyPrice))
                self.app.log.info("Sell Price : "+ str(sellPrice))
                yearlyProfit += profit
                self.app.log.error("****************************")
            except Exception as err:
                self.app.log.info("error for current expiry date of " + str(currentExpiryDate))
                self.app.log.info(err)
        print(yearlyProfit)

    @ex(
        help='short ladder buy call',
        arguments=[
            ( ['--symbol'],
              {'help': 'symbol',
               'action': 'store',
               'dest': 'symbol' }
            ),
            ( ['--year'],
              {'help': 'year to back test',
               'action': 'store', 'type': int,
               'dest': 'year' }
            ),
            ( ['--month'],
              {'help': 'month to back test',
               'action': 'store', 'type': int,
               'dest': 'month' }
            )
        ],
    )
    def shortLadder(self):
        log = self.app.log
        log.info(self.app.pargs.symbol)
        symbol = self.app.pargs.symbol
        year = self.app.pargs.year
        dateHelper = DateHelper()
        i = self.app.pargs.month
        try:
            currentExpiryDate = dateHelper.getLastThursday(self.app.pargs.year,i)
            currentExpiryDate = dateHelper.ensureNotHoliday(currentExpiryDate)
            for j in range(1, 32):    
                try:
                    currentDate = date(year, i, j)
                    nextDate = dateHelper.getNextDate(currentDate)
                    indexRecord = StockHistory().queryStock(symbol, currentDate)
                    oph = OptionPriceHelper()
                    atTheMoney = oph.atTheMoney(symbol, indexRecord.Close)
                    outTheMoney = oph.outTheMoney(symbol, atTheMoney, "PE")
                    inTheMoney = oph.inTheMoney(symbol, atTheMoney, "PE")
                    optHistory = OptHistory()
                    atMoney = optHistory.queryStock(symbol, currentExpiryDate, "PE", atTheMoney, currentDate, nextDate)
                    inMoney = optHistory.queryStock(symbol, currentExpiryDate, "PE", inTheMoney, currentDate, nextDate)
                    outMoney = optHistory.queryStock(symbol, currentExpiryDate, "PE", outTheMoney, currentDate, nextDate)
                    diff = atMoney[0].Close + outMoney[0].Close - inMoney[0].Close
                    log.info("%s price: %f At: %f | %f  In: %f | %f out: %f | %f  diff: %f" %(currentDate, indexRecord.Close,
                        atTheMoney, atMoney[0].Close, inTheMoney, inMoney[0].Close,
                        outTheMoney, outMoney[0].Close, diff))
                except:
                    pass
        except:
            pass
                
    @ex(
        help='intraday index',
        arguments=[
            ( ['--symbol'],
              {'help': 'symbol',
               'action': 'store',
               'dest': 'symbol' }
            ),
            ( ['--year'],
              {'help': 'year to back test',
               'action': 'store', 'type': int,
               'dest': 'year' }
            ),
            ( ['--month'],
              {'help': 'month to back test',
               'action': 'store', 'type': int,
               'dest': 'month' }
            )
        ],
    )
    def intradayIndex(self):
        self.app.log.info(self.app.pargs.symbol)
        self.app.log.info(self.app.pargs.year)
        log = self.app.log
        month = self.app.pargs.month
        year = self.app.pargs.year
        dateHelper = DateHelper()
        optHistory = OptHistory()
        indexHistory = IndexHistory()
        symbol = self.app.pargs.symbol
        yearlyProfit = 0
        first = DateHelper().getFirstWorkingday(date(year, month, 1))
        strikePrice = indexHistory.dayPrice(symbol, first).Open
        strikePrice = OptionPriceHelper().atTheMoney(symbol, strikePrice)
        while first.year == year and first.month == month:
            try:
                expiryDate = dateHelper.getLastThursday(year, month)
                expiryDate = dateHelper.ensureNotHoliday(expiryDate)
                ceRecord = optHistory.query(symbol, expiryDate, "CE", strikePrice + 100, first, dateHelper.getNextDate(first))
                peRecord = optHistory.query(symbol, expiryDate, "PE", strikePrice - 100, first, dateHelper.getNextDate(first))
                sell = ceRecord[0].Open + peRecord[0].Open
                buy = ceRecord[0].Close + peRecord[0].Close
                if sell > buy:
                    log.info("%s Sell %f Buy %f Profit : %f"%(first, sell, buy, sell-buy))
                else:
                    log.error("%s Sell %f Buy %f Profit : %f"%(first, sell, buy, sell-buy))
                yearlyProfit+= (sell-buy)
            except Exception as err:
                # first = dateHelper.getNextDate(first)
                # log.info(err)
                pass
            finally:
                # log.info("Finally")
                first = dateHelper.getNextDate(first)
        log.info("Profit %f"%(yearlyProfit))
