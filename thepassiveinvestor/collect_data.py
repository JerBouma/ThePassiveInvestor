"""Data Collection Module"""
from datetime import datetime

import pandas as pd
from yahooquery import Ticker

from .config import DEFAULT_KEY_STATISTICS_CHOICES, DEFAULT_SUMMARY_DETAIL_CHOICES

# pylint: disable=too-many-locals,broad-exception-caught


def collect_data(tickers, comparison=False, surpress_print=False):
    """
    Description
    ----
    Collect data from Yahoo Finance that consist of the most important characteristics
    of an ETF. This includes, among other things, the country and sector holdings,
    risk statistics and returns.

    Input
    ----
    ticker (string or list)
        A single ticker from an ETF (i.e. QQQ)

    Output
    ----
    ticker_data (dictionary)
        Returns a dictionary with the most important data about the ticker.
    """
    ticker_data = {}

    if isinstance(tickers, str):
        tickers = [tickers]

    for ticker in tickers:
        try:
            data = Ticker(ticker).all_modules[ticker]
            ticker_data[ticker] = {}

            fund_performance = data["fundPerformance"]
            top_holdings = data["topHoldings"]
            default_key_statistics = data["defaultKeyStatistics"]
            summary_detail = data["summaryDetail"]

            ticker_data[ticker]["long_name"] = data["quoteType"]["longName"]
            ticker_data[ticker]["summary"] = data["assetProfile"]["longBusinessSummary"]
            ticker_data[ticker]["image_URL"] = data["fundProfile"]["styleBoxUrl"]

            sector_data = top_holdings["sectorWeightings"]
            ticker_data[ticker]["sector_holdings"] = {}

            for sector in sector_data:
                for key, value in sector.items():
                    ticker_data[ticker]["sector_holdings"][
                        key
                    ] = f"{str(round(value * 100, 2))}%"

            company_data = top_holdings["holdings"]
            ticker_data[ticker]["company_holdings"] = {}

            for company in company_data:
                ticker_data[ticker]["company_holdings"][
                    company["holdingName"]
                ] = f"{str(round(company['holdingPercent'] * 100, 2))}%"

            annual_returns_data = fund_performance["annualTotalReturns"]["returns"][:6]
            ticker_data[ticker]["annual_returns"] = {}

            for returns in annual_returns_data:
                if returns["annualValue"] is None:
                    ticker_data[ticker]["annual_returns"][returns["year"]] = "N/A"
                else:
                    ticker_data[ticker]["annual_returns"][
                        returns["year"]
                    ] = f"{str(round(returns['annualValue'] * 100, 2))}%"

            risk_statistics = fund_performance["riskOverviewStatistics"][
                "riskStatistics"
            ]
            ticker_data[ticker]["risk_data"] = {}

            for risk in risk_statistics:
                ticker_data[ticker]["risk_data"][risk["year"]] = risk

            ticker_data[ticker]["key_characteristics"] = {}

            for option in DEFAULT_KEY_STATISTICS_CHOICES:
                if option == "fundInceptionDate":
                    ticker_data[ticker]["key_characteristics"][
                        option
                    ] = default_key_statistics[option]
                    ticker_data[ticker]["key_characteristics"][
                        option
                    ] = datetime.strptime(
                        ticker_data[ticker]["key_characteristics"][option],
                        "%Y-%m-%d %H:%M:%S",
                    ).date()
                else:
                    ticker_data[ticker]["key_characteristics"][
                        option
                    ] = default_key_statistics[option]

            for option in DEFAULT_SUMMARY_DETAIL_CHOICES:
                ticker_data[ticker]["key_characteristics"][option] = summary_detail[
                    option
                ]
        except Exception:
            if not surpress_print:
                print(f"Not able to collect data for {ticker}")

    if comparison:
        etf_comparison = []

        for ticker in list(ticker_data.keys()):
            for risk_year in ["3y", "5y", "10y"]:
                ticker_data[ticker][f"risk_data_{risk_year}"] = ticker_data[ticker][
                    "risk_data"
                ][risk_year]
            for x in [
                "long_name",
                "summary",
                "image_URL",
                "company_holdings",
                "risk_data",
            ]:
                ticker_data[ticker].pop(x)

            ticker_dataframe = pd.DataFrame.from_dict(
                {
                    (i, j): ticker_data[ticker][i][j]
                    for i in ticker_data[ticker]
                    for j in ticker_data[ticker][i]
                },
                orient="index",
                columns=[ticker],
            )

            ticker_dataframe.index = pd.MultiIndex.from_tuples(ticker_dataframe.index)

            etf_comparison.append(ticker_dataframe)

        etf_comparison_df = pd.concat(etf_comparison, axis="columns")

        return etf_comparison_df

    if len(tickers) == 1:
        ticker_data = ticker_data[tickers[0]]

    return ticker_data
