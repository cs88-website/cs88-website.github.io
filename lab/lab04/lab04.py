# Question 1

def converter(temperatures, convert):
    """Returns a sequence that converts each Celsius temperature to Fahrenheit

    >>> def convert(x):
    ...     return 9.0*x/5.0 + 32
    >>> temperatures = [10, 20, 30, 40, 50]
    >>> converter(temperatures, convert)
    [50.0, 68.0, 86.0, 104.0, 122.0]
    """
    "*** YOUR CODE HERE ***"
    


# Question 2

from operator import add, mul

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    "*** YOUR CODE HERE ***"
    


# Question 3

def piecewise(f, g, b):
    """Returns the piecewise function h where:

    h(x) = f(x) if x < b,
           g(x) otherwise

    >>> def negate(x):
    ...     return -x
    >>> def identity(x):
    ...     return x
    >>> abs_value = piecewise(negate, identity, 0)
    >>> abs_value(6)
    6
    >>> abs_value(-1)
    1
    """
    "*** YOUR CODE HERE ***"
    


# Question 4

def make_derivative(f):
    """Returns a function that approximates the derivative of f.

    Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
    approximate the derivative by choosing a very small value for h.

    >>> def square(x): 
    ...     # equivalent to: square = lambda x: x*x
    ...     return x*x
    >>> derivative = make_derivative(square)
    >>> result = derivative(3)
    >>> round(result, 3) # approximately 2*3
    6.0
    """
    h=0.00001
    "*** YOUR CODE HERE ***"


# Question 5

def intersects(f, x):
    """Returns a function that returns whether f intersects g at x.

    >>> def square(x):
    ...     return x * x
    >>> def triple(x):
    ...     return x * 3
    >>> def increment(x):
    ...     return x + 1
    >>> def identity(x):
    ...     return x
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
    

