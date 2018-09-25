######################
# Required Questions #
######################

def sine(x):
    """Returns the value of sine(x), where x is a value in radians. Use 0.0001 as a threshold.
    
    >>> from math import pi
    >>> sine(pi) #Notice how the value is very small but not quite 0.
    -1.482085565385205e-09 
    >>> sine(pi/2)
    1.0
    >>> sine((7 * pi)/2)
    -1.0
    >>> sine(1.5)
    0.9974949867067586
    """
    "*** YOUR CODE HERE ***"


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"


# Iterative solution, if you're curious
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    if n == 1 or n == 2 or n == 3:
        return n
    a, b, c = 1, 2, 3
    while n > 3:
        a, b, c = b, c, c + 2*b + 3*a
        n = n - 1
    return c


def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"



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
        a, b = b, a
    while a > b and not a % b == 0:
        a, b = b, a % b
    return b



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


# Recursive Min Sort

# Helper function
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


