import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class DataPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def handle_missing_data(self, df):
        # Fill numeric columns with median
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
        
        # Fill categorical columns with mode
        categorical_columns = df.select_dtypes(include=['object']).columns
        df[categorical_columns] = df[categorical_columns].fillna(df[categorical_columns].mode().iloc[0])
        
        return df

    def remove_duplicates(self, df):
        return df.drop_duplicates()

    def handle_inconsistent_data(self, df):
        # Example: Standardize customer gender
        if 'customer_gender' in df.columns:
            df['customer_gender'] = df['customer_gender'].str.lower()
            df['customer_gender'] = df['customer_gender'].replace({'m': 'male', 'f': 'female'})
        
        return df

    def handle_abnormal_values(self, df):
        # Remove negative prices
        if 'price' in df.columns:
            df = df[df['price'] >= 0]
        
        return df

    def feature_engineering(self, df):
        # Example: Create age groups
        if 'customer_age' in df.columns:
            df['age_group'] = pd.cut(df['customer_age'], bins=[0, 18, 30, 50, 100], labels=['<18', '18-30', '31-50', '>50'])
        
        # Example: Normalize price
        if 'price' in df.columns:
            df['normalized_price'] = self.scaler.fit_transform(df[['price']])
        
        return df

    def preprocess(self, df):
        try:
            df = self.handle_missing_data(df)
            df = self.remove_duplicates(df)
            df = self.handle_inconsistent_data(df)
            df = self.handle_abnormal_values(df)
            df = self.feature_engineering(df)
            return df
        except Exception as e:
            print(f"Error during preprocessing: {str(e)}")
            return None

def load_standardized_data(file_path):
    """Load standardized data from a CSV file"""
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def save_preprocessed_data(data, file_path):
    """Save preprocessed data to a CSV file"""
    try:
        data.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error saving data: {str(e)}")

# Load standardized data
standardized_data = load_standardized_data('standardized_data.csv')

if standardized_data is not None:
    # Create a DataPreprocessor instance
    preprocessor = DataPreprocessor()

    # Preprocess the data
    preprocessed_data = preprocessor.preprocess(standardized_data)

    if preprocessed_data is not None:
        # Save the preprocessed data
        save_preprocessed_data(preprocessed_data, 'preprocessed_data.csv')
    else:
        print("Preprocessing failed. No data saved.")
else:
    print("Failed to load data. No preprocessing performed.")