import unittest
import pandas as pd
from utils import import_data, sanitize_data, transform_data, export_data

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_csv('your_file.csv')  # Replace with your file path

    def test_import_data(self):
        data = import_data(open('your_file.csv', 'rb'))  # Replace with your file path
        self.assertIsInstance(data, pd.DataFrame)

    def test_sanitize_data(self):
        sanitized_data = sanitize_data(self.data)
        self.assertFalse(sanitized_data.duplicated().any())
        self.assertFalse(sanitized_data.isnull().values.any())

    def test_transform_data(self):
        transformed_data = transform_data(self.data)
        self.assertTrue(((transformed_data >= 0) & (transformed_data <= 1)).all().all())

    def test_export_data(self):
        export_data(self.data, 'your_export_file.csv')  # Replace with your export file path
        exported_data = pd.read_csv('your_export_file.csv')  # Replace with your export file path
        pd.testing.assert_frame_equal(exported_data, self.data)

if __name__ == "__main__":
    unittest.main()

