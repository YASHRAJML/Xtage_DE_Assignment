import pandas as pd

# Load standardized data
standardized_data = pd.read_csv('standardized_data.csv')

# Handle missing data
standardized_data.fillna(standardized_data.mean(), inplace=True)

# Handle duplicate records
standardized_data.drop_duplicates(inplace=True)

# Handle inconsistent data entries
standardized_data['Price'] = standardized_data['Price'].apply(lambda x: x if x > 0 else 0)

# Perform feature engineering
standardized_data['Total_Amount'] = standardized_data['Quantity'] * standardized_data['Price']

# Save preprocessed data to CSV file
standardized_data.to_csv('preprocessed_data.csv', index=False)