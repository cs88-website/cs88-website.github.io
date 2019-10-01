# HW05 Utilities

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

def lambda_curry2(func):
    """
    Returns a Curried version of a two argument function func.
    >>> from operator import add
    >>> x = lambda_curry2(add)
    >>> y = x(3)
    >>> y(5)
    8
    """
    "*** YOUR CODE HERE ***"
    


from operator import add, sub

def caesar_generator(num, op):
    """Returns a one-argument Caesar cipher function. The function should "rotate" a
    letter by an integer amount 'num' using an operation 'op' (either add or
    sub).

    You may use the provided `letter_to_num` and `num_to_letter` functions,
    which will map all lowercase letters a-z to 0-25 and all uppercase letters
    A-Z to 26-51.

    >>> letter_to_num('a')
    0
    >>> letter_to_num('c')
    2
    >>> num_to_letter(3)
    'd'

    >>> caesar2 = caesar_generator(2, add)
    >>> caesar2('a')
    'c'
    >>> brutus3 = caesar_generator(3, sub)
    >>> brutus3('d')
    'a'
    """
    "*** YOUR CODE HERE ***"
    


def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: _____
    while x > 0:
        x, y = _____, f()
    return y == n


def polynomial(degree, coeffs):
    """
    >>> fourth = polynomial(4, [3,6,2,1, 100])
    >>> fourth(3)   # 3*(3**4) + 6*(3**3) + 2*(3**2) + 1*(3**1) + 100
    526
    >>> third = polynomial(3, [2, 0, 0, 0])
    >>> third(4)   # 2*(4**3) + 0*(4**2) + 0*(4**1) + 0
    128
    """
    "*** YOUR CODE HERE ***"
    

