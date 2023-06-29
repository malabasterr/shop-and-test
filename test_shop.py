import unittest
import shop

class FurnitureShopTests(unittest.TestCase):

    def test_sufficient_funds_chair(self):
        balance = shop.process_purchase("chair")
        self.assertEqual(balance, 25)

    def test_sufficient_funds_cushion(self):
        balance = shop.process_purchase("cushion")
        self.assertEqual(balance, 92)

    def test_sufficient_funds_painting(self):
        balance = shop.process_purchase("painting")
        self.assertEqual(balance, 42)

    def test_sufficient_funds_table(self):
        balance = shop.process_purchase("table")
        self.assertEqual(balance, 10)

    def test_sufficient_funds_lamp(self):
        balance = shop.process_purchase("lamp")
        self.assertEqual(balance, 60)

unittest.main()