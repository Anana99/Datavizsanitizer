#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(df, plot_type, column1, column2=None):
    if plot_type == 'bar':
        df[column1].value_counts().plot(kind='bar')
    elif plot_type == 'pie':
        df[column1].value_counts().plot(kind='pie')
    elif plot_type == 'scatter' and column2:
        df.plot(kind='scatter', x=column1, y=column2)
    elif plot_type == 'heatmap' and column2:
        correlation = df[[column1, column2]].corr()
        sns.heatmap(correlation, annot=True, cmap='coolwarm')
    else:
        print("Invalid plot type or columns. Please provide a valid plot type (bar, pie, scatter, heatmap) and the necessary columns.")
    plt.show()

# Use the function
data = pd.read_csv('your_file.csv')  # Replace with your file path
plot_data(data, 'bar', 'your_column')  # Replace with your plot type and column(s)
