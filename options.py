import yfinance as yf
import program

tickerData = yf.Ticker(program.ticker)

period          =   {'1 Day'            : '1d',
                     '5 Days'           : '5d',
                     '1 Month'          : '1mo',
                     '3 Months'         : '3mo',
                     '6 Months'         : '6mo',
                     '1 Year'           : '1y',
                     '2 Years'          : '2y',
                     '5 Years'          : '5y',
                     '10 Years'         : '10y',
                     'YTD'              : 'ytd',
                     'Max'              : 'max'}


interval        =   {'1 Minute'         : '1m',
                     '2 Minutes'        : '2m',
                     '5 Minutes'        : '5m',
                     '15 Minutes'       : '15m',
                     '30 Minutes'       : '30m',
                     '60 Minutes'       : '60m',
                     '90 Minutes'       : '90m',
                     '1 Hour'           : '1h',
                     '1 Day'            : '1d',
                     '5 Days'           : '5d',
                     '1 Week'           : '1wk',
                     '1 Month'          : '1mo',
                     '3 Months'         : '3mo'}

mainVariables   =   {'Financials'       : tickerData.financials,
                     'Balance Sheet'    : tickerData.balance_sheet,
                     'Cashflow'         : tickerData.cashflow,
                     'Earnings'         : tickerData.earnings,
                     'Dividends'        : tickerData.dividends,
                     'Splits'           : tickerData.splits}

extraVariables  =   {'Sustainability'   : tickerData.sustainability,
                     'Recommendations'  : tickerData.recommendations,
                     'Actions'          : tickerData.actions,
                     'Event Calendar'   : tickerData.calendar,
                     'Options'          : tickerData.options}
