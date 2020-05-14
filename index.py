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

    IS = cmi.income_statement()
    BS = cmi.balance_sheet()
    CF = cmi.cash_flow_statement()
    price = cmi.price_history()
    profile = cmi.profile()
    growth = cmi.financial_growth()
    ratios = cmi.financial_ratios()
    value = cmi.enterprise_value()
    metrics = cmi.key_metrics()
    rating = cmi.company_rating()

    print('Profile\n', profile)
    print('Company Rating\n', rating['ratings'])
    print('Income Statement\n', IS.head())
    print('Balance Sheet\n', BS.head())
    print('Cash Flow Statement\n', CF.head())
    print('Price History\n', price.head())
    print('Financial Growth\n', growth.head())
    print('Financial Ratios\n', ratios.head())
    print('Key Metrics\n', metrics.head())
    print('Enterprise Value\n', value.head())
