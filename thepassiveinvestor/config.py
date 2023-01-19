# Default collected key statistics, could differ if desired
DEFAULT_KEY_STATISTICS_CHOICES = {
    "fundInceptionDate": "Fund Inception Date",
    "category": "Category",
    "totalAssets": "Total Assets",
}

# Default collected summary details, could differ if desired
DEFAULT_SUMMARY_DETAIL_CHOICES = {
    "currency": "Currency",
    "navPrice": "Net Asset Value",
    "previousClose": "Previous Close",
}

# In case no risk statistics are available (because the ETF doesn't exist that long), this
# default is used to fill in the gaps
EMPTY_RISK_STATISTICS = {
    "Years": 0,
    "Alpha": 0,
    "Beta": 0,
    "Mean Annual Return": 0,
    "R-squared": 0,
    "Standard Deviation": 0,
    "Sharpe Ratio": 0,
    "Treynor Ratio": 0,
}

# Map category naming to look identical to Yahoo Finance
RISK_STATISTICS_CATEGORY_MAPPING = {
    "year": "Years",
    "alpha": "Alpha",
    "beta": "Beta",
    "meanAnnualReturn": "Mean Annual Return",
    "rSquared": "R-squared",
    "stdDev": "Standard Deviation",
    "sharpeRatio": "Sharpe Ratio",
    "treynorRatio": "Treynor Ratio",
}

# Map category naming to look identical to Yahoo Finance
SECTOR_CATEGORY_MAPPING = {
    "realestate": "Real Estate",
    "consumer_cyclical": "Consumer Cyclical",
    "basic_materials": "Basic Materials",
    "consumer_defensive": "Consumer Defensive",
    "technology": "Technology",
    "communication_services": "Communication Services",
    "financial_services": "Financial Services",
    "utilities": "Utilities",
    "industrials": "Industrials",
    "energy": "Energy",
    "healthcare": "Healthcare",
}
