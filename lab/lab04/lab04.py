from utils import *

# Q1
def get_seven_a(x):
    """
    >>> x = [1, 3, [5, 7], 9]
    >>> get_seven_a(x)
    7
    """
    "*** YOUR CODE HERE ***"

def get_seven_b(x):
    """
    >>> x = [[7]]
    >>> get_seven_b(x)
    7
    """
    "*** YOUR CODE HERE ***"

def get_seven_c(x):
    """
    >>> x = [1, [2, [3, [4, [5, [6, [7]]]]]]]
    >>> get_seven_c(x)
    7
    """
    "*** YOUR CODE HERE ***"

# Q3
def reverse_recursive(lst):
    """Returns the reverse of the given list.

    >>> reverse_recursive([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"


# Q4
def reverse_iter_for(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter_for([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"

def reverse_iter_while(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    """
    rev_lst, i = [], 0
    while i < len(lst):
        "*** YOUR CODE HERE ***"


# Q5
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"


# Q6
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    # recursive
    "*** YOUR CODE HERE ***"

# Iterative solution 
def merge_iter(lst1, lst2):
    """Merges two sorted lists.

    >>> merge_iter([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge_iter([], [2, 4, 6])
    [2, 4, 6]
    >>> merge_iter([1, 2, 3], [])
    [1, 2, 3]
    >>> merge_iter([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"

def merge_sort(lst):
    """Return sorted list using a merge sort.
    Split the list into two halves (i.e., lengths differ by <= 1)
    Sort each and merge.

    >>> merge_sort([1,2,3,4,5])
    [1, 2, 3, 4, 5]
    >>> merge_sort([1,4,5,2,3])
    [1, 2, 3, 4, 5]
    """
    "*** YOUR CODE HERE ***"


# Secret Codes: Q7-8

from utils import *
import string

characters = string.ascii_letters

def char_index(c):
    """Return the index of character c in the characters reference string.

    >>> char_index('a')
    0
    >>> char_index('m')
    12
    """
    "*** YOUR CODE HERE ***"

def make_coders(shift):
    """Return a encoder,decoder function pair where the encoder shifts every char by
    a specified rotation of the reference character array and the decoder shifts it back.

    >>> enc, dec = make_coders(0)
    >>> enc("Quick")
    'Quick'
    >>> dec("Quick")
    'Quick'
    >>> enc7, dec7 = make_coders(7)
    >>> enc7("Quick")
    'XBpjr'
    >>> dec7('XBpjr')
    'Quick'
    """
    def make_coder(shift):
        "*** YOUR CODE HERE ***"

    return make_coder(shift), make_coder(-shift)

def code_message(coder, message):
    """Return message coded by a coder function applied to each word.
    message: string containing words in the reference character set separated by spaces
    coder: function that take a word and returns its coded form.

    >>> enc7, dec7 = make_coders(7)
    >>> code_message(enc7, "The quick brown fox")
    'aol xBpjr iyvDu mvE'
    >>> code_message(dec7, 'aol xBpjr iyvDu mvE')
    'The quick brown fox'
    """
    "*** YOUR CODE HERE ***"


def trim_leading(text, char):
    """Return trimmed text leading instances of char removed.

    >>> trim_leading("***quick**", "*")
    'quick**'
    >>> trim_leading("    quick  ", " ")
    'quick  '
    """
    "*** YOUR CODE HERE ***"

def next_sentence(text):
    """Return a tuple of the chars up to '.' and the remainder sans '.' and leading spaces.

    >>> next_sentence("This. And that. The other thing.")
    ('This', 'And that. The other thing.')
    >>> next_sentence("And that. The other thing.")
    ('And that', 'The other thing.')
    """
    "*** YOUR CODE HERE ***"

def split_sentences(text):
    """Return a list of the sentences in text with no periods and no leading spaces.

    >>> split_sentences("This. And that. The other thing.")
    ['This', 'And that', 'The other thing']
    """
    "*** YOUR CODE HERE ***"

def concat_sentences(sentence_sequence):
    """Concatenate a list of sentences, putting in missing periods and space.

    >>> concat_sentences(['This', 'And that', 'The other thing'])
    'This. And that. The other thing.'
    """
    "*** YOUR CODE HERE ***"

def code_document(coder, document):
    """Return a coded form of document.

    >>> enc9, dec9 = make_coders(9)
    >>> code_document(enc9, 'This. And that. The other thing.')
    'cqrB. Jwm CqjC. cqn xCqnA Cqrwp.'
    >>> code_document(dec9, 'cqrB. Jwm CqjC. cqn xCqnA Cqrwp.')
    'This. And that. The other thing.'
    """
    "*** YOUR CODE HERE ***"
    coded_sentences = map(msg_coder, sentences)
    return concat_sentences(coded_sentences)


