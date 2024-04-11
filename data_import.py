#!/usr/bin/python3
import pandas as pd

def import_data(file_name):
    if file_name.endswith('.csv'):
        data = pd.read_csv(file_name)
    elif file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        data = pd.read_excel(file_name)
    elif file_name.endswith('.json'):
        data = pd.read_json(file_name)
    else:
        print("Invalid file format. Please provide a CSV, Excel, or JSON file.")
        return None
    return data

# Use the function
data = import_data('your_file.csv')  # Replace with your file path
print(data.head())  # Print the first 5 rows of the dataframe
