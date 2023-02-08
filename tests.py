import unittest
from utils import format_request, chunks
from Goody import Goody

class TestRequest(unittest.TestCase):

    def test_request_formatting(self):
        goody = format_request({"name": "test","quantity": 2,"status": "imported","category": "book", "price": 12.90})[0]
        self.assertEqual(goody.name, "test", "name should to be correct")

    def test_chnks(self):
        test_dict = {"name": "test","quantity": 2,"status": "imported","category": "book", "price": 12.90}
        chunked_dict = chunks(test_dict, 2)
        self.assertEqual(len(list(chunked_dict)), 3, "a dictionary should to be chunked correctly")

class TestTaxCalculations(unittest.TestCase):

    def test_basic_sales_tax_on_non_imported_non_exempted_goods(self):
        goody = Goody("test", 1, "other", "other", 12.90)
        goody.calculate_tax_rate()
        self.assertEqual(goody.tax, 10, "tax should to be 10%")

    def test_price_with_tax(self):
        goody = Goody("test", 1, "other", "other", 12.90)
        goody.calculate_tax_rate()
        goody.calculate_price_with_tax()


    def test_sales_tax_on_exempt_categories(self):
        pass

    def test_sales_tax_on_imported_goodies(self):
        pass

    def test_sales_tax_on_imported_except_categories(self):
        pass


if __name__ == '__main__':
    unittest.main()
