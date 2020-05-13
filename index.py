from company import Company

if __name__ == '__main__':
    cmi = Company('CMI')

    IS = cmi.income_statement()
    BS = cmi.balance_sheet()
    CF = cmi.cash_flow_statement()

    profile = cmi.profile()
    growth = cmi.financial_growth()
    ratios = cmi.financial_ratios()
    value = cmi.enterprise_value()
    metrics = cmi.key_metrics()
    rating = cmi.company_rating()

    print('income statement\n', IS.head())
    print('balance sheet\n', BS.head())
    print('cash flow statement\n', CF.head())

    print('profile\n', profile)
    print('financial growth\n', growth)
    print('financial ratios\n', ratios)
    print('key metrics\n', metrics)
    print('enterprise value\n', value)
    print('company rating\n', rating['overall_rating'])
    print('company rating\n', rating['ratings'])
