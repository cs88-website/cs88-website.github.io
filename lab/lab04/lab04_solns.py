import string

## Code to generate list of shakespear words
def word_generator(filename):
    """
    Returns a generator over the words in a txt file.
    """
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                yield word.lower().strip(string.punctuation)

## Shakespeare words list
shakespeare_list = list(word_generator("shakespeare.txt"))



## Mutation Mystery

## Case 3

def deep_copy(lst):
    """Returns a new list that is a deep copy of lst.
    >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
    >>> y = deep_copy(x)
    >>> y[0][1] = 'z'
    >>> y
    [[0, 'z'], [1, 'b'], [2, 'c']]
    >>> x
    [[0, 'a'], [1, 'b'], [2, 'c']]
    >>> x = [[0, 'a'],  [1, 'b'], [2, 'c']]
    >>> z = deep_copy(x)
    >>> z[0][1] = 'z'
    >>> z
    [[0, 'z'], [1, 'b'], [2, 'c']]
    >>> x       #x should not change
    [[0, 'a'], [1, 'b'], [2, 'c']]
    """
    "*** YOUR CODE HERE ***"
    copy = []
    for elem in lst:
        if isinstance(elem, list):
            copy.append(deep_copy(elem))
        else:
            copy.append(elem)
    return copy


## Explanation
def case3_explanation():
    return "Format your explanation for the mystery\
            as a string that spans multiple lines, \
            like this. Keep explanations short, you\
            don't need more than a few sentences."


## Dictionary Mutation 

def word_count_dictionary(word_list):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input list of words.

    >>> d = word_count_dictionary(shakespeare_list)
    >>> d["the"]
    51
    >>> d["but"]
    12
    >>> d["thy"]
    5
    """
    "*** YOUR CODE HERE ***"
    d = {}
    for word in word_list:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d



## Nested List Mutation

def word_count_list(word_list):
    """ Returns a list of lists where each inner list is equal to
    [word, count].

    >>> lists = word_count_list(shakespeare_list)
    >>> lists[0]
    ['the', 51]
    >>> lists[183]
    ['but', 12]
    >>> lists[78]
    ['thy', 5]
    """
    "*** YOUR CODE HERE ***"
    lists = []
    for word in word_list:
        for lst in lists:
            if lst[0] == word:
                lst[1] += 1
                break
        else:
            lists += [[word, 1]]
    return lists



## List/Tuple Mutation 

def word_count_tuple(word_list):
    """ Returns a list of tuples where each tuple is equal to
    (word, count).

    >>> tuples = word_count_tuple(shakespeare_list)
    >>> tuples[0]
    ('the', 51)
    >>> tuples[183]
    ('but', 12)
    >>> tuples[78]
    ('thy', 5)
    """
    "*** YOUR CODE HERE ***"
    tuples = []
    for word in word_list:
        for i in range(len(tuples)):
            if tuples[i][0] == word:
                tuples[i] = (word, tuples[i][1] + 1)
                break
        else:
            tuples += [(word, 1)]
    return tuples



## get_word_count

def get_word_count(lists, word):
    """ Given a list of tuples or lists (such as those returned by
    word_count_tuple and word_count_list), returns the count of a word.

    >>> lists = word_count_list(shakespeare_list)
    >>> get_word_count(lists, "the")
    51
    >>> tuples = word_count_tuple(shakespeare_list)
    >>> get_word_count(tuples, "the")
    51
    """
    "*** YOUR CODE HERE ***"
    for elem in lists:
        if elem[0] == word:
            return elem[1]



## Mutating function

import string

def word_count_fun(word_list):
    """ Returns a list of lists where each inner list is equal to
    [word, count].

    >>> word_count_fun(["one", "two", "two"])
    [['one', 1], ['two', 2]]
    """
    lists = []
    def add_word(word):
        "*** YOUR CODE HERE ***"
        nonlocal lists
        for lst in lists:
            if lst[0] == word:
                lst[1] += 1
                return
        lists += [[word, 1]]
        return 
    for word in word_list:
        add_word(word)
    return lists

