# TODO: create testing framework for package and company
# TODO: implement logging as part of debugging
# TODO: create mongodb database for storing company value data
# TODO: create real-time ticker feed
# TODO: create object for handling market indexes, ETFs, commodities, mutual funds
# TODO: implement machine learning on data for predicting stock prices, company growth, buy/sell, etc.
# TODO: build out frontend with plotly dash

from company import Company
from fund import Fund

if __name__ == '__main__':
    # holdings = ['AAPL', 'CMI']
    # companies = {holding: Company(holding) for holding in holdings}
    #
    # for company in companies.values():
    #     company.generate_report('full')

    sp500 = Fund(ticker='GSPC', fund='index')
    print(sp500.market_index())
