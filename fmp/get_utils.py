import requests
import os
import platform
import itertools
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup


def get_legend(csv_name):
    """
    Get legend of all SIC codes, ticker, etc. from rank and filed.com csv
    """
    if platform.system() == 'Windows':
        legend_path = os.getcwd() + '\\references\\raf_ticker_data.pkl'
    else:
        legend_path = os.getcwd() + '/references/raf_ticker_data.pkl'

    return pd.read_pickle(legend_path)


def get_sic_codes():
    """
    Get SIC codes from sec.gov
    """

    url = 'https://www.sec.gov/info/edgar/siccodes.htm'
    sec_sic_page = requests.get(url)

    soup = BeautifulSoup(sec_sic_page.content, 'html.parser')
    sic_table = soup.find_all('table')

    return pd.read_html(str(sic_table))[0]


def get_ticker_info(tickers="all"):
    """
    Generates data frame with every ticker, and associated name, price, and exchange
    """

    if tickers == "all":
        tickers = get_all_tickers(as_df=False)
    elif tickers is None:
        raise Exception("Tickers must be a non-empty numpy array")

    url = 'https://financialmodelingprep.com/api/v3/company/stock/list'
    all_tickers = requests.get(url).json()['symbolsList']

    fields = all_tickers[0].keys()
    dict_ = {key: [] for key in fields}
    for ticker in all_tickers:
        if ticker['symbol'] in tickers:
            for field in dict_:
                if field in ticker and bool(ticker[field]):
                    dict_[field].append(ticker[field])
                else:
                    dict_[field].append('')

    return pd.DataFrame.from_dict(dict_)


def get_sp500_tickers():
    """
    Get S&P500 tickers from Wiki
    """

    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    wiki_page = requests.get(url)

    soup = BeautifulSoup(wiki_page.content, 'html.parser')
    tickers = soup.find(id="constituents").find_all('a', class_='external text')

    ticker_array = [ticker.string for ticker in itertools.islice(tickers, None, None, 2)]

    return pd.Series(np.asarray(ticker_array), name='ticker')


def get_all_tickers(as_df=True):
    """
    Get all tickers using FMP api
    """

    url = 'https://financialmodelingprep.com/api/v3/company/stock/list'
    all_ticker_info = requests.get(url).json()['symbolsList']

    symbols = [ticker["symbol"] for ticker in all_ticker_info]
    if as_df:
        return pd.Series(symbols)
    else:
        return symbols


def create_report(df_dict, name="default"):
    writer = pd.ExcelWriter(f'{name}.xlsx')
    for name, df in df_dict.items():
        df.to_excel(writer, name)
    writer.save()
