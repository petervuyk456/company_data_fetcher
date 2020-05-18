from fmp.fund import FundData


class Fund(FundData):

    _stock_price = []
    _market_index = []
    _etf = []
    _commodity = []
    _euronext = []
    _mutual_fund = []

    def __init__(self, ticker, fund=None):
        super().__init__(ticker, fund)

    def stock_price(self, ticker=None):
        if not self._stock_price:
            self._stock_price = self._get_fund(ticker, 'stock')

        return self._stock_price

    def market_index(self, ticker=None):
        if not self._market_index:
            self._market_index = self._get_fund(ticker, 'index')

        return self._market_index

    def etf(self, ticker=None):
        if not self._etf:
            self._etf = self._get_fund(ticker, 'etf')

        return self._etf

    def euro_next(self, ticker=None):
        if not self._euronext:
            self._euronext = self._get_fund(ticker, 'euronext')

        return self._euronext

    def commodity(self, ticker=None):
        if not self._commodity:
            self._commodity = self._get_fund(ticker, 'commodity')

        return self._commodity

    def mutual_fund(self, ticker=None):
        if not self._mutual_fund:
            self._mutual_fund = self._get_fund(ticker, 'mutual_fund')

        return self._mutual_fund
