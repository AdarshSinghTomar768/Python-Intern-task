import requests
import pandas as pd
import time
from openpyxl import load_workbook
import os  

url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 50,
    'page': 1
}

def fetch_data():
    response = requests.get(url, params=params)
    data = response.json()


    df = pd.DataFrame(data)
    df = df[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]
    df.columns = ['Cryptocurrency Name', 'Symbol', 'Current Price (USD)', 'Market Capitalization', '24h Trading Volume', 'Price Change (24h %)']

    return df

def analyze_data(df):
    top_5_by_market_cap = df.sort_values(by='Market Capitalization', ascending=False).head(5)

    average_price = df['Current Price (USD)'].mean()

    highest_price_change = df.loc[df['Price Change (24h %)'].idxmax()]
    lowest_price_change = df.loc[df['Price Change (24h %)'].idxmin()]

    print("Top 5 Cryptocurrencies by Market Cap:")
    print(top_5_by_market_cap[['Cryptocurrency Name', 'Market Capitalization']])
    
    print(f"\nAverage Price of Top 50 Cryptocurrencies: ${average_price:.2f}")
    
    print("\nHighest 24h Price Change:")
    print(highest_price_change[['Cryptocurrency Name', 'Price Change (24h %)']])
    
    print("\nLowest 24h Price Change:")
    print(lowest_price_change[['Cryptocurrency Name', 'Price Change (24h %)']])

def save_to_excel(df):
    file_name = 'crypto_data.xlsx'

    if not os.path.exists(file_name):
        with pd.ExcelWriter(file_name, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Live Data')
    else:
        with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            df.to_excel(writer, index=False, sheet_name='Live Data')
def update_data():
    while True:
        print("Fetching data...")
        df = fetch_data()
        
        analyze_data(df)

        save_to_excel(df)

        print("\nWaiting for the next update...\n")
        time.sleep(300)

if __name__ == "__main__":
    update_data()
