import pandas as pd

from fmp.FMPReader import FMPReader
from fmp.constants import *
from fmp.get_utils import get_all_tickers
import requests

class CompanyData(FMPReader):

    _data_type = ''

    def __init__(self, ticker, req_type, period='annual'):
        super().__init__(ticker)

        if self._check_period(period):
            self._period = period

        if req_type in REQ_TYPES:
            self._req_type = req_type
            self._data_type = self.__get_type(req_type)
        else:
            raise ValueError('req_type should be a member of REQ_TYPES (see fmp.constants)')

    @staticmethod
    def _check_period(period):
        if period in PERIODS:
            return True
        else:
            raise ValueError('period should be a member of PERIODS (see fmp.constants)')

    @staticmethod
    def _check_request(req, data_type):
        if data_type == 'statement':
            okay_req = STATEMENTS
            const_ = ['statement_type', 'STATEMENTS']
        else:  # data_type == 'metric'
            okay_req = METRICS
            const_ = ['metric_type', 'METRICS']

        if req in okay_req:
            return True
        else:
            raise ValueError(f'{const_[0]} should be a member of {const_[1]} (see fmp.constants)')

    def _get_data(self, req_type=None, period=None):

        if req_type is None:
            req_type = self.req_type
        elif self._check_request(req_type, self._data_type):
            self.req_type = req_type

        if period is None:
            period = self.period
        elif self._check_period(period):
            self.period = period

        subfields = REQ_TYPES[req_type]['field']

        if len(subfields) == 1:
            subfield = subfields[0]
        else:
            subfield = None

        dict_ = self._get_dict(req_type, subfield)
        if period == "both":
            annual = CompanyData.doc2dict(self._send_request(req_type, 'annual', subfield), dict_, self._data_type)
            quarter = CompanyData.doc2dict(self._send_request(req_type, 'quarter', subfield), dict_, self._data_type)
            annual['Period'] = 'A'
            quarter['Period'] = 'Q'
            reports = annual.append(quarter).sort_values(by=['date'], ascending=False)
        else:
            reports = CompanyData.doc2dict(self._send_request(req_type, period, subfield), dict_, self._data_type)

        return reports

    @staticmethod
    def doc2dict(reports, fields, data_type):
        if data_type == 'statement':
            for doc in reports:
                for field in fields:
                    if field in doc and bool(doc[field]):
                        fields[field].append(doc[field])
                    else:
                        fields[field].append('')
        else:
            for field in fields:
                if type(reports) == list and len(reports) > 1:
                    for report in reports:
                        if field in report and bool(report[field]):
                            fields[field].append(report[field])
                        else:
                            fields[field].append('')
                else:
                    if field in reports and bool(reports[field]):
                        fields[field].append(reports[field])
                    else:
                        fields[field].append('')

        return pd.DataFrame.from_dict(fields)

    @staticmethod
    def __get_type(req_type):
        if req_type in STATEMENTS:
            return 'statement'
        elif req_type in METRICS:
            return 'metric'
        else:
            return

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        if data_type in ['statement', 'metric']:
            self._data_type = data_type

    @property
    def req_type(self):
        return self._req_type

    @req_type.setter
    def req_type(self, req_type):
        type_ = self.__get_type(req_type)
        if type_ is not None:
            self.data_type = type_

        self._req_type = req_type


class Statement(CompanyData):

    __statement = []

    def __init__(self, ticker, statement_type='income', period='annual'):
        super().__init__(ticker, statement_type, period)

    def get_statement(self, statement_type=None, period=None):
        self.__statement = self._get_data(statement_type, period)
        return self.__statement


class Metric(CompanyData):

    __metric = []

    def __init__(self, ticker, metric_type='profile', period='annual'):
        super().__init__(ticker, metric_type, period)

    def get_metric(self, metric_type=None, period=None):
        metric = self._get_data(metric_type, period)

        if metric_type == 'profile':
            metric = metric.loc[0, :]

        # TODO: incorporate yfinance for building out profile with
        # info, sustainability, major_holders, institutional holders, splits/dividends
        # yfin_data = Ticker(self.ticker)
        # pd.read_json(yfin_data.info)

        self.__metric = metric

        return self.__metric


class StockPrice:

    __statement = []
    _ticker = ''

    def __init__(self, ticker):
        self.ticker = ticker

    def data_generator(self):
        url = f'https://financialmodelingprep.com/api/v3/stock/real-time-price/{self.ticker}'
        for i in range(0, 10):
            with requests.Session() as s:
                yield s.get(url, stream=True).json()['price']

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, ticker):
        if ticker in get_all_tickers(False):
            self._ticker = ticker
