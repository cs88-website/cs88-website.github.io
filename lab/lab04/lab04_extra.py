from lab04 import *

# Q9
# Iterative min sort
def first(s):
    return s[0]

def rest(s):
    return s[1:]

def imin(s):
    """Return the minimum value in a sequence.

    >>> imin([3,1,2])
    1
    """
    "*** YOUR CODE HERE ***"

def iremove(x, s):
    """Remove first element equal to x from sequence s.

    >>> iremove(1,[])
    []
    >>> iremove(1,[1])
    []
    >>> iremove(1,[1,1])
    [1]
    >>> iremove(1,[2,1])
    [2]
    >>> iremove(1,[3,1,2])
    [3, 2]
    >>> iremove(1,[3,1,2,1])
    [3, 2, 1]
    >>> iremove(5, [3, 5, 2, 5, 11])
    [3, 2, 5, 11]
    """
    "*** YOUR CODE HERE ***"

def minsort(s):
    """Sort sequence s in ascending order.
    
    >>> minsort([])
    []
    >>> minsort([1])
    [1]
    >>> minsort([1, 1, 1])
    [1, 1, 1]
    >>> minsort([1, 2, 3])
    [1, 2, 3]
    >>> minsort([3, 2, 1])
    [1, 2, 3]
    >>> minsort([1, 2, 1])
    [1, 1, 2]
    >>> minsort([1,2,3, 2, 1])
    [1, 1, 2, 2, 3]
    """
    "*** YOUR CODE HERE ***"


# Q10
def leq_maker(i):
    """Return a less_equal function that compares the i-th elements of two sequences.

    >>> leq_maker(0)((1,3),(2,2))
    True
    >>> leq_maker(1)((1,3),(2,2))
    False
    """
    "*** YOUR CODE HERE ***"

def first(s):
    return s[0]
def rest(s):
    return s[1:]

def merge_hof(lst1, lst2, leq):
    """Merge two sorted lists using the leq function to compare elements.

    >>> merge_hof([(1,2),(3,1)], [(2,4),(3,2),(4,5)], leq_maker(0))
    [(1, 2), (2, 4), (3, 1), (3, 2), (4, 5)]
    >>> merge_hof([(3, 1), (1, 2)],  [(3, 2), (2, 4), (4, 5)], leq_maker(1))
    [(3, 1), (1, 2), (3, 2), (2, 4), (4, 5)]
    >>> merge_hof([], [2, 4, 6], lambda x,y: x<=y )
    [2, 4, 6]
    >>> merge_hof([1, 2, 3], [], lambda x,y: x<=y )
    [1, 2, 3]
    """
    # recursive
    "*** YOUR CODE HERE ***"

# Iterative solution 
def merge_hof_iter(lst1, lst2, leq):
    """Merge two sorted lists using the leq function to compare element.

    >>> merge_hof_iter([(1,2),(3,1)], [(2,4),(3,2),(4,5)], leq_maker(0))
    [(1, 2), (2, 4), (3, 1), (3, 2), (4, 5)]
    >>> merge_hof_iter([(3, 1), (1, 2)],  [(3, 2), (2, 4), (4, 5)], leq_maker(1))
    [(3, 1), (1, 2), (3, 2), (2, 4), (4, 5)]
    >>> merge_hof_iter([], [2, 4, 6], lambda x,y: x<=y )
    [2, 4, 6]
    >>> merge_hof_iter([1, 2, 3], [], lambda x,y: x<=y )
    [1, 2, 3]
    """
    "*** YOUR CODE HERE ***"

def merge_hof_sort(lst, leq):
    """Return sorted list using a merge sort.
    Split the list into two halves (i.e., lengths differ by <= 1)
    Sort each and merge.

    >>> merge_hof_sort([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], leq_maker(0)) 
    [(1, 'how'), (2, 'hi'), (5, 'goes'), (7, 'I')]
    >>> merge_hof_sort([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], leq_maker(1)) 
    [(7, 'I'), (5, 'goes'), (2, 'hi'), (1, 'how')]
    >>> merge_hof_sort([1,2,3,4,5], lambda x,y: x<=y)
    [1, 2, 3, 4, 5]
    >>> merge_hof_sort([1,2,3,4,5], lambda x,y: x>=y)
    [5, 4, 3, 2, 1]
    >>> merge_hof_sort([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], lambda x,y: len(x[1]) <= len(y[1]))
    [(7, 'I'), (2, 'hi'), (1, 'how'), (5, 'goes')]
    """
    "*** YOUR CODE HERE ***"

