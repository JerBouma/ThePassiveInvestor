# Default collected key statistics, could differ if desired
DEFAULT_KEY_STATISTICS_CHOICES = ['fundInceptionDate',
                                  'category',
                                  'totalAssets']

# Default collected summary details, could differ if desired
DEFAULT_SUMMARY_DETAIL_CHOICES = ['currency',
                                  'navPrice',
                                  'previousClose']

# In case no risk statistics are available (because the ETF doesn't exist that long), this
# default is used to fill in the gaps
EMPTY_RISK_STATISTICS = {"year": 0,
                         "alpha": 0,
                         "beta": 0,
                         "meanAnnualReturn": 0,
                         "rSquared": 0,
                         "stdDev": 0,
                         "sharpeRatio": 0,
                         "treynorRatio": 0}
