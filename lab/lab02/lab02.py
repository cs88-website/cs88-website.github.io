"""Lab 2: FunArgs and Higher Order Functions. """

# Utils

def identity(x):
    return x

def four(x):
    return 4

def increment(x):
    return x + 1

def triple(x):
    return 3 * x

def square(x):
    return x * x

def sqrt(x):
    return x**(1/2)





# Experience with functions

def area_rectangle(length, width):
    return length*width

def area_square(length):
    """
    >>> area_square(2)
    4
    """
    "*** YOUR CODE HERE ***"


pi = 3.141592653589793

def area_circle(radius):
    area = pi*square(radius)
    return area



def perimeter_triangle(a,b,c):
    return a+b+c

def area_triangle(a, b, c):
    """Return the area of a triangle of sides of length as a,b,c.

    >>> area_triangle(3,4,5)
    6.0
    """
    s = perimeter_triangle(a,b,c)/2
    "*** YOUR CODE HERE ***"




def uarea_rectangle(descriptor):
    """
    >>> uarea_rectangle((3,4))
    12
    """
    "*** YOUR CODE HERE ***"
    return area_rectangle(length,width)

def uarea_square(descriptor):
    """
    >>> uarea_square(3)
    9
    """
    length = descriptor
    return area_square(length)

def uarea_circle(descriptor):
    """
    >>> uarea_circle(3)
    28.274333882308138
    """
    return area_circle(descriptor)

def uarea_triangle(descriptor):
    """Return the area of a triangle of sides described as (a,b,c).

    >>> uarea_triangle((3,4,5))
    6.0
    """
    "*** YOUR CODE HERE ***"



# Functions as arguments

def twice(f,x):
    """Apply f to the result of applying f to x"
    >>> twice(square,3)
    81
    """
    "*** YOUR CODE HERE ***"

def apply_n(f, x, n):
    """Apply function f to x n times.

    >>> apply_n(increment, 2, 10)
    12
    """
    "*** YOUR CODE HERE ***"


# Mapping functions over data


def map(f,s):
    return [f(x) for x in s]



def mapn(f, n):
    """Return the list resulting from applying function f to the seguence 0 to n-1.

    >>> mapn(square,4)
    [0, 1, 4, 9]
    """
    "*** YOUR CODE HERE ***"


def maxfun(f, g, low, high):
    """Return the list of the maximums of f and g applied to the low..high-1.

    >>> maxfun(four,square,-4,4)
    [16, 9, 4, 4, 4, 4, 4, 9]
    """
    "*** YOUR CODE HERE ***"



# Reducing data using aggregation functions

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


from operator import add, mul

def accumulate(combiner, base, n, term):
    """Return the result of combining the first n terms in a sequence.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)   # 2 * 1^2 * 2^2 * 3^2
    72
    """
    "*** YOUR CODE HERE ***"

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate.

    >>> summation_using_accumulate(5, square)
    55
    >>> summation_using_accumulate(5, triple)
    45
    """
    "*** YOUR CODE HERE ***"

def product_using_accumulate(n, term):
    """An implementation of product using accumulate.

    >>> product_using_accumulate(4, square)
    576
    >>> product_using_accumulate(6, triple)
    524880
    """
    "*** YOUR CODE HERE ***"


# Higher order functions


def lookup(key, table):
    """Return the val associated with the key in a table.                                     

    >>> lookup('grape', [('apple', 1.29),('grape', 2.49),('orange', 1.79)])                   
    2.49                                                                                      
    >>> lookup('banana', [('apple', 1.29),('grape', 2.49),('orange', 1.79)])   
    """
    "*** YOUR CODE HERE ***"


gender_table = ((0, "all"),
                (1, "male"),
                (2, "female"))

def int_to_gender(i):
    return lookup(i, gender_table)



def translater_maker(table):
    def lookup_fun(key):
        return lookup(key, table)
    return lookup_fun



def area_maker(afuns):
    """Return a function that computes area based on shape and descriptor built from
    a list of (shape function tuples).

    >>> afun = area_maker([("square",uarea_square),("rectangle", uarea_rectangle)])
    >>> afun("square",2)
    4
    >>> afun("rectangle",(2,3))
    6

    """
    "*** YOUR CODE HERE ***"


