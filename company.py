from fmp.request_types import *
from fmp.get_utils import create_report
from datetime import datetime
import time


class Company:

    _income_statement = []
    _balance_sheet = []
    _cash_flow_statement = []
    _profile = []
    _ratios = []
    _enterprise_value = []
    _key_metrics = []
    _financial_growth = []
    _company_rating = []
    _price_history = []

    def __init__(self, ticker):
        self.__ticker = ticker

        self.__statement = Statement(ticker)
        self.__metrics = Metric(ticker)
        self.__stock_price = StockPrice(ticker)

    @property
    def ticker(self):
        return self.__ticker

    def income_statement(self, period='both'):
        if not self._income_statement:
            self._income_statement = self.__statement.get_statement('income', period)

        return self._income_statement

    def balance_sheet(self, period='both'):
        if not self._balance_sheet:
            self._balance_sheet = self.__statement.get_statement('balance-sheet', period)

        return self._balance_sheet

    def cash_flow_statement(self, period='both'):
        if not self._cash_flow_statement:
            self._cash_flow_statement = self.__statement.get_statement('cash-flow', period)

        return self._cash_flow_statement

    def profile(self):
        if not self._profile:
            self._profile = self.__metrics.get_metric('profile')

        return self._profile

    def financial_ratios(self):
        if not self._ratios:
            self._ratios = self.__metrics.get_metric('ratio')

        return self._ratios

    def key_metrics(self):
        if not self._key_metrics:
            self._key_metrics = self.__metrics.get_metric('metric')

        return self._key_metrics

    def enterprise_value(self):
        if not self._enterprise_value:
            self._enterprise_value = self.__metrics.get_metric('value')

        return self._enterprise_value

    def financial_growth(self):
        if not self._financial_growth:
            self._financial_growth = self.__metrics.get_metric('growth')

        return self._financial_growth

    def company_rating(self):
        if not self._company_rating:
            rating = self.__metrics.get_metric('rating').iloc[:, -2:]
            overall_rating = rating['rating'][0].pop('rating')
            rating['ratingDetails'][0]['rating'] = overall_rating
            self._company_rating = {'overall_rating': overall_rating, 'ratings': pd.DataFrame.from_dict(rating['ratingDetails'][0])}

        return self._company_rating

    def generate_ticker_stream(self):
        for quote in self.__stock_price.data_generator():
            print(f'{datetime.now().strftime("%m/%d %H:%M:%S")} {quote}')
            time.sleep(7)

    def price_history(self):
        if not self._price_history:
            self._price_history = self.__metrics.get_metric('price')

        return self._price_history

    def generate_report(self, type_='full'):
        if type_ == 'full':
            print('Profile\n', self.profile())
            print('Company Rating\n', self.company_rating()['ratings'])
            print('Income Statement\n', self.income_statement().head())
            print('Balance Sheet\n', self.balance_sheet().head())
            print('Cash Flow Statement\n', self.cash_flow_statement().head())
            print('Price History\n', self.price_history().head())
            print('Financial Growth\n', self.financial_growth().head())
            print('Financial Ratios\n', self.financial_ratios().head())
            print('Key Metrics\n', self.key_metrics().head())
            print('Enterprise Value\n', self.enterprise_value().head())
        elif type_ == 'statements':
            print('Income Statement\n', self.income_statement().head())
            print('Balance Sheet\n', self.balance_sheet().head())
            print('Cash Flow Statement\n', self.cash_flow_statement().head())
        elif type_ == 'metrics':
            print('Price History\n', self.price_history().head())
            print('Financial Growth\n', self.financial_growth().head())
            print('Financial Ratios\n', self.financial_ratios().head())
            print('Key Metrics\n', self.key_metrics().head())
            print('Enterprise Value\n', self.enterprise_value().head())
        else:
            raise ValueError('type_ arg must be in ["full", "statements", "metrics"]')