import pandas as pd
from datetime import datetime

# Load ingested data
sales_data = pd.read_csv('ingested_sales_data.csv')
exchange_rates = pd.read_csv('ingested_exchange_rates.csv')
customer_data = pd.read_csv('ingested_customer_data.csv')
products = pd.read_csv('ingested_products.csv')
transactions = pd.read_csv('ingested_transactions.csv')


# Merge data from all sources into standardized format
standardized_data = pd.merge(sales_data, products, on='Product_ID')
standardized_data = pd.merge(standardized_data, transactions, on='Transaction_ID')
standardized_data = pd.merge(standardized_data, customer_data, on='Customer_ID')
standardized_data = pd.merge(standardized_data, exchange_rates, on='Transaction_Date')


# Convert columns to datetime format
standardized_data['transaction_date'] = pd.to_datetime(standardized_data['transaction_date'])
standardized_data['customer_date_joined'] = pd.to_datetime(standardized_data['customer_date_joined'])

# Save standardized data to CSV file
standardized_data.to_csv('standardized_data.csv', index=False)
