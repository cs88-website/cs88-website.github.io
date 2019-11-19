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
class Person:
    def __init__(self, name, ethnicity={}):
        self.name = name
        assert type(ethnicity) == dict
        for i in ethnicity.values():
            assert type(i) == float
        self.ethnicity = ethnicity

    def __repr__(self):
        return self.name

class Family:
    def __init__(self, parents, children={}):
        # Leaf families have one parent and no children
        self.parents = parents
        self.children = children
        if not self.is_leaf():
            for p in parents:
                assert isinstance(p, Person)
            for child, tree in children.items():
                assert isinstance(child, Person)
                assert isinstance(tree, Family)

    def __repr__(self):
        if self.is_leaf():
            return self.parents[0].name
        else:
            children_str = ', ' + repr(self.children)
        return 'Parents:{} Children:{})'.format([i.name for i in self.parents], children_str)

    def is_leaf(self):
        return self.children == {}

    def get_ethnicities(self):
        return [parent.ethnicity for parent in self.parents]


def computeAncesTree(t):
    """
    Fill in the ethnicities of all descendants.
    >>> gma1 = Person("Farah", {"Moroccan": 100.0})
    >>> gpa1 = Person("Lorenzo", {"Italian" : 100.0})
    >>> gpa2 = Person("Hai", {"Chinese":100.0})
    >>> gma2 = Person("Gazala", {"Indian":100.0})
    >>> papa1 = Person("Amjad") #  Son of Farah and Lorenzo
    >>> papa2 = Person("Arjun") # Son of Hai and Gazala
    >>> mama1 = Person("Anabella") # Daughter of Farah and Lorenzo
    >>> mama2 = Person("Biyu") # Daughter of Hai and Gazala
    >>> c1 = Person("Dipika") # Daughter of Arjun and Anabella
    >>> c2 = Person("Cosimo") # Son of Arjun and Anabella
    >>> c3 = Person("Jin") # Son of Amjad and Biyu
    >>> c4 = Person("Malika") # Daughter of Amjad and Biyu
    >>> leaves = [Family([c]) for c in [c1, c2, c3, c4]]
    >>> fam1 = Family([papa2, mama1], {c1:leaves[0], c2:leaves[1]})
    >>> fam2 = Family([papa1, mama2], {c3:leaves[2], c4:leaves[3]})
    >>> t1 = Family([gpa1, gma1], {papa1:fam2, mama1:fam1})
    >>> t2 = Family([gpa2, gma2], {papa2:fam1, mama2:fam2})
    >>> computeAncesTree(t1)
    >>> papa1.ethnicity == mama1.ethnicity
    True
    >>> c1.ethnicity == c2.ethnicity == c3.ethnicity == c4.ethnicity
    True
    >>> computeAncesTree(t2)
    >>> papa2.ethnicity == mama2.ethnicity
    True
    >>> eth = {a:25.0 for a in ["Moroccan", "Italian", "Chinese", "Indian"]}
    >>> c1.ethnicity == c2.ethnicity == c3.ethnicity == c4.ethnicity == eth
    True
    >>> sidepa = Person("Kahlil Gibran", {"Lebanese":75.0, "Moroccan":25.0})
    >>> secret = Person("نبي")
    >>> secretFam = Family([secret])
    >>> t3 = Family([sidepa, gma1], {secret:secretFam})
    >>> computeAncesTree(t3)
    >>> eth2 = {"Lebanese":37.5, "Moroccan":62.5}
    >>> secret.ethnicity == eth2
    True
    """
    "*** YOUR CODE HERE ***"

