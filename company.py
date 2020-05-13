from fmp.request_types import *


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

    def __init__(self, ticker):
        self.__ticker = ticker

        self.__statement = Statement(ticker)
        self.__metrics = Metric(ticker)

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
