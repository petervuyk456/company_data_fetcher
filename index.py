from company import Company
import pandas as pd
from pprint import pprint
import os
from fmp.get_utils import get_all_tickers

if __name__ == '__main__':
    cummins = Company('CMI')
    IS = cummins.income_statement()
    BS = cummins.balance_sheet()
    CF = cummins.cash_flow_statement()

    print('income statement\n', IS.shape)
    print('balance sheet\n', BS.head())
    print('cash flow statement\n', CF.head())

    profile = cummins.profile()
    pprint(profile)
