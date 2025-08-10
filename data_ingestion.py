import pandas as pd
import yfinance as yf 
from datetime import date, timedelta
import pprint as pp



def fetch_stock_data(tickers, start_date, end_date):
    # Step 1: Download full OHLCV + Adj Close
    data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False)
    data.reset_index(inplace=True)

    # Step 2: Flatten MultiIndex columns into single-level strings
    data.columns = [
        col[0] if col[1] == '' else f"{col[0]}_{col[1]}"
        for col in data.columns
    ]

    # Step 3: Melt wide to long format
    data_melted = data.melt(
        id_vars="Date",
        var_name="Attribute_Ticker",
        value_name="Value"
    )

    # Step 4: Split into 'Attribute' and 'Ticker'
    data_melted[['Attribute', 'Ticker']] = data_melted['Attribute_Ticker'].str.split('_', n=1, expand=True)
    data_melted.drop(columns='Attribute_Ticker', inplace=True)

    # Step 5: Pivot to wide format, attributes as columns
    data_pivoted = data_melted.pivot(
        index=['Date', 'Ticker'],
        columns='Attribute',
        values='Value'
    ).reset_index()

    return data_pivoted



end_date = date.today().strftime("%Y-%m-%d")
start_date = (date.today() - timedelta(days=365)).strftime("%Y-%m-%d")
tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS']

data = fetch_stock_data(tickers, start_date, end_date)
print(data.columns.tolist())

#data = data.set_index('Date')

#data = data[data['Ticker'] == 'RELIANCE.NS']
#pp.pprint(data.head())


