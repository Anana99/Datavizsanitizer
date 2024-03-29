#!/usr/bin/python3

import pandas as pd

def filter_and_sort_data(df, filter_column, filter_value, sort_column, ascending=True):
    # Filter the data
    filtered_data = df[df[filter_column] == filter_value]

    # Sort the data
    sorted_data = filtered_data.sort_values(by=sort_column, ascending=ascending)

    return sorted_data

# Use the function
data = pd.read_csv('your_file.csv')  # Replace with your file path
filtered_and_sorted_data = filter_and_sort_data(data, 'your_filter_column', 'your_filter_value', 'your_sort_column')  # Replace with your columns and values
print(filtered_and_sorted_data.head())  # Print the first 5 rows of the dataframe
