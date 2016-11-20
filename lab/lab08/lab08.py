#############
# Exeptions #
#############

def avoid_indexerror(lst, index, missing=None):
    """Return lst[index] if it exists, otherwise missing.

    >>> avoid_indexerror([1,2,3], 1)
    2
    >>> avoid_indexerror([1,2,3], 4)
    >>> avoid_indexerror([1,2,3], 4, "Index out of range.")
    'Index out of range.'
    """
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

