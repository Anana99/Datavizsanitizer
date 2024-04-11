#!/usr/bin/python3

from flask import Flask
from views import data_view

app = Flask(__name__)
app.register_blueprint(data_view)

if __name__ == "__main__":
    app.run(debug=True)
