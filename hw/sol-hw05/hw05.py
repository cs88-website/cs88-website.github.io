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

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)


##pyTunes

def make_pytunes(username):
    """Return a pyTunes tree as shown in the diagram with USERNAME as the value
    of the root.

    >>> pytunes = make_pytunes('i_love_music')
    >>> print_tree(pytunes)
    i_love_music
      pop
        kesha
          single
            praying
        2017 pop mashup
      trance
        darude
          sandstorm
    """
    return tree(username, 
             [tree('pop', 
               [tree('kesha',
                 [tree('single',
                   [tree('praying')])]),
                tree('2017 pop mashup')]),
              tree('trance',
                [tree('darude', 
                  [tree('sandstorm')])])])


def num_songs(t):
    """Return the number of songs in the pyTunes tree, t.

    >>> pytunes = make_pytunes('i_love_music')
    >>> num_songs(pytunes)
    3
    """
    if is_leaf(t):
        return 1
    return sum([num_songs(b) for b in branches(t)])

# Alternate solution
def num_songs(t):
    if is_leaf(t):
        return 1
    leaves = 0
    for b in branches(t):
        leaves += num_songs(b)
    return leaves


def find(t, target):
    """Returns True if t contains a node with the value TARGET and False
    otherwise.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> find(my_account, 'korean')
    True
    >>> find(my_account, 'blank space')
    True
    >>> find(my_account, 'bad blood')
    False
    """
    if root(t) == target:
        return True
    if is_leaf(t):
        return False
    return any([find(b, target) for b in branches(t)])

# Alternate solution
def find(t, target):
    if root(t) == target:
        return True
    for b in branches(t):
        if find(b, target):
            return True
    return False


def add_song(t, song, category):
    """Returns a new tree with SONG added to CATEGORY. Assume the CATEGORY
    already exists.

    >>> indie_tunes = tree('indie_tunes',
    ...                  [tree('indie',
    ...                    [tree('alvvays',
    ...                       [tree('archie, marry me')])])])
    >>> new_indie = add_song(indie_tunes, 'dreams tonite', 'alvvays')
    >>> print_tree(new_indie)
    indie_tunes
      indie
        alvvays
          archie, marry me
          dreams tonite

    """
    if root(t) == category:
        return tree(root(t), branches(t) + [tree(song)])
    kept_branches = []
    for b in branches(t):
        kept_branches += [add_song(b, song, category)]
    return tree(root(t), kept_branches)

# Alternative Solution
def add_song(t, song, category):
    if root(t) == category:
        return tree(root(t), branches(t) + [tree(song)])
    all_branches = [add_song(b, song, category) for b in branches(t)]
    return tree(root(t), all_branches)


def delete(t, target):
    """Returns the tree that results from deleting TARGET from t. If TARGET is
    a category, delete everything inside of it.

    >>> my_account = tree('kpop_king',
    ...                    [tree('korean',
    ...                          [tree('gangnam style'),
    ...                           tree('wedding dress')]),
    ...                     tree('pop',
    ...                           [tree('t-swift',
    ...                                [tree('blank space')]),
    ...                            tree('uptown funk'),
    ...                            tree('see you again')])])
    >>> new = delete(my_account, 'pop')
    >>> print_tree(new)
    kpop_king
      korean
        gangnam style
        wedding dress
    """
    kept_branches = []
    for b in branches(t):
        if root(b) != target:
            kept_branches += [delete(b, target)]
    return tree(root(t), kept_branches)

# Alternate solution
def delete(t, target): 
    kept_branches = [delete(b, target) for b in branches(t) if root(b) != target]
    return tree(root(t), kept_branches)



#Mutation 

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    attempts = []
    def withdraw(amount, password_attempt):
        nonlocal balance
        if len(attempts) == 3:
            return 'Your account is locked. Attempts: ' + str(attempts)
        if password_attempt != password:
            attempts.append(password_attempt)
            return 'Incorrect password'
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    error = withdraw(0, old_password)
    if type(error) == str:
        return error
    def joint(amount, password_attempt):
        if password_attempt == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, password_attempt)
    return joint


