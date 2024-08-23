import pandas as pd
import requests
import psycopg2

# Ingest sales data from CSV file
sales_data = pd.read_csv('sales_data.csv')


# Ingest exchange rates from external API
api_endpoint = 'https://api.example.com/exchange_rates'
auth_token = 'your_auth_token'
headers = {'Authorization': f'Bearer {auth_token}'}
response = requests.get(api_endpoint, headers=headers)
exchange_rates = response.json()

# Ingest customer data from internal API
api_endpoint = 'https://api.example.com/customer_data'
auth_token = 'your_auth_token'
headers = {'Authorization': f'Bearer {auth_token}'}
response = requests.get(api_endpoint, headers=headers)
customer_data = response.json()

#this above code fetche data from two external APIs using authentication token and stores the responses in the exchange_rates and customer_data variables.


# Ingest products and transactions data from PostgreSQL database
#Connection details to the postgreSQl database is required
#cur is used to exceute the quries and fetch the results
conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_username",
    password="your_password"
)
cur = conn.cursor()
cur.execute("SELECT * FROM products")
products = cur.fetchall()
cur.execute("SELECT * FROM transactions")
transactions = cur.fetchall()
cur.close()
conn.close()

# Save ingested data to CSV files
sales_data.to_csv('ingested_sales_data.csv', index=False)
pd.DataFrame(exchange_rates).to_csv('ingested_exchange_rates.csv', index=False)
pd.DataFrame(customer_data).to_csv('ingested_customer_data.csv', index=False)
pd.DataFrame(products).to_csv('ingested_products.csv', index=False)
pd.DataFrame(transactions).to_csv('ingested_transactions.csv', index=False)
