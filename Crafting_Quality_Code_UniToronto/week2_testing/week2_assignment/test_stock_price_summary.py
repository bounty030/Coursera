import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_empty(self):
        """Empty list condition test.
        
        A zero size / empty list of price_changes.
        """

        price_changes = []
        self.assertEqual(a1.stock_price_summary(price_changes), (0, 0))

    def test_stock_price_summary_one_size_positive(self):
        """Size condition test.
        
        A list with one positive value item.
        """

        price_changes = [1]
        self.assertEqual(a1.stock_price_summary(price_changes), (1, 0))

    def test_stock_price_summary_one_size_zero(self):
        """Size condition test.
        
        A list with one zero value item.
        """

        price_changes = [0]
        self.assertEqual(a1.stock_price_summary(price_changes), (0, 0))

    def test_stock_price_summary_one_size_negative(self):
        """Size condition test.
        
        A list with one negative value item.
        """

        price_changes = [-1]
        self.assertEqual(a1.stock_price_summary(price_changes), (0, -1))


    def test_stock_price_summary_large_size(self):
        """Size condition test.
        
        A large size list of positive, negative and zero values.
        """

        price_changes = [0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01]
        self.assertEqual(a1.stock_price_summary(price_changes), (0.14, -0.17))


    def test_stock_price_summary_small_size(self):
        """Size condition test.
        
        A small size list of price_changes.
        """

        price_changes = [1, -1]
        self.assertEqual(a1.stock_price_summary(price_changes), (1, -1))



if __name__ == '__main__':
    unittest.main(exit=False)
