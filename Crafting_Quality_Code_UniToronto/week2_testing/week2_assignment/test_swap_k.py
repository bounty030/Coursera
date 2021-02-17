import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_zero_size(self):
        """A size test condition.
        
        Zero size list.
        """
        
        nums = []
        k = 0

        a1.swap_k(nums, k)

        self.assertEqual(nums, [])


    def test_swap_k_zero_k(self):
        """A boundary test condition.
        
        Zero swaps.
        """
        
        nums = [1, 2, 3]
        k = 0

        a1.swap_k(nums, k)

        self.assertEqual(nums, nums)


    def test_swap_k_one_k(self):
        """A boundary test condition.
        
        One swap.
        """
        
        nums = [1, 2, 3]
        k = 1

        a1.swap_k(nums, k)

        self.assertEqual(nums, [3, 2, 1])

    def test_swap_k_one_size(self):
        """A size test condition.
        
        One size list.
        """
        
        nums = [5]
        k = 1

        a1.swap_k(nums, k)

        self.assertEqual(nums, [5])

    def test_swap_k_small_size(self):
        """A size test condition.
        
        Small size ĺist.
        """
        
        nums = [5, 6, 3]
        k = 1

        a1.swap_k(nums, k)

        self.assertEqual(nums, [3, 6, 5])

    def test_swap_k_large_size(self):
        """A size test condition.
        
        Large size ĺist.
        """
        
        nums = [5, 6, 3, 1, 0, 22, -5, 99]
        k = 3

        a1.swap_k(nums, k)

        self.assertEqual(nums, [22, -5, 99, 1, 0, 5, 6, 3])

    def test_swap_k_thresh(self):
        """A threshold test condition.
        
        Precondition: 0 <= k <= len(L) // 2

        k and len(L) are threshold values according to the precondition.
        """
        
        nums = [5, 6, 3, 1]
        k = 2

        a1.swap_k(nums, k)

        self.assertEqual(nums, [3, 1, 5, 6])

    def test_swap_k_order_forward(self):
        """An order test condition.
        
        List has increasing values, i.e. is ordered forwards.

        """
        
        nums = [1, 2, 3, 4]
        k = 2

        a1.swap_k(nums, k)

        self.assertEqual(nums, [3, 4, 1, 2])

    def test_swap_k_order_backward(self):
        """An order test condition.
        
        List has decreasing values, i.e. is ordered backwards
        """
        
        nums = [4, 3, 2, 1]
        k = 2

        a1.swap_k(nums, k)

        self.assertEqual(nums, [2, 1, 4, 3])

if __name__ == '__main__':
    unittest.main(exit=False)
