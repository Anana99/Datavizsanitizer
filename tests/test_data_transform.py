import unittest
from data_transform import import_data, sanitize_data

class TestDataTransform(unittest.TestCase):
    def test_import_data_valid_file(self):
        file_path = 'test_data.csv'  # Replace with the path to a valid test data file
        data = import_data(file_path)
        self.assertIsNotNone(data)
        self.assertTrue(data.shape[0] > 0)

    def test_import_data_invalid_file(self):
        file_path = 'invalid_file.csv'  # Replace with a non-existent file path
        data = import_data(file_path)
        self.assertIsNone(data)

    def test_sanitize_data(self):
        # Create a sample DataFrame with duplicate rows
        data = pd.DataFrame({
            'Product': ['A', 'B', 'C', 'A'],
            'Quantity': [100, 200, 150, 1000],
            'Revenue': [1000, 2000, 1500, 5000]
        })
        sanitized_data = sanitize_data(data)
        self.assertIsNotNone(sanitized_data)
        self.assertEqual(sanitized_data.shape[0], 3)  # Expecting 3 unique rows

if __name__ == '__main__':
    unittest.main()
