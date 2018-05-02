## Exceptions

def avoid_indexerror(lst, index, missing=None):
    """Return lst[index] if it exists, otherwise missing.

    >>> avoid_indexerror([1,2,3], 1)
    2
    >>> avoid_indexerror([1,2,3], 4)
    >>> avoid_indexerror([1,2,3], 4, "Index out of range.")
    'Index out of range.'
    """
    "*** YOUR CODE HERE ***"
    # BEGIN SOLUTION
    try:
        return lst[index]
    except IndexError:
        return missing
    # END SOLUTION


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
    # BEGIN SOLUTION
    try:
        return dictionary[key]
    except KeyError as e:
        print("Avoid Exception")
        dictionary[key] = 'no value'
    # END SOLUTION


## Generators

def char_gen(s):
    """
    >>> for char in char_gen("hello"):
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    """
    "*** YOUR CODE HERE ***"
    # BEGIN SOLUTION
    for char in s:
        yield char
    # END SOLUTION


def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    # BEGIN SOLUTION
    while n >= 0:
        yield n
        n = n - 1
    # END SOLUTION


from math import sqrt

def is_prime(n):
    """
    Return True if n is prime, false otherwise.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(19)
    True
    """
    "*** YOUR CODE HERE ***"
    # BEGIN SOLUTION
    if n < 2:
        return False
    counter = 2
    while counter <= sqrt(n):
        if n % counter == 0:
            return False
        counter += 1
    return True
    # END SOLUTION

def primes():
    """
    An infinite generator that outputs primes. 

    >>> p = primes()
    >>> for i in range(3):
    ...     print(next(p))
    ...
    2
    3
    5
    """
    "*** YOUR CODE HERE ***"
    # BEGIN SOLUTION
    num = 0
    while True:
        if is_prime(num):
            yield num
        num += 1
    # END SOLUTION



## Sequences

def count_palindromes(L):
    """The number of palindromic words in the sequence of strings
    L (ignoring case).

    >>> count_palindromes(("Acme", "Madam", "Pivot", "Pip"))
    2
    """
    "*** YOUR CODE HERE ***"
    count = 0
    for word in L:
        if word == word[::-1]:
            count += 1
    return count 



## Naturals generator, needed for doctests

def naturals():
    i = 1
    while True:
        yield i
        i += 1