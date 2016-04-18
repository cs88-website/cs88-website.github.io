#############
# Exeptions #
#############

def quiet_get(data, selector, missing=None):
    """Return data[selector] if it exists, otherwise missing.

    >>> quiet_get([1,2,3], 1)
    2
    >>> quiet_get([1,2,3], 4)
    >>> quiet_get({'a':2, 'b':5}, 'a', -1)
    2
    >>> quiet_get({'a':2, 'b':5}, 'd', -1)
    -1
    """
    try:
        return data[selector]
    "*** YOUR CODE HERE ***"


def avoid_keyerror(dictionary, key):
    """ Returns the value associated with key in dictionary. If key 
    does not exist in the dictionary, print out 'Avoid Exception' and
    map it to the string 'no value'.

    >>> d = {1: 'one', 3: 'three', 5: 'five'}
    >>> avoid_keyerror(d, 3)
    'three'
    >>> avoid_keyerror(d, 4)
    Avoid Exception
    >>> d[4]
    'no value'
    """
    "*** YOUR CODE HERE ***"


def safe_sum(fun, seq, missing=0):
    """Return the sum of fun applied to elements in seq using missing as a replacement
    for those elements on which fun throws an exception

    >>> safe_sum(lambda x: 1/x, [1, 2, 0, 3, None, "bad"])
    1.8333333333333333
    """
    def wrap(fun, x):
        "*** YOUR CODE HERE ***"

    psum = 0
    for x in seq:
        psum += wrap(fun, x)
    return psum

