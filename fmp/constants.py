BASE_URL = 'https://financialmodelingprep.com/api/v3/'

PERIODS = ['annual', 'quarter', 'both']

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
    'metrics': {
        'ext': 'company-key-metrics',
        'quarter': True,
        'field': ['metrics'],
    },
    'rating': {
        'ext': 'company/rating',
        'quarter': False,
        'field': ['rating', 'ratingDetails'],
    },
    'ratios': {
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
}

REQ_TYPES = {
    **METRICS,
    **STATEMENTS,
}
