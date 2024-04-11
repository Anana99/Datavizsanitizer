#!/usr/bin/python3

from flask import Blueprint, render_template, request
import pandas as pd
from utils import import_data, sanitize_data, transform_data, plot_data, export_data

data_view = Blueprint('data_view', __name__)

@data_view.route('/import_data', methods=['POST'])
def import_data_route():
    file = request.files['file']
    data = import_data(file)
    return render_template('data.html', data=data.to_html())

