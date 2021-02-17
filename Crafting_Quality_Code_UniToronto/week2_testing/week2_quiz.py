def contains_item(L, s):
    """ (list, object) -> bool

    Return True if and only if s is an item of L.
    """

    for item in L:
        if item == s:
            return True
        else:
            return False

if __name__ == '__main__':
    print(contains_item([1, 2, 3], 3))
    print(contains_item([1, 2, 3], 1))
    print(contains_item([1, 2, 3], 2))
    print(contains_item([], 1))