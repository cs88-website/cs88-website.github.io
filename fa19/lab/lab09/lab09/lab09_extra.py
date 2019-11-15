from lab09 import *
# Q6
def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    result = []
    while link is not Link.empty:
        result.append(link.first)
        link = link.rest
    return result

# Q7
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    # BEGIN SOLUTION
    lists = set()
    while link is not Link.empty:
        if link in lists:
            return True
        lists.add(link)
        link = link.rest
    return False
