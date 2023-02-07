import unittest
from utils import format_request, chunks

class TestRequest(unittest.TestCase):

    def test_request_formatting(self):
        goody = format_request({"name": "test","quantity": 2,"status": "imported","category": "book"})[0]
        self.assertEqual(goody.name, "test", "name should to be correct")

    def test_chnks(self):
        test_dict = {"name": "test","quantity": 2,"status": "imported","category": "book"}
        chunked_dict = chunks(test_dict, 2)
        self.assertEqual(len(list(chunked_dict)), 2, "a dictionary should to be chunked correctly")

class TestTaxCalculations(unittest.TestCase):

    def test_basic_sales_tax(self):
        pass

    def test_sales_tax_on_exempt_categories(self):
        pass

    def test_sales_tax_on_imported_goodies(self):
        pass

    def test_sales_tax_on_imported_except_categories(self):
        pass


if __name__ == '__main__':
    unittest.main()
