######################
# Required Questions #
######################

def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"


# Recursive Min Sort

# Helper function
def first(s):
    """Return the first element in a sequence."""
    return s[0]

# Helper function
def rest(s):
    """Return all elements in a sequence after the first"""
    return s[1:]

# Helper function
def rmin(s):
    """Return the minimum value in a sequence."""
    if len(s) == 1:
        return first(s)
    else:
        return min(first(s), rmin(rest(s)))

# Helper function
def remove(to_remove, s):
    """Returns the sequence s with the first occurrence of to_remove taken out."""
    if s == []:
        return []
    if first(s) == to_remove:
        return rest(s)
    else:
        return [first(s)] + remove(to_remove, rest(s))

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


###################
# Extra Questions #
###################

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

