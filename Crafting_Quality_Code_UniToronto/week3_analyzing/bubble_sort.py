def bubble_sort(L):
    """ (list) -> NoneType

    Sort a list according to the bubble sort algorithm.

    >>> L = [2, 3, 5, 3]
    >>> bubble_sort(L)
    >>> L 
    [2, 3, 3, 5]
    >>> L = []
    >>> bubble_sort(L)
    >>> L
    []
    """

    # The index of the last unsorted item.
    end = len(L) - 1

    while end >= 0:
        for i in range(end):
            # Bubble once through the unsorted section to move the largest item
            # to index end.
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
            
        end = end - 1

if __name__ == '__main__':
    import cProfile
    import doctest
    doctest.testmod()

    L = [3,1,2,10,1,0,5]
    cProfile.run('bubble_sort(L)')
