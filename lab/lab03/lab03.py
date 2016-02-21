# Q1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"


# Q2
def first(s):
    """Return the first element in a sequence."""
    return s[0]

def rest(s):
    """Return all elements in a sequence after the first"""
    return s[1:]

def remove(x, s):
    """Remove first element equal to x from sequence s.

    >>> remove(1,[])
    []
    >>> remove(1,[1])
    []
    >>> remove(1,[1,1])
    [1]
    >>> remove(1,[2,1])
    [2]
    >>> remove(1,[3,1,2])
    [3, 2]
    >>> remove(1,[3,1,2,1])
    [3, 2, 1]
    >>> remove(5, [3, 5, 2, 5, 11])
    [3, 2, 5, 11]
    """
    "*** YOUR CODE HERE ***"


# Q3
def factorial(n):
    """Return n * (n - 1) * (n - 2) * ... * 1.

    >>> factorial(5)
    120
    """
    if n == 0:
        return 1
    else:
        n * factorial(n-1)


# Q4
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 0:
        return 0
    else:
        return n * skip_mul(n - 2)


# Q5
i = 0
def count_up(n):
    global i
    if n == 0:
        return []
    else:
        i = i+1
        return [i] + count_up(n-1)
    
count_up(5)


# Q6

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"



# Iterative solution, if you're curious
def gcd_iter(a, b):
    """Returns the greatest common divisor of a and b, using iteration.

    >>> gcd_iter(34, 19)
    1
    >>> gcd_iter(39, 91)
    13
    >>> gcd_iter(20, 30)
    10
    >>> gcd_iter(40, 40)
    40
    """
    if a < b:
        return gcd_iter(b, a)
    while a > b and not a % b == 0:
        a, b = b, a % b
    return b



# Q7
# Recursive min sort

def rmin(s):
    """Return the minimum value in a sequence."""
    if len(s) == 1:
        return first(s)
    else:
        return min(first(s), rmin(rest(s)))

def rsort(s):
    """Sort sequence s in ascending order.
    
    >>> rsort([])
    []
    >>> rsort([1])
    [1]
    >>> rsort([1, 1, 1])
    [1, 1, 1]
    >>> rsort([1, 2, 3])
    [1, 2, 3]
    >>> rsort([3, 2, 1])
    [1, 2, 3]
    >>> rsort([1, 2, 1])
    [1, 1, 2]
    >>> rsort([1,2,3, 2, 1])
    [1, 1, 2, 2, 3]
    """
    "*** YOUR CODE HERE ***"



