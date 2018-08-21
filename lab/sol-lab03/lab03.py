## Data Abstraction ##

def make_city(name, lat, lon):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    >>> get_lat(city)
    0
    >>> get_lon(city)
    1
    """
    return [name, lat, lon]

def get_name(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_name(city)
    'Berkeley'
    """
    return city[0]

def get_lat(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lat(city)
    0
    """
    return city[1]

def get_lon(city):
    """
    >>> city = make_city('Berkeley', 0, 1)
    >>> get_lon(city)
    1
    """
    return city[2]

from math import sqrt
def distance(city_1, city_2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    """
    lat_1, lon_1 = get_lat(city_1), get_lon(city_1)
    lat_2, lon_2 = get_lat(city_2), get_lon(city_2)
    return sqrt((lat_1 - lat_2)**2 + (lon_1 - lon_2)**2)

def closer_city(lat, lon, city1, city2):
    """ Returns the name of either city1 or city2, whichever is closest
        to coordinate (lat, lon).

        >>> berkeley = make_city('Berkeley', 37.87, 112.26)
        >>> stanford = make_city('Stanford', 34.05, 118.25)
        >>> closer_city(38.33, 121.44, berkeley, stanford)
        'Stanford'
        >>> bucharest = make_city('Bucharest', 44.43, 26.10)
        >>> vienna = make_city('Vienna', 48.20, 16.37)
        >>> closer_city(41.29, 174.78, bucharest, vienna)
        'Bucharest'
    """
    "*** YOUR CODE HERE ***"



## ADT: Trees ##

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)


def root(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)


def tree_map(fn, t):
    """Maps the function fn over the entries of tree and returns the
    result in a new tree.

    >>> numbers = tree(1, 
    ...                    [tree(2, 
    ...                          [tree(3),   
    ...                           tree(4)]),  
    ...                     tree(5,   
    ...                           [tree(6,                           
    ...                                [tree(7)]), 
    ...                           tree(8)])])
    >>> print_tree(tree_map(lambda x: 2**x, numbers))
    2
      4
        8
        16
      32
        64
          128
        256
    """
    "*** YOUR CODE HERE ***"



## ADT: Rational Numbers ##

def make_rat(num, den):
    """Creates a rational number, given a numerator and
    denominator.
    """
    return lambda x, y: [lambda: den + x, lambda: num + y]

def num(rat):
    """Extracts the numerator from a rational number."""
    return rat(2, 3)[1]() - 3

def den(rat):
    """Extracts the denominator from a rational number."""
    return rat(8, 5)[0]() - 8

def add_rat(a, b):
    """Adds two rational numbers A and B. For example,
    (3 / 4) + (5 / 3) = (29 / 12)

    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = add_rat(a, b)
    >>> num(c)
    29
    >>> den(c)
    12
    """
    "*** YOUR CODE HERE ***"

def sub_rat(a, b):
    """Subtracts two rational numbers A and B. For example,
    (3 / 4) - (5 / 3) = (-11 / 12)

    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = sub_rat(a, b)
    >>> num(c)
    -11
    >>> den(c)
    12
    """
    "*** YOUR CODE HERE ***"

def mul_rat(a, b):
    """Multiplies two rational numbers A and B. For example,
    (3 / 4) * (5 / 3) = (15 / 12)

    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = mul_rat(a, b)
    >>> num(c)
    15
    >>> den(c)
    12
    """
    "*** YOUR CODE HERE ***"

def div_rat(a, b):
    """Divides two rational numbers A and B. Keep in mind that A / B
    is equivalent to A * (1 / B). For example,
    (3 / 4) / (5 / 3) = (9 / 20)

    >>> a, b = make_rat(3, 4), make_rat(5, 3)
    >>> c = div_rat(a, b)
    >>> num(c)
    9
    >>> den(c)
    20
    """
    "*** YOUR CODE HERE ***"

def eq_rat(a, b):
    """Returns True if two rational numbers A and B are equal. For
    example, (2 / 3) = (6 / 9), so eq_rat would return True.

    >>> a, b = make_rat(2, 3), make_rat(6, 9)
    >>> eq_rat(a, b)
    True
    >>> c, d = make_rat(1, 4), make_rat(1, 2)
    >>> eq_rat(c, d)
    False
    """
    "*** YOUR CODE HERE ***"



## Challenge Question ##

def depth(t, v):
    """Returns the depth of value v in tree t if v is contained in t.
    If v is not in t, return None.

    >>> test_tree = tree(1,
    ...                  (tree(2,
    ...                        (tree(3,
    ...                              (tree(4),
    ...                               tree(5))),
    ...                         tree(6,
    ...                              (tree(7),
    ...                               tree(8))))),
    ...                  (tree(9,
    ...                        (tree(10,
    ...                              (tree(11),
    ...                               tree(12))),
    ...                         tree(13,
    ...                              (tree(14),
    ...                               tree(15))))))))
    >>> depth(test_tree, 1)
    0
    >>> depth(test_tree, 42) # Returns None
    >>> depth(test_tree, 6)
    2
    >>> depth(test_tree, 15)
    3
    """
    "*** YOUR CODE HERE ***"

