import requests
import pandas as pd
from fmp.constants import *
from fmp.get_utils import get_all_tickers


class FMPReader:

    _period = 'annual'  # annual, quarter, both

    def __init__(self, ticker):

        if ticker not in get_all_tickers(False):
            raise ValueError('ticker must be a member of get_all_tickers(as_df=False)')

        self._ticker = ticker

    def _get_dict(self, req, subfield=None):

        try:
            res = self._send_request(req)[0]
        except KeyError:
            res = self._send_request(req)

        if subfield is not None:
            res = res[subfield]

        if type(res) == list:
            res = res[0]

        return {key: [] for key in res}

    def _send_request(self, req, period='annual', subfield=None):
        """
        ticker must be a single ticker i.e. 'AAPL, GOOG, GM
        req_type:
            See fmp website for more details
        period:
            1. annual
            2. quarter
        """

        if req not in REQ_TYPES:
            raise ValueError('req_type must be a member of REQ_TYPES (see constants.py)')

        if period not in PERIODS:
            raise ValueError('period must be a member of PERIODS (see constants.py)')

        if not REQ_TYPES[req]['quarter']:
            period = 'annual'

        ext = REQ_TYPES[req]['ext']

        if period == 'annual':
            url = f'{BASE_URL}{ext}/{self.ticker}'
            with requests.Session() as s:
                res = s.get(url).json()
        elif period == 'quarter':
            url = f'{BASE_URL}{ext}/{self.ticker}?period=quarter'
            with requests.Session() as s:
                res = s.get(url).json()
        elif period == 'both':
            subfield = REQ_TYPES[req]['field'][0]
            annual = self._send_request(req, 'annual')[subfield]
            quarter = self._send_request(req, 'quarter')[subfield]
            return annual + quarter
        else:
            raise ValueError('period must be "annual", "quarter", or "both". Default is "annual".')

        if subfield is not None:
            res = res[subfield]
        return res

    @property
    def ticker(self):
        return self._ticker

    @ticker.setter
    def ticker(self, tick):
        if tick in get_all_tickers(False):
            self._ticker = tick

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        if period in ["annual", "quarter", "both"]:
            self._period = period
