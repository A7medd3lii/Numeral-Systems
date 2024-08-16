import unittest
from main import app, convert_number

class NumberConverterTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client and other test fixtures."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_get(self):
        """Test the GET request to the index page."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Convert numbers between Decimal, Hexadecimal, Binary, and Octal systems.', response.data)

    def test_conversion_valid(self):
        """Test conversion with valid input."""
        response = self.app.post('/', data=dict(
            number='1010',
            from_base='2',
            to_base='10'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Decimal :', response.data)
        self.assertIn(b'10', response.data)  # Expected result for binary '1010' to decimal '10'

    def test_conversion_invalid_number(self):
        """Test conversion with an invalid number."""
        response = self.app.post('/', data=dict(
            number='ZZZ',
            from_base='16',
            to_base='10'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid number or base conversion error.', response.data)

    def test_conversion_invalid_base(self):
        """Test conversion with an invalid base."""
        response = self.app.post('/', data=dict(
            number='1010',
            from_base='20',  # Invalid base
            to_base='10'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid base provided.', response.data)

    def test_conversion_same_base(self):
        """Test conversion with the same base."""
        response = self.app.post('/', data=dict(
            number='10',
            from_base='10',
            to_base='10'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Decimal :', response.data)
        self.assertIn(b'10', response.data)  # Expected result is the same number

    def test_convert_number_function(self):
        """Test the convert_number function."""
        self.assertEqual(convert_number('1010', 2, 10), '10')
        self.assertEqual(convert_number('10', 10, 16), 'A')
        self.assertEqual(convert_number('A', 16, 10), '10')
        self.assertEqual(convert_number('10', 10, 2), '1010')
        self.assertEqual(convert_number('10', 10, 8), '12')

if __name__ == '__main__':
    unittest.main()
