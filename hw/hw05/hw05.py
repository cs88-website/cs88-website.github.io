## Debug This
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


## MapReduce

def map(f, s):
    """
    Map a function f onto a sequence.

    >>> def double(x):
    ...     return x * 2
    >>> def square(x):
    ...     return x ** 2
    >>> def toLetter(x):
    ...     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ...     return alpha[x%26]
    >>> map(double, [1,2,3,4])
    [2, 4, 6, 8]
    >>> map(square, [1, 2, 3, 4, 5, 10])
    [1, 4, 9, 16, 25, 100]
    >>> map(toLetter, [3, 0, 19, 0])
    ['d', 'a', 't', 'a']

    """
    if s == []:
        return s
    return [f(s[0])] + map(f, s[1:])


def filter(f, s):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    "*** YOUR CODE HERE ***"
    


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
    


# Recursive Math

def decimal(n):
    """Return a list representing the decimal representation of a number.

    >>> decimal(55055)
    [5, 5, 0, 5, 5]
    >>> decimal(-136)
    ['-', 1, 3, 6]
    """
    "*** YOUR CODE HERE ***"


def binary(n):
    """Return a list representing the representation of a number in base 2.

    >>> binary(55055)
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
    >>> binary(-136)
    ['-', 1, 0, 0, 0, 1, 0, 0, 0]
    """
    "*** YOUR CODE HERE ***"


def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    >>> count_digit(1231421, 1)
    3
    >>> count_digit(12, 3)
    0
    """
    "*** YOUR CODE HERE ***"


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"



# Challenge

def count_change(amount, denominations):
    """Returns the number of ways to make change for amount.

    >>> denominations = [50, 25, 10, 5, 1]
    >>> count_change(7, denominations)
    2
    >>> count_change(100, denominations)
    292
    >>> denominations = [16, 8, 4, 2, 1]
    >>> count_change(7, denominations)
    6
    >>> count_change(10, denominations)
    14
    >>> count_change(20, denominations)
    60
    """
    "*** YOUR CODE HERE ***"


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"

