import unittest
import palindrome2 as pdrome

class TestPalindrome(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(pdrome.reverse('hello'), 'olleh')
        self.assertEqual(pdrome.reverse('a'), 'a')
        self.assertEqual(pdrome.reverse('otto'), 'otto')

    def test_palindrome(self):
        self.assertEqual(pdrome.is_palindrome_v2('noon'), True)
        self.assertEqual(pdrome.is_palindrome_v2('racecar'), True)
        self.assertEqual(pdrome.is_palindrome_v2('dented'), False)

if __name__ == '__main__':
    unittest.main()