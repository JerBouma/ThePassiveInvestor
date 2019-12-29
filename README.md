# The Passive Investor

Theories and research about the stock market have stated that the semi-strong form of market efficiency seems to hold. This means that all public information is accurately reflected in the price of an financial instrument. This makes the job of a portfolio manager primarily managing the desired risk appetite of the client and not explicitly trying to outperform the market. This fact in combination with Finance professionals all around the world looking for that 'edge' to make their investment decisions as profitable as possible, makes it so the average joe can not compete.

Therefore, the term 'Passive Investing' is often coined around. This often refers to buying funds (either ETFs or Mutual Funds) that follow the index (i.e. S&P 500, Dow Jones Index) or a broad market (Developed Markets, MSCI World) for diversification benefits. This means that a sudden decrease in performance of one stock within the index does not (on average) lead to a significant decline in the index as a whole. This allows the holder to spend limited time monitoring his holdings, therefore the term 'Passive'.

With a large increase in ETFs available (over 5,000 in 2020), it can become difficult to make the right choice in what ETFs you wish to invest. There are many different providers offering ETFs (iShares, Vanguard, Invesco) as well as with changes to the underlying stocks (i.e. High Yield, Super Dividends, Equal Weighted). This is quickly reflected when looking for a S&P 500 ETF as there are over 20 different ETFs available.

With this program and the accompanying spreadsheet, I wish to make investment decisions easier to make and manage.

## Functionality

### The Program
The program is able to output an overview of each fund on a seperate sheet. In this overview the following data is shown:
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

An example of the output can be found in the GIF below. This depicts several ETFs found automatically collected from [the Top ETFs according to Yahoo Finance](https://finance.yahoo.com/etfs). 
 
![](Images/outputExample.gif)
<p><i>Example of several ETFs from Yahoo Finance</i></p>

### The Spreadsheet 
The spreadsheet allow you to input your investment choices and track them accordingly. It uses data as input from what the program creates, but can also be used independently. It features the following.

* Portfolio Tab
    * Display information about  (all continiously updating):
        * Amount bought
        * Purchase date
        * Recent price
        * Bought price
        * Additional costs
        * Total invested
        * Recent value
        * Return (in % and €)
        * YTD trendline
        * Weight in the portfolio
        * Days
    * Recent changes in value of the Indices and Currency exchanges and their trends
    * Comparison between portfolio and indices as benchmarks
    * Accurate input on diversification 
* Orderbook Tab
    * Accurate tracking of orders made that are aggregated on the Portfolio tab
    * Allows the Portfolio Tab not to become cluttered when you invest frequently in the same fund
* Sector Holdings tab
    * Is used to accurately depict the diversification displayed on the portfolio tab
    * Data can be obtained from the output from the program's created excelfile
    * Modifications on a hidden tab are made to correctly weight the diversification (based on amount bought)
* Mobile View tab
    * Created to be bookmarked to quickly track holdings on a mobile phone
    * Requires the tab to be 'Published to the Web' and then bookmarked. Columns can be shifted to match screensize.

An example of the Portfolio tab can be found below:
![](Images/SpreadsheetExample.PNG)

To see a live example and to obtain an empty copy see below:
* [Live example](https://docs.google.com/spreadsheets/d/1Ssb8hRVdwR3vLl8VascSOt3VrFhXec967phnrw9t8Do/edit?usp=sharing)
* [Empty version](https://docs.google.com/spreadsheets/d/1BeJzpVVjJC8CGL-VAbSmvbZX9a3ws34-JlOijvm_sWQ/edit?usp=sharing)

You can create a copy of the empty version for personal use.
