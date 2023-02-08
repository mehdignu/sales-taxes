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

    def round_to_value(self, number,roundto):
        return (round(number / roundto) * roundto)

    def test_price_with_tax(self):
        goody = Goody("test", 1, "other", "other", 14.99)
        goody.calculate_tax_rate()
        goody.calculate_price_with_tax()
        self.assertEqual(goody.price_with_tax, 16.49, "price with tax should to be 16.49")


    def test_sales_tax_on_exempt_categories(self):
        goody = Goody("test", 1, "other", "medical", 14.99)
        goody.calculate_tax_rate()
        goody.calculate_price_with_tax()
        self.assertEqual(goody.price_with_tax, 14.99, "price with tax should to be 14.99")

    def test_sales_tax_on_imported_non_exepted_goodies(self):
        goody = Goody("test", 1, "imported", "food", 10.00)
        goody.calculate_tax_rate()
        goody.calculate_price_with_tax()
        self.assertEqual(goody.price_with_tax, 10.50, "price with tax should to be 10.50")

    def test_sales_tax_on_imported_except_categories(self):
        pass


if __name__ == '__main__':
    unittest.main()
