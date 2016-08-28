# Lab02 Utilities

UPPERCASE_SHIFT = 65
LOWERCASE_SHIFT = 97
ALPHA_SHIFT = 26

def letter_to_num(letter):
    """Converts all letters to numbers 0-51, with lowercase letters mapped to
    0-25 and uppercase letters mapped to 26-51
    >>> letter_to_num('a')
    0
    >>> letter_to_num('z')
    25
    >>> letter_to_num('A')
    26
    >>> letter_to_num('Z')
    51
    """
    if letter.isupper():
        return ord(letter)-UPPERCASE_SHIFT + ALPHA_SHIFT
    return ord(letter)-LOWERCASE_SHIFT

def num_to_letter(num):
    """Coverts a number 0-51 to a letter
    >>> num_to_letter(0)
    'a'
    >>> num_to_letter(25)
    'z'
    >>> num_to_letter(26)
    'A'
    >>> num_to_letter(51)
    'Z'
    """
    try:
        num = int(num)
    except ValueError:
        return ' '
    num = num % 52
    if num > 25:
        return chr(num - ALPHA_SHIFT + UPPERCASE_SHIFT)
    return chr(num + LOWERCASE_SHIFT)

def mirror_letter(letter):
    """ Returns the letter in the same position on the other 
    side of the alphabet. 

    >>> mirror_letter('a')
    'z'
    >>> mirror_letter('z')
    'a'
    >>> mirror_letter('B')
    'Y'
    >>> mirror_letter('C')
    'X'
    """
    if letter.isupper():
        return chr(155 - ord(letter))
    return chr(219 - ord(letter))


def looper(f, delimiter=''):
    """Returns a function that applies function f to every element of an iterable."""
    return lambda iterable: delimiter.join([str(f(i)) for i in iterable])
