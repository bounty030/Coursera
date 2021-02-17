def is_palindrome_v3(s):
    """ (str) -> bool

    Return True if and only if s is a palindrome.
    
    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    >>> is_palindrome_v3('')
    True
    >>> is_palindrome_v3(' ')
    True
    """

    j = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[j - i]:
            return False

    return True

def count_startswith(L, ch):
    """ (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1

    Return the number of strings in L that begin with ch.

    >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
    2
    >>> count_startswith(['rumba', 'salsa', 'samba'], 'r')
    1
    >>> count_startswith(['salsa', 'samba'], 'r')
    0
    """

    startswith = L[:]

    for item in L:
        if item.startswith(ch):
            startswith.remove(item)

    return len(L) - len(startswith)


def count_digits1(s):
    """
    >>> count_digits1('dghf2dfg12')
    '212'
    """

    digits = ''

    for ch in s:
        if ch in '0123456789':
            digits = digits + ch

    return digits

def is_one_to_one(d):
    """ (dict) -> bool

    Return True if and only if no two of d's keys map to the same value.
     
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
    False
    >>> is_one_to_one({})
    True
    """

    val_list = []

    for val in d.values():
        val_list.append(val)

    copy_list = val_list.copy()

    val_list = list( dict.fromkeys(val_list) )

    return len(copy_list) == len(val_list)

if __name__ == '__main__':
    import doctest
    doctest.testmod()