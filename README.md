# Python Intern Task: Cryptocurrency Data Analysis

## Description
This project is part of a Python development internship assessment. The goal is to fetch live cryptocurrency data for the top 50 cryptocurrencies by market capitalization, analyze the data, and save it in a live-updating Excel sheet. Key insights such as the top 5 cryptocurrencies by market cap, average price, and highest/lowest 24-hour price changes are also included in the analysis.

## Features
- Fetches live cryptocurrency data using the CoinGecko API.
- Performs data analysis, including:
  - Top 5 cryptocurrencies by market capitalization.
  - Average price of the top 50 cryptocurrencies.
  - Highest and lowest 24-hour percentage price change.
- Saves data in a live-updating Excel file (`crypto_data.xlsx`), refreshing every 5 minutes.

## Setup Instructions
1. **Install Dependencies**:
   - Ensure Python is installed on your system.
   - Install the required Python libraries:
     ```bash
     pip install pandas requests openpyxl
     ```
2. **Run the Script**:
   - Execute the script using:
     ```bash
     python crypto_data_fetcher.py
     ```
3. **Live Excel File**:
   - The script generates and updates `crypto_data.xlsx` in the same folder every 5 minutes.

4. **Analysis**:
   - View analysis results in the terminal during script execution.
   - Key insights are also summarized in the `Cryptocurrency_Analysis_Report.pdf`.

## Folder Contents
- `crypto_data_fetcher.py`: Python script for fetching, analyzing, and saving cryptocurrency data.
- `crypto_data.xlsx`: Excel file that updates every 5 minutes with live cryptocurrency data.
- `Cryptocurrency_Analysis_Report.pdf`: A brief report summarizing the analysis.
- `README.md`: This file.

## Live Excel Link
[View Live Excel Sheet](https://docs.google.com/spreadsheets/d/1LdvJeJDywcELtgj29iDWyNxRZKDO_e6V/edit?usp=sharing&ouid=112635910988877342520&rtpof=true&sd=true)

## Author
- ADARSH SINGH TOMAR
- Contact: adarsh.23bcs10031@sst.scaler.com
