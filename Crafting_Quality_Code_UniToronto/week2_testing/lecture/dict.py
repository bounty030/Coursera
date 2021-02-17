
def change(d):

    d['a'] = 0

if __name__ == '__main__':

    expected1 = {'c': 2, 'b': 2, 'a': 1}
    expected2 = {'a': 1, 'b': 2, 'c': 2}

    a = change(expected1)

    print(expected1 == a)