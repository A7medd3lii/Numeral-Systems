import unittest
from flask import Flask
from main import app
from convert import convert_number  

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_convert_number_invalid_cases(self):
        # Test empty input
        result, result_type, error_message, _ = convert_number('', 10, 2)
        self.assertIsNone(result)
        self.assertIsNone(result_type)
        self.assertEqual(error_message, "No number provided.")

        # Test number with leading zero   
        result, result_type, error_message, _ = convert_number('010', 10, 2)
        self.assertIsNone(result)
        self.assertIsNone(result_type)
        self.assertEqual(error_message, "Invalid input: Numbers should not begin with Zero.")

        # Test non-digit input
        result, result_type, error_message, _ = convert_number('1a', 10, 2)
        self.assertIsNone(result)
        self.assertIsNone(result_type)
        self.assertEqual(error_message, "Invalid input: Please enter digits only.")

        # Test invalid number for the selected base
        result, result_type, error_message, _ = convert_number('10', 2, 10)
        self.assertIsNone(result)
        self.assertIsNone(result_type)
        self.assertEqual(error_message, "Invalid number for the selected base.")


    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        response = self.app.post('/', data={
            'number': '10',
            'from_base': '10',
            'to_base': '2'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1010', response.data)  # Check if the result is in the response

if __name__ == '__main__':
    unittest.main()
