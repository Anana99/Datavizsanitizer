import unittest
from flask import Flask
from views import data_view

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(data_view)
        self.client = self.app.test_client()

    def test_import_data_route(self):
        response = self.client.post('/import_data', data={'file': (open('your_file.csv', 'rb'), 'your_file.csv')})  # Replace with your file path
        self.assertEqual(response.status_code, 200)

# Add more tests for other routes here

if __name__ == "__main__":
    unittest.main()
