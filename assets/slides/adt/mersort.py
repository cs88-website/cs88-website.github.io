def merge(lst1, lst2, key_fun):
    """Merge two sorted lists using the key_fun function to get the key for <= comparison.

    >>> merge([(1,2),(3,1)], [(2,4),(3,2),(4,5)], lambda x:x[0])
    [(1, 2), (2, 4), (3, 1), (3, 2), (4, 5)]
    >>> merge([(3, 1), (1, 2)],  [(3, 2), (2, 4), (4, 5)], lambda x:x[1])
    [(3, 1), (1, 2), (3, 2), (2, 4), (4, 5)]
    >>> merge([], [2, 4, 6], lambda x:x)
    [2, 4, 6]
    >>> merge([1, 2, 3], [], lambda x:x)
    [1, 2, 3]
    """
    new = []
    while lst1 and lst2:
        if key_fun(lst1[0]) <= key_fun(lst2[0]):
            new += [lst1[0]]
            lst1 = lst1[1:]
        else:
            new += [lst2[0]]
            lst2 = lst2[1:]
    if lst1:
        return new + lst1
    else:
        return new + lst2

def msort(lst, key_fun):
    """Return sorted list using a merge sort.
    Split the list into two halves (i.e., lengths differ by <= 1)
    Sort each and merge.

    >>> msort([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], lambda x:x[0])
    [(1, 'how'), (2, 'hi'), (5, 'goes'), (7, 'I')]
    >>> msort([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], lambda x:x[1])
    [(7, 'I'), (5, 'goes'), (2, 'hi'), (1, 'how')]
    >>> msort([1,2,3,4,5], lambda x: x)
    [1, 2, 3, 4, 5]
    >>> msort([1,2,3,4,5], lambda x: -x)
    [5, 4, 3, 2, 1]
    >>> msort([(2, "hi"), (1, "how"), (5, "goes"), (7, "I")], lambda x: len(x[1]))
    [(7, 'I'), (2, 'hi'), (1, 'how'), (5, 'goes')]
    """
    if len(lst) < 2:
        return lst
    else:
        mid = len(lst)//2
        left = lst[0:mid]
        right = lst[mid:]
        return merge(msort(left, key_fun),msort(right, key_fun), key_fun)

