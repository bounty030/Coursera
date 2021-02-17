import math

def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    >>> num_buses(100)
    2
    >>> num_buses(101)
    3
    >>> num_buses(1)
    1
    >>> num_buses(0)
    0
    """

    buses = math.ceil(n / 50)

    return buses


def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0.00, 0.00, -0.00, -0.00, 0.00, 0, 0.0, 0.0])
    (0, 0)
    """


    gains = 0
    losses = 0

    for item in price_changes:
        if item > 0:
            gains += item
        if item < 0:
            losses += item

    return (gains, losses)

def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    items_front = list()
    items_last = list()

    for i in range(k):
        items_front.append(L[i])
        items_last.append(L[len(L) - k + i])

    L[0 : k] = items_last
    L[len(L) - k : len(L)] = items_front


    return 

if __name__ == '__main__':
    import doctest
    doctest.testmod()