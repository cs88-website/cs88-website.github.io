######################
# Required Questions #
######################

def bad_list_flattener(lst1, lst2):
    """
    Flattens both lst1 and lst2, and returns the 
    concatenation of the two flattened lists. Flattening 
    a list means to collapse the list into one 
    dimension (like np.flatten).
    >>> girls = [['Rachel', 'Green'], ['Phoebe', 'Buffay']]
    >>> boys = [['Ross', 'Geller'], ['Chandler', 'Bing']]
    >>> bad_list_flattener(girls, boys)
    ['Rachel', 'Green', 'Phoebe', 'Buffay', 'Ross', 'Geller', 'Chandler', 'Bing']
    >>> cats = [['Persian'], ['British', 'Shorthair']]
    >>> dogs = [['Golden', 'Retriever']]
    >>> bad_list_flattener(dogs, cats)
    ['Golden', 'Retriever', 'Persian', 'British', 'Shorthair']
    """
    newlist1 = []
    newlist2 = []
    for inner_lst in lst1:
        for item in inner_lst:
            newlist1 += item
    for inner_lst in lst2:
        for item in inner_lst:
            newlist2 += item
    return newlist1 + newlist2


def is_palindrome(lst):
    """ Returns True if the list is a palindrome. A palindrome is a list 
    that reads the same forwards as backwards
    >>> is_palindrome([1, 2, 3, 4, 5])
    False
    >>> is_palindrome(["p", "a", "l", "i", "n", "d", "r", "o", "m", "e"])
    False
    >>> is_palindrome([True, False, True])
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome(["racecar", "racecar"])
    True
    >>> is_palindrome(["r", "a", "c", "e", "c", "a", "r"])
    True
    """
    "*** YOUR CODE HERE ***"


def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"



def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"



# Iterative solution, if you're curious
def gcd_iter(a, b):
    """Returns the greatest common divisor of a and b, using iteration.

    >>> gcd_iter(34, 19)
    1
    >>> gcd_iter(39, 91)
    13
    >>> gcd_iter(20, 30)
    10
    >>> gcd_iter(40, 40)
    40
    """
    if a < b:
        a, b = b, a
    while a > b and not a % b == 0:
        a, b = b, a % b
    return b



def add_matrices(x, y):
    """
    >>> matrix1 = [[1, 3],
    ...            [2, 0]]
    >>> matrix2 = [[-3, 0],
    ...            [1, 2]]
    >>> add_matrices(matrix1, matrix2)
    [[-2, 3], [3, 2]]
    """
    "*** YOUR CODE HERE ***"
    


def mul_by_num(num):
    """
    Returns a function that takes one argument and returns num
    times that argument.
    >>> x = mul_by_num(5)
    >>> y = mul_by_num(2)
    >>> x(3)
    15
    >>> y(-4)
    -8
    """
    "*** YOUR CODE HERE ***"
    


def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"


######################
# Extra Optional Questions #
######################

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

