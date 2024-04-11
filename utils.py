#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt

def import_data(file):
    if file.filename.endswith('.csv'):
        data = pd.read_csv(file)
    elif file.filename.endswith('.xlsx') or file.filename.endswith('.xls'):
        data = pd.read_excel(file)
    elif file.filename.endswith('.json'):
        data = pd.read_json(file)
    else:
        return None
    return data

def sanitize_data(df):
    df = df.drop_duplicates()
    df = df.dropna()
    return df

def transform_data(df):
    df = df.apply(lambda x: (x - x.min()) / (x.max() - x.min()) if x.dtype.kind in 'biufc' else x)
    return df

def plot_data(df, column):
    plt.hist(df[column])
    plt.savefig('static/plot.png')

def export_data(df, file_name):
    df.to_csv(file_name, index=False)

