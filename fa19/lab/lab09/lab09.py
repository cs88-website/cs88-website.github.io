## Recursive Objects ##

# Linked List Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

def print_link(link):
    """Print elements of a linked list link.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> link1 = Link(1, Link(Link(2), Link(3)))
    >>> print_link(link1)
    <1 <2> 3>
    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> print_link(link1)
    <3 <4> 5 6>
    """
    print('<' + helper(link).rstrip() + '>')

def helper(link):
    if link == Link.empty:
        return ''
    elif isinstance(link.first, Link):
        return '<' + helper(link.first).rstrip() + '> ' + helper(link.rest)
    else:
        return str(link.first) +' '+  helper(link.rest)

# Tree Class
class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.entry, branches_str)

    def is_leaf(self):
        return not self.branches



# Q2
def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> print_link(link)
    <1 2 3>
    """
    "*** YOUR CODE HERE ***"


# Q3
def insert(link, value, index):
    """Insert a value into a Link at the given index.

    >>> link = Link(1, Link(2, Link(3)))
    >>> print_link(link)
    <1 2 3>
    >>> insert(link, 9001, 0)
    >>> print_link(link)
    <9001 1 2 3>
    >>> insert(link, 100, 2)
    >>> print_link(link)
    <9001 1 100 2 3>
    >>> insert(link, 4, 5)
    IndexError
    """
    "*** YOUR CODE HERE ***"


# Q5
def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape if they have the same number of branches and each of their
    children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(7)])
    >>> same_shape(t, s)
    False
    """
    "*** YOUR CODE HERE ***"


# Q6
class FamilyTree:
    def __init__(self, name, ethnicity, parents=[]):
        # Leaf FamilyTrees have no parents
        self.name = name
        self.ethnicity = ethnicity
        self.parents = parents
        if not self.is_leaf():
            for p in parents:
                assert isinstance(p, FamilyTree)

    def __repr__(self):
        if self.is_leaf():
            return self.name
        return '{} child of {}'.format(self.name, repr(self.parents))

    def is_leaf(self):
        return len(self.parents) == 0


def computeAncesTree(t):
    """
    Fill in the ethnicities of all parents.
    >>> gma1 = FamilyTree("Farah", {"Moroccan": 100.0})
    >>> gpa1 = FamilyTree("Lorenzo", {"Italian" : 100.0})
    >>> gpa2 = FamilyTree("Hai", {"Chinese":100.0})
    >>> gma2 = FamilyTree("Gazala", {"Indian":100.0})
    >>> papa1 = FamilyTree("Amjad", {}, [gma1, gpa1]) #  Son of Farah and Lorenzo
    >>> papa2 = FamilyTree("Arjun", {}, [gma2, gpa2]) # Son of Hai and Gazala
    >>> mama1 = FamilyTree("Anabella", {}, [gma1, gpa1]) # Daughter of Farah and Lorenzo
    >>> mama2 = FamilyTree("Biyu", {}, [gma2, gpa2]) # Daughter of Hai and Gazala
    >>> c1 = FamilyTree("Dipika", {}, [mama1, papa2]) # Daughter of Arjun and Anabella
    >>> c2 = FamilyTree("Cosimo", {}, [mama1, papa2]) # Son of Arjun and Anabella
    >>> c3 = FamilyTree("Jin", {}, [mama2, papa1]) # Son of Amjad and Biyu
    >>> c4 = FamilyTree("Malika", {}, [mama2, papa1]) # Daughter of Amjad and Biyu
    >>> eth = {a:25.0 for a in ["Moroccan", "Italian", "Chinese", "Indian"]}
    >>> computeAncesTree(c1) == eth
    True
    >>> mama1.ethnicity["Moroccan"] == 50.0 and mama1.ethnicity["Italian"] == 50.0
    True
    >>> papa2.ethnicity["Indian"] == 50.0 and papa2.ethnicity["Chinese"] == 50.0
    True
    >>> mama2.ethnicity == papa1.ethnicity == c2.ethnicity == c3.ethnicity == c4.ethnicity
    True
    >>> computeAncesTree(c2) == computeAncesTree(c3) == computeAncesTree(c4) == eth
    True
    >>> papa1.ethnicity == mama1.ethnicity
    True
    >>> papa2.ethnicity == mama2.ethnicity
    True
    >>> sidepa = FamilyTree("Kahlil Gibran", {"Lebanese":75.0, "Moroccan":25.0})
    >>> secret = FamilyTree("The Prophet", {}, [gma1, sidepa])
    >>> eth2 = {"Lebanese":37.5, "Moroccan":62.5}
    >>> computeAncesTree(secret) == eth2
    True
    """
    "*** YOUR CODE HERE ***"

