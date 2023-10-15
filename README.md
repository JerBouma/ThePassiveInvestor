# The Passive Investor

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor_this_Project-grey?logo=github)](https://github.com/sponsors/JerBouma)
[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-grey?logo=buymeacoffee)](https://www.buymeacoffee.com/jerbouma)
[![Twitter](https://img.shields.io/badge/Twitter-grey?logo=x)](https://twitter.com/JerBouma)
[![Documentation](https://img.shields.io/badge/Documentation-grey?logo=readme)](https://www.jeroenbouma.com/projects/thepassiveinvestor)
[![PYPI Version](https://img.shields.io/pypi/v/ThePassiveInvestor)](https://pypi.org/project/ThePassiveInvestor/)
[![PYPI Downloads](https://static.pepy.tech/badge/thepassiveinvestor/month)](https://pepy.tech/project/thepassiveinvestor)

Theories and research about the stock market have stated that the semi-strong form of market efficiency seems to hold. This means that all public information is accurately reflected in the price of a financial instrument. This makes the job of a portfolio manager primarily managing the desired risk appetite of the client and not explicitly trying to outperform the market. This fact in combination with Finance professionals all around the world looking for that 'edge' to make their investment decisions as profitable as possible, makes it so the average joe can not compete.

Therefore, the term 'Passive Investing' is often coined around. This refers to buying funds (either ETFs or Mutual Funds) that follow the index (i.e. S&P 500, Dow Jones Index) or a broad market (Developed Markets, MSCI World) for diversification benefits. This means that a sudden decrease in performance of one stock within the index does not (on average) lead to a significant decline in the index as a whole. This allows the holder to spend limited time monitoring his holdings, therefore the term 'Passive'.

With a large increase in ETFs available (over 5,000 in 2020), it can become difficult to make the best choice in what you wish to invest. There are many different providers (iShares, Vanguard, Invesco) as well as with changes to the underlying stocks (i.e. High Yield, Super Dividends, Equal Weighted). This is quickly reflected when looking for a S&P 500 ETF as there are over 20 different ETFs available. With this package, I wish to make  investment decisions easier to make and manage.

An example of the output can be found in the GIF below. This depicts several ETFs collected from [the Top ETFs according to Yahoo Finance](https://finance.yahoo.com/etfs).

![ThePassiveInvestor](https://raw.githubusercontent.com/JerBouma/ThePassiveInvestor/master/Images/outputExample.gif)

## Installation

The package can be installed via the following commands:

1. `pip install thepassiveinvestor`
   - Alternatively, download this repository.
1. (within Python) `import thepassiveinvestor as pi`

The functions within this package are:

- `collect_data(ticker)` - collects the most important data for ETFs as listed in the [Functionality](#Functionality)
  section.
- `create_ETF_report(tickers, filename, folder=None)` - uses collect_data to create an Excel report with data, as
  depicted in the GIF above, per sheet for each ticker.

Therefore, if you wish to collect data on an ETF or create a report of a selection of ETFs you can use the following
example:

```python
import thepassiveinvestor as pi

# Collect data from a specific ETF
vanguard_sp500 = pi.collect_data('VOO')

# Show the data
vanguard_sp500
```

Which returns the following:
```
{'long_name': 'Vanguard 500 Index Fund', 'summary': "The fund employs an indexing investment approach designed to track the performance of the Standard & Poor's 500 Index, a widely recognized benchmark of U.S. stock market performance that is dominated by the stocks of large U.S. companies. The advisor attempts to replicate the target index by investing all, or substantially all, of its assets in the stocks that make up the index, holding each stock in approximately the same proportion as its weighting in the index.", 'image_URL': 'https://s.yimg.com/lq/i/fi/3_0stylelargeeq2.gif', 'sector_holdings': {'realestate': '2.75%', 'consumer_cyclical': '10.13%', 'basic_materials': '2.4%', 'consumer_defensive': '7.38%', 'technology': '23.65%', 'communication_services': '7.43%', 'financial_services': '13.7%', 'utilities': '2.43%', 'industrials': '8.82%', 'energy': '5.11%', 'healthcare': '15.27%'}, 'company_holdings': {'Apple Inc': '5.92%', 'Microsoft Corp': '5.62%', 'Amazon.com Inc': '4.06%', 'Facebook Inc Class A': '2.29%', 'Alphabet Inc Class A': '2.02%', 'Alphabet Inc Class C': '1.97%', 'Berkshire Hathaway Inc Class B': '1.44%', 'Tesla Inc': '1.44%', 'NVIDIA Corp': '1.37%', 'JPMorgan Chase & Co': '1.3%'}, 'annual_returns': {'2022': '-18.15%', '2021': '28.66%', '2020': '18.35%', '2019': '31.46%', '2018': '-4.42%', '2017': '21.78%'}, 'risk_data': {'5y': {'year': '5y', 'alpha': -0.04, 'beta': 1, 'meanAnnualReturn': 0.89, 'rSquared': 100, 'stdDev': 18.69, 'sharpeRatio': -0.19, 'treynorRatio': 8.04}, '3y': {'year': '3y', 'alpha': -0.04, 'beta': 1, 'meanAnnualReturn': 0.8, 'rSquared': 100, 'stdDev': 21.17, 'sharpeRatio': -0.55, 'treynorRatio': 6.76}, '10y': {'year': '10y', 'alpha': -0.04, 'beta': 1, 'meanAnnualReturn': 1.08, 'rSquared': 100, 'stdDev': 14.78, 'sharpeRatio': 0.88, 'treynorRatio': 11.7}}, 'key_characteristics': {'fundInceptionDate': '2010-09-07', 'category': 'Large Blend', 'totalAssets': 744769716224, 'currency': 'USD', 'navPrice': 366.24, 'previousClose': 365.67}}
```

You also have the option to generate a comparison report as follows:

```python
import thepassiveinvestor as pi

# Collect data from a set of ETFs and compare them
etf_comparison = pi.collect_data(['VOO', 'QQQ', 'ARKG', 'VUG', 'SCHA', 'VWO'], comparison=True)

# Show the comparison
etf_comparison
```

Which returns the following:

|                                               | VOO          | QQQ          | ARKG       | VUG          | SCHA        | VWO                       |
|:----------------------------------------------|:-------------|:-------------|:-----------|:-------------|:------------|:--------------------------|
| ('sector_holdings', 'realestate')             | 2.75%        | 0.29%        | 0%         | 2.55%        | 7.16%       | 2.95%                     |
| ('sector_holdings', 'consumer_cyclical')      | 10.13%       | 14.2%        | 0%         | 18.09%       | 12.75%      | 12.92%                    |
| ('sector_holdings', 'basic_materials')        | 2.4%         | 0%           | 0%         | 2.01%        | 4.35%       | 9.34%                     |
| ('sector_holdings', 'consumer_defensive')     | 7.38%        | 6.67%        | 0%         | 2.92%        | 4.12%       | 6.23%                     |
| ('sector_holdings', 'technology')             | 23.65%       | 47.62%       | 3.41%      | 41.19%       | 14.18%      | 15.49%                    |
| ('sector_holdings', 'communication_services') | 7.43%        | 15.99%       | 0%         | 11.96%       | 2.74%       | 8.72%                     |
| ('sector_holdings', 'financial_services')     | 13.7%        | 0.74%        | 0%         | 6.95%        | 15.68%      | 20.63%                    |
| ('sector_holdings', 'utilities')              | 2.43%        | 0.88%        | 0%         | 0%           | 1.83%       | 3.78%                     |
| ('sector_holdings', 'industrials')            | 8.82%        | 4.75%        | 0%         | 4.64%        | 16.16%      | 7.26%                     |
| ('sector_holdings', 'energy')                 | 5.11%        | 0.49%        | 0%         | 1.35%        | 5.85%       | 5.36%                     |
| ('sector_holdings', 'healthcare')             | 15.27%       | 7.54%        | 96.58%     | 8.13%        | 13.98%      | 4.6%                      |
| ('annual_returns', '2022')                    | -18.15%      | -32.49%      | -53.94%    | -33.13%      | -19.8%      | -17.72%                   |
| ('annual_returns', '2021')                    | 28.66%       | 27.24%       | -33.89%    | 27.26%       | 16.35%      | 0.96%                     |
| ('annual_returns', '2020')                    | 18.35%       | 48.6%        | 180.51%    | 40.16%       | 19.35%      | 15.32%                    |
| ('annual_returns', '2019')                    | 31.46%       | 39.12%       | 43.75%     | 37.26%       | 26.54%      | 20.4%                     |
| ('annual_returns', '2018')                    | -4.42%       | -0.14%       | 0.59%      | -3.32%       | -11.75%     | -14.57%                   |
| ('annual_returns', '2017')                    | 21.78%       | 32.7%        | 45.41%     | 27.8%        | 15.04%      | 31.38%                    |
| ('key_characteristics', 'fundInceptionDate')  | 2010-09-07   | 1999-03-10   | 2014-10-31 | 2004-01-26   | 2009-11-03  | 2005-03-04                |
| ('key_characteristics', 'category')           | Large Blend  | Large Growth | Health     | Large Growth | Small Blend | Diversified Emerging Mkts |
| ('key_characteristics', 'totalAssets')        | 744769716224 | 145931501568 | 1899108352 | 132303921152 | 13327223808 | 93044613120               |
| ('key_characteristics', 'currency')           | USD          | USD          | USD        | USD          | USD         | USD                       |
| ('key_characteristics', 'navPrice')           | 366.24       | 281.03       | 32.79      | 225.08       | 43.42       | 41.9                      |
| ('key_characteristics', 'previousClose')      | 365.67       | 281.54       | 33.43      | 225.66       | 43.41       | 41.92                     |
| ('risk_data_3y', 'year')                      | 3y           | 3y           | 3y         | 3y           | 3y          | 3y                        |
| ('risk_data_3y', 'alpha')                     | -0.04        | 0.76         | -4.62      | -1.7         | -3.72       | -1.28                     |
| ('risk_data_3y', 'beta')                      | 1            | 1.08         | 1.32       | 1.11         | 1.15        | 0.9                       |
| ('risk_data_3y', 'meanAnnualReturn')          | 0.8          | 0.92         | 0.25       | 0.74         | 0.6         | 0.05                      |
| ('risk_data_3y', 'rSquared')                  | 100          | 87.57        | 41.82      | 90.79        | 82.66       | 76.68                     |
| ('risk_data_3y', 'stdDev')                    | 21.17        | 24.49        | 41.28      | 24.6         | 26.8        | 20.04                     |
| ('risk_data_3y', 'sharpeRatio')               | -0.55        | -0.7         | 0.27       | -0.72        | 1.58        | 2                         |
| ('risk_data_3y', 'treynorRatio')              | 6.76         | 7.04         | -4.51      | 4.7          | 2.44        | -2.53                     |
| ('risk_data_5y', 'year')                      | 5y           | 5y           | 5y         | 5y           | 5y          | 5y                        |
| ('risk_data_5y', 'alpha')                     | -0.04        | 2.15         | 2.44       | -0.2         | -5.06       | -0.93                     |
| ('risk_data_5y', 'beta')                      | 1            | 1.1          | 1.5        | 1.1          | 1.16        | 0.94                      |
| ('risk_data_5y', 'meanAnnualReturn')          | 0.89         | 1.16         | 0.98       | 0.96         | 0.6         | 0.11                      |
| ('risk_data_5y', 'rSquared')                  | 100          | 88.49        | 45.66      | 91.7         | 83.48       | 78.97                     |
| ('risk_data_5y', 'stdDev')                    | 18.69        | 21.85        | 39.32      | 21.4         | 23.73       | 18.27                     |
| ('risk_data_5y', 'sharpeRatio')               | -0.19        | -0.44        | -0.12      | -0.3         | 1.77        | 1.58                      |
| ('risk_data_5y', 'treynorRatio')              | 8.04         | 9.81         | 1.98       | 7.55         | 2.69        | -1.74                     |
| ('risk_data_10y', 'year')                     | 10y          | 10y          | 10y        | 10y          | 10y         | 10y                       |
| ('risk_data_10y', 'alpha')                    | -0.04        | 2.46         | 0          | -0.51        | -4.08       | -1.79                     |
| ('risk_data_10y', 'beta')                     | 1            | 1.1          | 0          | 1.08         | 1.16        | 0.98                      |
| ('risk_data_10y', 'meanAnnualReturn')         | 1.08         | 1.39         | 0          | 1.13         | 0.9         | 0.24                      |
| ('risk_data_10y', 'rSquared')                 | 100          | 85.33        | 0          | 91.48        | 80.44       | 75.61                     |
| ('risk_data_10y', 'stdDev')                   | 14.78        | 17.56        | 0          | 16.76        | 19.06       | 16.38                     |
| ('risk_data_10y', 'sharpeRatio')              | 0.88         | 0.39         | 0          | 0.78         | 2.92        | 1.44                      |
| ('risk_data_10y', 'treynorRatio')             | 11.7         | 14.01        | 0          | 11.05        | 7.38        | 0.79                      |

Lastly, if you wish to export to Excel this is also a possibility generating an Excel file that contains the most relevant information for each ticker.

```python
import thepassiveinvestor as pi

# Create a report from a list of ETFs
etf_list = ['VOO', 'QQQ', 'ARKG', 'VUG', 'SCHA', 'VWO']
pi.create_ETF_report(etf_list, 'Popular ETFs.xlsx')
```

Which returns the following:

<img width="1512" alt="Screenshot 2023-01-19 at 13 26 48" src="https://user-images.githubusercontent.com/46355364/213443231-ee125c24-3c70-4978-87fd-783c57eacbf2.png">

## Functionality

The package outputs an overview of each fund on a separate sheet. In this overview the following data is shown:

| Topic           | Contains                                                                                                                                                                                                   |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General         | The title of the fund and a summary about the fund's purpose and goal.                                                                                                                                     |
| Characteristics | Inception date (the start of the fund), the category, assets under management (AUM), the denominated currency, net asset value (NAV), the latest close price and the Morningstar Style Box (if available). |
| Holdings        | Sector holdings (% in each sector) and company holdings (top 10 companies with highest %).                                                                                                                 |
| Risk Metrics    | All metrics are displayed in an interval of 3, 5 and 10 years. This includes Jensen's Alpha, Beta, Mean Annual Return, R-squared, Standard Deviation, Sharpe Ratio and Treynor Ratio.                      |
| Performance     | The last five annual returns of the fund as wel as a graph depicting the adjusted close prices over the last 10 years. The actual data for this graph is available on a hidden sheet.                      |

# Contact
If you have any questions about the FinanceToolkit or would like to share with me what you have been working on, feel free to reach out to me via:

- **Website**: https://jeroenbouma.com/
- **Twitter**: https://twitter.com/JerBouma
- **LinkedIn:** https://www.linkedin.com/in/boumajeroen/
- **Email:** jer.bouma@gmail.com
- **Discord:** add me on Discord **`JerBouma`**

If you'd like to support my efforts, either help me out by contributing to the package or [Sponsor Me](https://github.com/sponsors/JerBouma).

[![Star History Chart](https://api.star-history.com/svg?repos=JerBouma/ThePassiveInvestor&type=Date)](https://star-history.com/#JerBouma/ThePassiveInvestor&Date)
