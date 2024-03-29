#!/usr/bin/python3

import pandas as pd

def export_data(df, file_name):
    df.to_csv(file_name, index=False)
    print(f"Data exported to {file_name}")

# Use the function
data = pd.read_csv('your_file.csv')  # Replace with your file path
export_data(data, 'your_export_file.csv')  # Replace with your export file path

