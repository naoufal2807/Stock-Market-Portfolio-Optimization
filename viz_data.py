import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import pprint as pp
from datetime import date, timedelta
from data_ingestion import fetch_stock_data


def visualize_stock_data(stock_data):
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    

    
    
    plt.figure(figsize=(14, 7))
    sns.set_theme(style="whitegrid")
    sns.lineplot(data=stock_data, x='Date', y='Adj Close', hue='Ticker', marker='o')
    
    plt.title('Adjusted Close Price Over Time', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Adjusted Close Price', fontsize=14)
    plt.legend(title='Ticker', title_fontsize='13', fontsize='11')
    plt.grid(True)
    
    plt.xticks(rotation=45)
    
    plt.show()
    
end_date = date.today().strftime("%Y-%m-%d")
start_date = (date.today() - timedelta(days=365)).strftime("%Y-%m-%d")
tickers = ['RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS']

data = fetch_stock_data(tickers, start_date, end_date)
visualize_stock_data(data)