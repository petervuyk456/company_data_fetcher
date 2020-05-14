# TODO: create testing framework for package and company
# TODO: implement logging as part of debugging
# TODO: create mongodb database for storing company value data
# TODO: create real-time ticker feed
# TODO: create object for handling market indexes, ETFs, commodities, mutual funds
# TODO: implement machine learning on data for predicting stock prices, company growth, buy/sell, etc.
# TODO: build out frontend with plotly dash

from company import Company

if __name__ == '__main__':
    cmi = Company('AAPL')
    cmi.generate_report('full')


