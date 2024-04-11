import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_data_route(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('labels', data)
        self.assertIn('values', data)

if __name__ == '__main__':
    unittest.main()
