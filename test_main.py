import unittest
from flask import Flask
from main import app

class NumberConverterTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Number Converter', response.data)

    def test_valid_conversion(self):
        response = self.app.post('/', data=dict(number='123'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Binary:', response.data)
        self.assertIn(b'Hexadecimal:', response.data)
        self.assertIn(b'1111011', response.data)  # 123 in binary
        self.assertIn(b'7B', response.data)       # 123 in hexadecimal

    def test_invalid_input_non_digit(self):
        response = self.app.post('/', data=dict(number='abc'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input: Please enter a valid number.', response.data)

    def test_invalid_input_leading_zero(self):
        response = self.app.post('/', data=dict(number='0123'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid input: Numbers should not begin with Zero.', response.data)

if __name__ == '__main__':
    unittest.main()
