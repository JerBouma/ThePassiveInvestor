# The Passive Investor

[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-brightgreen?logo=buymeacoffee)](https://www.buymeacoffee.com/jerbouma)
[![Issues](https://img.shields.io/github/issues/jerbouma/ThePassiveInvestor)](https://github.com/JerBouma/ThePassiveInvestor/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/JerBouma/ThePassiveInvestor?color=yellow)](https://github.com/JerBouma/ThePassiveInvestor/pulls)
[![PYPI Version](https://img.shields.io/pypi/v/ThePassiveInvestor)](https://pypi.org/project/ThePassiveInvestor/)
[![PYPI Downloads](https://img.shields.io/pypi/dm/ThePassiveInvestor)](https://pypi.org/project/ThePassiveInvestor/)

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

```
import thepassiveinvestor as pi

# Collect data from a specific ETF
vanguard_sp500 = pi.collect_data('VOO')

# Create a report from a list of ETFs
etf_list = ['VOO', 'QQQ', 'ARKG', 'VUG', 'SCHA', 'VWO']
pi.create_ETF_report(etf_list, 'Popular ETFs.xlsx')
```

## Functionality

The package outputs an overview of each fund on a separate sheet. In this overview the following data is shown:

| Topic           | Contains                                                                                                                                                                                                   |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General         | The title of the fund and a summary about the fund's purpose and goal.                                                                                                                                     |
| Characteristics | Inception data (the start of the fund), the category, assets under management (AUM), the denominated currency, net asset value (NAV), the latest close price and the Morningstar Style Box (if available). |
| Holdings        | Sector holdings (% in each sector) and company holdings (top 10 companies with highest %).                                                                                                                 |
| Risk Metrics    | All metrics are displayed in an interval of 3, 5 and 10 years. This includes Jensen's Alpha, Beta, Mean Annual Return, R-squared, Standard Deviation, Sharpe Ratio and Treynor Ratio.                      |
| Performance     | The last five annual returns of the fund as wel as a graph depicting the adjusted close prices over the last 10 years. The actual data for this graph is available on a hidden sheet.                      |

## Contribution

Projects are bound to have (small) errors and can always be improved. Therefore, I highly encourage you to submit issues and create pull requests to improve the package.
