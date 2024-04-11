#!/usr/bin/python3

import pandas as pd
from sklearn import preprocessing

def transform_data(df):
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            # Normalize numerical columns
            df[column] = preprocessing.MinMaxScaler().fit_transform(df[[column]])
        else:
            # Encode categorical columns
            df[column] = preprocessing.LabelEncoder().fit_transform(df[column])
    return df

# Use the function
data = pd.read_csv('your_file.csv')  # Replace with your file path
transformed_data = transform_data(data)
print(transformed_data.head())  # Print the first 5 rows of the dataframe
