import pandas as pd

from fmp.FMPReader import FMPReader
from fmp.constants import *
from fmp.utils import get_all_tickers, dict2df
import requests


class FundData(FMPReader):
    _fund = ''

    def __init__(self, ticker, fund=None):
        super().__init__(ticker)
        if fund is None:
            self._fund = 'stock'
        else:
            self._fund = fund

    def _get_fund(self, ticker=None, fund=None):

        if fund is None or fund in FUNDS:
            self._fund = fund
        else:
            raise ValueError('fund should be a member of FUNDS (see fmp.constants)')

        fund_dict = self._send_request(req=self._fund, ticker=ticker, subfield='historical')

        if bool(fund_dict):
            return dict2df(fund_dict, self._get_fields(fund, subfield='historical'), 'fund')
        else:
            raise ValueError(f'{ticker} is not a valid {fund} ticker')
