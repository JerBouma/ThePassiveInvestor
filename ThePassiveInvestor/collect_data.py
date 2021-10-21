from datetime import datetime

from yfinance.utils import get_json

from .config import DEFAULT_KEY_STATISTICS_CHOICES, DEFAULT_SUMMARY_DETAIL_CHOICES


def collect_data(ticker):
    """
    Description
    ----
    Collect data from Yahoo Finance that consist of the most important characteristics
    of an ETF. This includes, among other things, the country and sector holdings,
    risk statistics and returns.

    Input
    ----
    ticker (string)
        A single ticker from an ETF (i.e. QQQ)

    Output
    ----
    ticker_data (dictionary)
        Returns a dictionary with the most important data about the ticker.
    """
    data = get_json(f"https://finance.yahoo.com/quote/{ticker}")
    ticker_data = {}

    fund_performance = data['fundPerformance']
    top_holdings = data['topHoldings']
    default_key_statistics = data['defaultKeyStatistics']
    summary_detail = data['summaryDetail']

    ticker_data['long_name'] = data['quoteType']['longName']
    ticker_data['summary'] = data['assetProfile']['longBusinessSummary']
    ticker_data['image_URL'] = data['fundProfile']['styleBoxUrl']

    sector_data = top_holdings['sectorWeightings']
    ticker_data['sector_holdings'] = {}

    for sector in sector_data:
        for key, value in sector.items():
            ticker_data['sector_holdings'][key] = f"{str(round(value * 100, 2))}%"

    company_data = top_holdings['holdings']
    ticker_data['company_holdings'] = {}

    for company in company_data:
        ticker_data['company_holdings'][company['holdingName']] = f"{str(round(company['holdingPercent'] * 100, 2))}%"

    annual_returns_data = fund_performance['annualTotalReturns']['returns'][:6]
    ticker_data['annual_returns'] = {}

    for returns in annual_returns_data:
        if returns['annualValue'] is None:
            ticker_data['annual_returns'][returns['year']] = "N/A"
        else:
            ticker_data['annual_returns'][returns['year']] = f"{str(round(returns['annualValue'] * 100, 2))}%"

    risk_statistics = fund_performance['riskOverviewStatistics']['riskStatistics']
    ticker_data['risk_data'] = {}

    for risk in risk_statistics:
        ticker_data['risk_data'][risk['year']] = risk

    ticker_data['key_characteristics'] = {}

    for option in DEFAULT_KEY_STATISTICS_CHOICES:
        if option == 'fundInceptionDate':
            ticker_data['key_characteristics'][option] = default_key_statistics[option]
            ticker_data['key_characteristics'][option] = datetime.fromtimestamp(
                ticker_data['key_characteristics'][option]).strftime(
                '%Y-%m-%d')
        else:
            ticker_data['key_characteristics'][option] = default_key_statistics[option]

    for option in DEFAULT_SUMMARY_DETAIL_CHOICES:
        ticker_data['key_characteristics'][option] = summary_detail[option]

    return ticker_data
