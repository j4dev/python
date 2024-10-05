import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from _2_perfect_arrangement import get_sorted_customers

class TestGetSortedCustomers(unittest.TestCase):
    def setUp(self):
        self.customers = [
            {"ID": 1, "FIRST_NAME": "Alex", "LAST_NAME": "White", "COUNTRY": "USA", "CREDIT_LIMIT": 200350.54},
            {"ID": 2, "FIRST_NAME": "Tyler", "LAST_NAME": "Hanson", "COUNTRY": "UK", "CREDIT_LIMIT": 15354.23},
            {"ID": 3, "FIRST_NAME": "Jordan", "LAST_NAME": "Fernandez", "COUNTRY": "France", "CREDIT_LIMIT": 359200.67},
            {"ID": 4, "FIRST_NAME": "Drew", "LAST_NAME": "Bradley", "COUNTRY": "Albania", "CREDIT_LIMIT": 1060.57},
            {"ID": 5, "FIRST_NAME": "Blake", "LAST_NAME": "Fuller", "COUNTRY": "USA", "CREDIT_LIMIT": 14789.00},
            {"ID": 6, "FIRST_NAME": "Spencer", "LAST_NAME": "Johnston", "COUNTRY": "China", "CREDIT_LIMIT": 100243.35},
            {"ID": 7, "FIRST_NAME": "Ellis", "LAST_NAME": "Gutierrez", "COUNTRY": "USA", "CREDIT_LIMIT": 998999.20},
            {"ID": 8, "FIRST_NAME": "Morgan", "LAST_NAME": "Thomas", "COUNTRY": "Canada", "CREDIT_LIMIT": 500500.23},
            {"ID": 9, "FIRST_NAME": "Riley", "LAST_NAME": "Garza", "COUNTRY": "UK", "CREDIT_LIMIT": 18782.44},
            {"ID": 10, "FIRST_NAME": "Peyton", "LAST_NAME": "Harris", "COUNTRY": "USA", "CREDIT_LIMIT": 153867.00}
        ]

    def print_table(self, data, headers):
        row_format = "{:<10}" * len(headers)
        print(row_format.format(*headers))
        for item in data:
            print(row_format.format(*[item[header] for header in headers]))

    def test_get_sorted_customers(self):
        print("Starting test_get_sorted_customers")
        print("Input customers:")
        self.print_table(self.customers, ["ID", "FIRST_NAME", "LAST_NAME", "COUNTRY", "CREDIT_LIMIT"])
        
        expected_result = [
            {"ID": 1, "FIRST_NAME": "Alex", "LAST_NAME": "White", "COMBINED_NAME": "AlexWhite"},
            {"ID": 9, "FIRST_NAME": "Riley", "LAST_NAME": "Garza", "COMBINED_NAME": "RileyGarza"},
            {"ID": 5, "FIRST_NAME": "Blake", "LAST_NAME": "Fuller", "COMBINED_NAME": "BlakeFuller"},
            {"ID": 4, "FIRST_NAME": "Drew", "LAST_NAME": "Bradley", "COMBINED_NAME": "DrewBradley"},
            {"ID": 2, "FIRST_NAME": "Tyler", "LAST_NAME": "Hanson", "COMBINED_NAME": "TylerHanson"}
        ]
        
        result = get_sorted_customers(self.customers)
        print("Output result:")
        self.print_table(result, ["ID", "FIRST_NAME", "LAST_NAME", "COMBINED_NAME"])
        
        self.assertEqual(result, expected_result)
        print("Test passed")

if __name__ == '__main__':
    unittest.main()