## List Comprehensions ##

def tax(shopping_cart, percent):
    """
    Adds a `percent` tax to each item's price in a shopping cart.

    >>> fruitCart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> tax(fruitCart, 10)
    [ (apple, 0.55, 3), (banana, 0.275, 4)]

    >>> calCart = [("oski", 1000, 1), ("go", 1, 2), ("bears", 3.5, 2)]
    >>> tax(calCart, 100)
    [("oski", 2000, 1), ("go", 2, 2), ("bears", 7, 2)]

    """
    "*** YOUR CODE HERE ***"
    return ______
    
def cartSum(shopping_cart):
    """
    Sums a shopping cart

    >>> fruitCart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> taxedFruit = tax(fruitCart, 10)
    [ (apple, 0.55, 3), (banana, 0.275, 4)]
    >>> cartSum(taxedFruit)
    2.75
    >>> calCart = [("oski", 1000, 1), ("go", 1, 2), ("bears", 3.5, 2)]
    >>> taxedCal = tax(calCart, 100)
    [("oski", 2000, 1), ("go", 5.5, 4), ("bears", 13.2, 4)]
    >>> cartSum(taxedCal)
    2018

    """
    "*** YOUR CODE HERE ***"
    return ______


## Conditionals ##

def arange(start, end, step=1):
    """
    arange behaves just like np.arange(start, end, step).
    You only need to support positive values for step.

    >>> arange(1, 3)
    [ 1, 2]
    >>> arange(0, 25, 2)
    [ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24]
    >>> arange(0, 1231, 34)
    [   0,   34,   68,  102,  136,  170,  204,  238,  272,  306,  340,
            374,  408,  442,  476,  510,  544,  578,  612,  646,  680,  714,
            748,  782,  816,  850,  884,  918,  952,  986, 1020, 1054, 1088,
           1122, 1156, 1190, 1224]

    """
    "*** YOUR CODE HERE ***"
    return ______


## Iteration ##

def minmax(s):
    """Return the minimum and maximum elements of a sequence.

    >>> minmax([1, 2, -3])
    (-3, 2)
    >>> minmax([2])
    (2, 2)
    >>> minmax([])
    (None, None)
    """
    "*** YOUR CODE HERE ***"



## Challenge Question ##
