#!/usr/bin/python3

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Assume you have a DataFrame 'df' with 'column1' and 'column2'
df = pd.read_csv('your_file.csv')  # Replace with your file path

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in df.columns],
        value='column1'  # Replace with your column
    ),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_column):
    return px.histogram(df, x=selected_column)

if __name__ == '__main__':
    app.run_server(debug=True)

