BASE_URL = 'https://financialmodelingprep.com/api/v3/'

PERIODS = ['annual', 'quarter', 'both']

FUNDS = {
    'etf': {
        'ext': 'historical-price-full/etf',
        'available': 'etfs'
    },
    'commodity': {
        'ext': 'historical-price-full/commodity',
        'available': 'commodities'
    },
    'index': {
        'ext': 'historical-price-full/index',
        'available': 'indexes'
    },
    'euro_next': {
        'ext': 'historical-price-full/euronext ',
        'available': 'euronext'

    },
    'mutual_fund': {
        'ext': 'historical-price-full/mutual_fund',
        'available': 'mutual-funds'
    },
    'stock': {
        'ext': 'historical-price-full',
        'available': ''
    },
}

STATEMENTS = {
    'income': {
        'ext': 'financials/income-statement',
        'quarter': True,
        'field': ['financials'],
    },
    'balance-sheet': {
        'ext': 'financials/balance-sheet-statement',
        'quarter': True,
        'field': ['financials'],
    },
    'cash-flow': {
        'ext': 'financials/cash-flow-statement',
        'quarter': True,
        'field': ['financials'],
    },
}

METRICS = {
    'profile': {
        'ext': 'company/profile',
        'quarter': False,
        'field': ['profile'],
    },
    'metric': {
        'ext': 'company-key-metrics',
        'quarter': True,
        'field': ['metrics'],
    },
    'rating': {
        'ext': 'company/rating',
        'quarter': False,
        'field': ['rating', 'ratingDetails'],
    },
    'ratio': {
        'ext': 'financial-ratios',
        'quarter': False,
        'field': ['ratios'],
    },
    'value': {
        'ext': 'enterprise-value',
        'quarter': True,
        'field': ['enterpriseValues'],
    },
    'growth': {
        'ext': 'financial-statement-growth',
        'quarter': True,
        'field': ['growth'],
    },
    'dcf': {
        'ext': 'historical-discounted-cash-flow',
        'quarter': True,
        'field': ['dcf', 'Stock Price'],
    },
    'price': {
        'ext': 'historical-price-full',
        'quarter': False,
        'field': ['historical'],
    },
}

REQ_TYPES = {
    **METRICS,
    **STATEMENTS,
    **FUNDS,
}
