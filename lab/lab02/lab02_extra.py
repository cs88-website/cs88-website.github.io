"""Optional program for lab02 """

from lab02 import *

# Extra Question

def max_list(s):
    """Return the largest value in a sequence.  None if empty.

    >>> max_list([1,3,-1])
    3
    """
    "*** YOUR CODE HERE ***"

def remove_element(s, exclude):
    """Remove all entries in sequence s equal to exclude.

    >>> remove_element([1, 3, -1], 1)
    [3, -1]
    """
    "*** YOUR CODE HERE ***"

def remove_max(s):
    """Return a a list containing non-maximal elements of a sequence.

    >>> remove_max([1, 3, -1, 3])
    [1, -1]
    """
    "*** YOUR CODE HERE ***"


def count_cond(condition, n):
    """
    >>> divides = lambda n, i: n % i == 0
    >>> count_cond(divides, 2) # 1, 2
    2
    >>> count_cond(divides, 4) # 1, 2, 4
    3
    >>> count_cond(divides, 12) # 1, 2, 3, 4, 6, 12
    6

    >>> is_prime = lambda n, i: count_cond(divides, i) == 2
    >>> count_cond(is_prime, 2) # 2
    1
    >>> count_cond(is_prime, 3) # 2, 3
    2
    >>> count_cond(is_prime, 4) # 2, 3
    2
    >>> count_cond(is_prime, 5) # 2, 3, 5
    3
    >>> count_cond(is_prime, 20) # 2, 3, 5, 7, 11, 13, 17, 19
    8
    """
    "*** YOUR CODE HERE ***"

