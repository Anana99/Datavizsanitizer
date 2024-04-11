#!/usr/bin/python3
from flask import Flask, render_template_string


app = Flask(__name__)


@app.route('/')
def home():
    return render_template_string('''
        <h1>Welcome to the DataVizSanitizer App!</h1>
        <p>This app allows you to import, sanitize, transform, visualize, and export your data.</p>
        <h2>Instructions:</h2>
        <ol>
            <li><strong>Import Data:</strong> Click on the "Import Data" button and select your CSV, Excel, or JSON file.</li>
            <li><strong>Sanitize Data:</strong> Click on the "Sanitize Data" button to clean the data.</li>
            <li><strong>Transform Data:</strong> Click on the "Transform Data" button to prepare the data for analysis.</li>
            <li><strong>Visualize Data:</strong> Select the type of chart or graph you want to create from the "Visualize Data" dropdown menu.</li>
            <li><strong>Export Data:</strong> Click on the "Export Data" button to download the cleaned and transformed data.</li>
        </ol>
        <h2>Help Resources:</h2>
        <p>If you need further assistance, please visit our <a href="/help">Help Page</a>.</p>
    ''')


@app.route('/help')
def help():
    return render_template_string('''
        <h1>Help Page</h1>
        <p>If you're having trouble using the DataVizSanitizer App, please contact our support team at support@datavizsanitizer.com.</p>
    ''')


if __name__ == '__main__':
    app.run(debug=True)

