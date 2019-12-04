
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        "*** YOUR CODE HERE ***"


def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1 and 
    make sure to remove the repeated values in both. 
    You can also assume that s0 and s1 represent infinite sequences.

    >>> twos = scale(naturals(), 2)
    >>> threes = scale(naturals(), 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    "*** YOUR CODE HERE ***"


