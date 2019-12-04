# Iterators: Scale

class ScaleIterator:
    """An iterator the scales elements of the iterable s by a number k.

    >>> s = ScaleIterator([1, 5, 2], 5)
    >>> list(s)
    [5, 25, 10]

    >>> m = ScaleIterator(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    def __init__(self, s, k):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        return self

    def __next__(self):
        "*** YOUR CODE HERE ***"


# Generators: Scale

def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"

