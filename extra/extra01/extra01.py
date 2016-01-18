##################################
# Newton's method (from lecture) #
##################################

def improve(update, close, guess=1, max_updates=100):
    """Iteratively improve guess with update until close(guess) is true."""
    k = 0
    while not close(guess) and k < max_updates:
        guess = update(guess)
        k = k + 1
    return guess

def approx_eq(x, y, tolerance=1e-15):
    """Whether x is within tolerance of y."""
    return abs(x - y) < tolerance

def find_zero(f, df):
    """Return a zero of the function f with derivative df."""
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def newton_update(f, df):
    """Return an update function for f with derivative df."""
    def update(x):
        return x - f(x) / df(x)
    return update

def nth_root_of_a(n, a):
    """Return the nth root of a.

    >>> nth_root_of_a(2, 64)
    8.0
    >>> nth_root_of_a(3, 64)
    4.0
    >>> nth_root_of_a(6, 64)
    2.0
    """
    return find_zero(lambda x: pow(x, n) - a, lambda x: n * pow(x, n-1))



#############
# Questions #
#############

def intersect(f, df, g, dg):
    """Return where f with derivative df intersects g with derivative dg.

    >>> parabola, line = lambda x: x*x - 2, lambda x: x + 10
    >>> dp, dl = lambda x: 2*x, lambda x: 1
    >>> intersect(parabola, dp, line, dl)
    4.0
    """
    "*** YOUR CODE HERE ***"


# Huffman encoding trees

def huffman_leaf(letter, weight):
    """A leaf of a Huffman tree, which has a weight at the root."""
    return tree(weight, [tree(letter)])

def huffman_tree(left, right):
    """A Huffman encoding tree; left and right are also Huffman trees."""
    return tree(root(left) + root(right), [left, right])

def weight(tree):
    """The weight of a Huffman encoding tree."""
    return root(tree)

def is_huffman_leaf(tree):
    """Whether this Huffman tree is a Huffman leaf."""
    return not is_leaf(tree) and is_leaf(branches(tree)[0])

def letter(leaf):
    """The letter of a Huffman leaf."""
    return root(branches(leaf)[0])

# Trees (from lecture)
def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root] + list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

CD = huffman_tree(huffman_leaf('c', 1), huffman_leaf('d', 1))
EF = huffman_tree(huffman_leaf('e', 1), huffman_leaf('f', 1))
GH = huffman_tree(huffman_leaf('g', 1), huffman_leaf('h', 1))
EFGH = huffman_tree(EF, GH)
BCD = huffman_tree(huffman_leaf('b', 3), CD)
BCDEFGH = huffman_tree(BCD, EFGH)
example_tree = huffman_tree(huffman_leaf('a', 8), BCDEFGH)

def letters(tree):
    """Return a list of all letters encoded in Huffman encoding TREE.

    >>> letters(example_tree)
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    "*** YOUR CODE HERE ***"

def decode(tree, code):
    """Decode CODE, a list of 0's and 1's using the Huffman encoding TREE.

    >>> decode(example_tree, [1, 0, 0, 0, 1, 1, 1, 1])
    'bah'
    """
    word = ''
    while code:
        word += decode_one(tree, code)
    return word

def decode_one(tree, code):
    """Decode and remove the first letter in CODE, using TREE.

    >>> code = [1, 0, 0, 0, 1, 1, 1, 1]
    >>> decode_one(example_tree, code)
    'b'
    >>> code # The initial 1, 0, and 0 are removed by decode_one
    [0, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"

def encodings(tree):
    """Return all encodings in a TREE as a dictionary that maps symbols to
    bit lists.

    >>> e = encodings(example_tree)
    >>> set(e.keys()) == set('abcdefgh')
    True
    >>> e['a']
    [0]
    >>> e['c']
    [1, 0, 1, 0]
    >>> e['h']
    [1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"

def huffman(frequencies):
    """Return a Huffman encoding for FREQUENCIES, a list of (symbol,
    frequency) pairs.

    >>> frequencies = [('a', 8), ('b', 3), ('c', 1), ('d', 1)]
    >>> h = huffman(frequencies)
    >>> for letter, code in sorted(encodings(h).items()):
    ...     print(letter + ':', code)
    a: [1]
    b: [0, 1]
    c: [0, 0, 0]
    d: [0, 0, 1]
    """
    frequencies.sort(key=lambda freq: freq[1]) # lowest frequencies first
    leaves = [huffman_leaf(letter, freq) for letter, freq in frequencies]
    "*** YOUR CODE HERE ***"

def huffman_wiki():
    """Return a Huffman encoding tree for the text of the Huffman coding page
    on Wikipedia. (Internet connection required!)

    >>> e = encodings(huffman_wiki())
    >>> [[letter, e[letter]] for letter in ['a', 'b', 'c']]
    [['a', [0, 0, 1, 0]], ['b', [1, 0, 0, 0, 1, 0]], ['c', [0, 1, 0, 1, 1]]]
    """
    from urllib.request import urlopen
    from json import loads
    from collections import Counter
    huff = urlopen('http://goo.gl/w1Jdjj').read().decode()
    content = loads(huff)['query']['pages']['13883']['revisions'][0]['*']
    return huffman(list(Counter(content).items()))


#######################
# Challenge Questions #
#######################

X = lambda x, derive: 1 if derive else x
K = lambda k: lambda x, derive: 0 if derive else k

def quadratic(a, b, c):
    """Return a quadratic polynomial a*x*x + b*x + c.

    >>> q_and_dq = quadratic(1, 6, 8) # x*x + 6*x + 8
    >>> q_and_dq(1.0, False)  # value at 1
    15.0
    >>> q_and_dq(1.0, True)   # derivative at 1
    8.0
    >>> q_and_dq(-1.0, False) # value at -1
    3.0
    >>> q_and_dq(-1.0, True)  # derivative at -1
    4.0
    """
    A, B, C = K(a), K(b), K(c)
    AXX = mul_fns(A, mul_fns(X, X))
    BX = mul_fns(B, X)
    return add_fns(AXX, add_fns(BX, C))

def add_fns(f_and_df, g_and_dg):
    """Return the sum of two polynomials."""
    "*** YOUR CODE HERE ***"

def mul_fns(f_and_df, g_and_dg):
    """Return the product of two polynomials."""
    "*** YOUR CODE HERE ***"

def poly_zero(f_and_df):
    """Return a zero of polynomial f_and_df, which returns:
        f(x)  for f_and_df(x, False)
        df(x) for f_and_df(x, True)

    >>> q = quadratic(1, 6, 8)
    >>> round(poly_zero(q), 5) # Round to 5 decimal places
    -2.0
    >>> round(poly_zero(quadratic(-1, -6, -9)), 5)
    -3.0
    """
    "*** YOUR CODE HERE ***"


