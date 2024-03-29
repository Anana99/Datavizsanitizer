#!/usr/bin/python3
import pandas as pd
import numpy as np

def sanitize_data(df):
    # Handle missing values
    # This will fill any numerical column missing values with the mean of that column
    # And any non-numerical column missing values with the most frequent value of that column
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            df[column].fillna(df[column].mode()[0], inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Correct inconsistent entries
    # This will convert any non-numerical column to a 'category' data type
    for column in df.columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            df[column] = df[column].astype('category')

    return df

# Use the function
data = pd.read_csv('your_file.csv')  # Replace with your file path
sanitized_data = sanitize_data(data)
print(sanitized_data.head())  # Print the first 5 rows of the dataframe
