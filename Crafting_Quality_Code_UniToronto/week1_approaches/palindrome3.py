# Learn to Program: Crafting Quality Code

# Palindrome: Algorithm 3
    # Compare first character to last character, second to second last character ...
    
def is_palindrome_v3(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """

    i = 0

    # Last string index.
    j = len(s) - 1

    # Run loop until first and last character do not equal anymore
    # and until all characters have been compared.
    while s[i] == s[j] and i < j:
        i = i + 1
        j = j - 1

    return j <= i

