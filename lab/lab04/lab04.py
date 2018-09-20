# Question 1

def data_clean(a):
    """Write a function that rounds each element of the list down to the nearest tens place.
    Then, calculate and return the sum of all elements from both lists.

    >>> a = [12, 23, 34]
    >>> data_clean(a)
    [10, 20, 30]
    >>> b = [238, 193, 928]
    >>> data_clean(b)
    [230, 190, 920]
    >>> c = [10, 20, 30]
    >>> data_clean(c)
    [10, 20, 30]
    >>> d = [9, 9, 9]
    >>> data_clean(d)
    [0, 0, 0]
    """
    "*** YOUR CODE HERE ***"
    return _____


# Question 2

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    "*** YOUR CODE HERE ***"
    return _____


# Question 3

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    "*** YOUR CODE HERE ***"
    return _____


# Question 4

def make_buzzer(n):
    """ Returns a function that prints numbers in a specified
    range except those divisible by n.

    >>> i_hate_fives = make_buzzer(5)
    >>> i_hate_fives(10)
    Buzz!
    1
    2
    3
    4
    Buzz!
    6
    7
    8
    9
    """
    "*** YOUR CODE HERE ***"
    return _____


# Question 5

def intersects(f, x):
    """Returns a function that returns whether f intersects g at x.

    >>> at_three = intersects(square, 3)
    >>> at_three(triple) # triple(3) == square(3)
    True
    >>> at_three(increment)
    False
    >>> at_one = intersects(identity, 1)
    >>> at_one(square)
    True
    >>> at_one(triple)
    False
    """
    "*** YOUR CODE HERE ***"
    return _____

