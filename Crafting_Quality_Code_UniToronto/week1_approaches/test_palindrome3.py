import unittest
import palindrome3 as pdrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertEqual(pdrome.is_palindrome_v3('noon'), True)
        self.assertEqual(pdrome.is_palindrome_v3('racecar'), True)
        self.assertEqual(pdrome.is_palindrome_v3('dented'), False)
        self.assertEqual(pdrome.is_palindrome_v3('cheesecake'), False)
        self.assertEqual(pdrome.is_palindrome_v3(' '), True)
        self.assertEqual(pdrome.is_palindrome_v3('a'), True)
        self.assertEqual(pdrome.is_palindrome_v3('na'), False)

if __name__ == '__main__':
    unittest.main()