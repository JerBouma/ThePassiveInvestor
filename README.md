# The Passive Investor
[![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-brightgreen?logo=buymeacoffee)](https://www.buymeacoffee.com/jerbouma)
[![Issues](https://img.shields.io/github/issues/jerbouma/ThePassiveInvestor)](https://github.com/JerBouma/ThePassiveInvestor/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/JerBouma/ThePassiveInvestor?color=yellow)](https://github.com/JerBouma/ThePassiveInvestor/pulls)
[![PYPI Version](https://img.shields.io/pypi/v/ThePassiveInvestor)](https://pypi.org/project/ThePassiveInvestor/)
[![PYPI Downloads](https://img.shields.io/pypi/dm/ThePassiveInvestor)](https://pypi.org/project/ThePassiveInvestor/)

Theories and research about the stock market have stated that the semi-strong form of market efficiency seems to hold.
This means that all public information is accurately reflected in the price of a financial instrument.
This makes the job of a portfolio manager primarily managing the desired risk appetite of the client and not explicitly
trying to outperform the market. This fact in combination with Finance professionals all around the world looking for
that 'edge' to make their investment decisions as profitable as possible, makes it so the average joe can not compete.

Therefore, the term 'Passive Investing' is often coined around. This refers to buying funds
(either ETFs or Mutual Funds) that follow the index (i.e. S&P 500, Dow Jones Index) or a broad market
(Developed Markets, MSCI World) for diversification benefits. This means that a sudden decrease in performance
of one stock within the index does not (on average) lead to a significant decline in the index as a whole.
This allows the holder to spend limited time monitoring his holdings, therefore the term 'Passive'.

With a large increase in ETFs available (over 5,000 in 2020), it can become difficult to make the best choice in
what you wish to invest. There are many different providers (iShares, Vanguard, Invesco) as well as with changes
to the underlying stocks (i.e. High Yield, Super Dividends, Equal Weighted). This is quickly reflected when looking
for a S&P 500 ETF as there are over 20 different ETFs available. With the package and program, I wish to make 
investment decisions easier to make and manage.

An example of the output can be found in the GIF below. This depicts several ETFs collected 
from [the Top ETFs according to Yahoo Finance](https://finance.yahoo.com/etfs). 

![ThePassiveInvestor](https://raw.githubusercontent.com/JerBouma/ThePassiveInvestor/master/Images/outputExample.gif)

## Installation

### Package
The package can be installed via the following commands:

1. `pip install ThePassiveInvestor`
    * Alternatively, download this repository.
2. (within Python) `import ThePassiveInvestor as pi`

The functions within this package are:
- `collect_data(ticker)` - collects the most important data for ETFs as listed in the [Functionality](#Functionality) 
  section.
- `create_ETF_report(tickers, filename)` - uses collect_data to create an Excel report with data, as 
depicted in the GIF above, per sheet for each ticker.
  
Therefore, if you wish to collect data on an ETF or create a report of a selection of ETFs you can use the following 
example:
````
import ThePassiveInvestor as pi

# Collect data from a specific ETF
vanguard_sp500 = pi.collect_data('VOO')

# Create a report from a list of ETFs
etf_list = ['VOO', 'QQQ', 'ARKG', 'VUG', 'SCHA', 'VWO']
pi.create_ETF_report(etf_list, 'Popular ETFs.xlsx')
````


### Program
Installing the program and running an analysis:

1. Download the most recent release [here](https://github.com/JerBouma/ThePassiveInvestor/releases).
    * If you have Python you can also download the repository and run program.py.
2. Unpack the ZIP file to your prefered location and run the file "ThePassiveInvestor.exe"
3. Go to the [FinanceDatabase](https://github.com/JerBouma/FinanceDatabase) and search the database for your preferred tickers.
Then, place the tickers in an Excel sheet with the tickers listed vertically. See the example on the page of the FinanceDatabase.
   * You can also use the Yahoo Finance Screener ([ETFs](https://finance.yahoo.com/screener/etf/new)
   or [Mutual Funds](https://finance.yahoo.com/screener/mutualfund/new)), select your preferences and click
   "Find ETFs". Then you can copy the URL.
    * You can also use 'Quote Lookup' ([example](https://finance.yahoo.com/lookup/etf?s=developed%20markets))
    * You can also use your own Excel file that has the tickers listed vertically.
4. Open the program, enter your save location (i.e. C:/Documents/DevelopedMarketsETF.xlsx) and
input the URL or Excelfile you decided to use in Step 2. Note that you <u>do not</u> have to create an Excel file,
the program does this for you. However, it does not create folders.
5. Run the program, this takes less than a minute to complete.
6. Analyse the Excelfile created

The input should either be an Excel File (with solely tickers in it) or via Yahoo Finance's ETF or Mutual Fund 
Screener (see [here](https://finance.yahoo.com/screener/etf/new) 
and [here](https://finance.yahoo.com/screener/mutualfund/new)). Note that the program <i>can not</i>
handle stocks, bonds or anything else that is not a fund. This is because the data used is only available
for funds and equity investing is not considered Passive Investing. 

![ThePassiveInvestor](https://raw.githubusercontent.com/JerBouma/ThePassiveInvestor/master/Images/programExample.png)

## Functionality
The program and package are able to output an overview of each fund on a separate sheet. In this overview the 
following data is shown:
* The title of the fund
* A summary about the fund's purpose/goal
* Sector Holdings (% in each sector)
* Company Holdings (top 10 companies with highest %)
* Risk Statistics (several measures of risk)
    * Displayed in 3, 5 and 10 years
    * Alpha
    * Beta
    * Mean Annual Return
    * R Squared
    * Standard Deviation
    * Sharpe Ratio
    * Treynor Ratio
* Characteristics of the instrument
    * Inception date (start of fund)
    * Category
    * Total assets
    * Currency
    * Net Asset Value
    * Latest close price
* Morningstar Style Box (style of the fund)
* Last five annual returns
* Graph depicting the adjusted close prices over the last 10 years
* Last 10 years of adjusted close prices for all Tickers (hidden sheet)

## Contribution
Projects are bound to have (small) errors and can always be improved. Therefore,
I highly encourage you to submit issues and create pull requests to improve the program:

If you wish to test the packaging, you can do so by:

1. Clone/Download this repository.
2. Open CMD/PowerShell/Terminal in folder.
3. install dependencies: ```pip install -r requirements.txt``` 

<a href="https://www.buymeacoffee.com/jerbouma" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

### Run/Develop
Run the following command:
- ```python program.py```

### Build
 Installation:
- Windows: 
    - ```pyinstaller --add-data="images;images" --icon=images\iconICO.ico --name=ThePassiveInvestor program.py```
- MacOS/Linux:
    - ```pyinstaller --add-data="images:images" --icon=images/iconICO.ico --name=ThePassiveInvestor --windowed program.py```
    
 Open the 'dist' folder and the 'ThePassiveInvestor' folder, run exe/app. Or:
- Windows:
    - CMD:
        - ```start dist\ThePassiveInvestor\ThePassiveInvestor.exe```
    - PowerShell:
        - ```dist\ThePassiveInvestor\ThePassiveInvestor.exe```
- MacOS 
    - ```open dist/ThePassiveInvestor.app```

## Troubleshooting
The following issue is known:
- <b>Error pyi_rth_certifi</b>: include the files found in the folder "SSL" to the main directory of the program.
Alternatively, download the latest release which fixes this issue.
 
## Disclaimer
While the program allows you to make financial decisions more easily, it explicitly <i>does not</i> make the 
decisions for you. Therefore, these decisions remain your own and I am not responsible for any losses (or gains) made.
