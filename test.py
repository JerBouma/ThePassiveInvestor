import thepassiveinvestor as pi
import json

# List of random tickers
etf_tickers = ['SPY', 'QQQ', 'VTI', 'IWM', 'VEA', 'IEFA', 'AGG', 'GLD', 'VWO', 'BND']


# Initialize an empty list to store the data
etf_strat = []

# Collect data for each selected ticker
for ticker in etf_tickers:
    etf_data = pi.collect_data(ticker)
    item = {
        "long_name": etf_data["long_name"],
        "summary": etf_data["summary"]
    }
    etf_strat.append(item)

# Save the data structure to a local file
with open('etf_data.json', 'w') as file:
    json.dump(etf_strat, file, indent=4)