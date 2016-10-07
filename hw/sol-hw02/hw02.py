# Question 2

def sum_of_squares(n):
    """
    return the sum of squares from 1 to n
    >>> sum_of_squares(3)
    14
    """
    psum = 0
    for x in range(1,n+1):
        psum += x*x
    return psum



# Question 3

def factors(n):
    """Prints out all of the numbers that divide `n` evenly.

    >>> factors(20)
    20
    10
    5
    4
    2
    1
    """
    x = n
    while x > 0:
        if n % x == 0:
            print(x)
        x -= 1


# Question 4

def max_list(s):
    """Return the largest value in a sequence.  None if empty.

    >>> max_list([1,3,-1])
    3
    """
    # Hint: Is there a built-in function you can use for this?
    return max(s)

def remove_element(s, exclude):
    """Remove all entries in sequence s equal to exclude.

    >>> remove_element([1, 3, -1], 1)
    [3, -1]
    """
    result = []
    for val in s:
        if val != exclude:
            result = result + [val]
    return result

def remove_max(s):
    """Return a a list containing non-maximal elements of a sequence.

    >>> remove_max([1, 3, -1, 3])
    [1, -1]
    """
    maximum = max_list(s)
    return remove_element(s, maximum)


# Question 5

def reverse(s):
    """Return a list that is the reverse of sequence s.

    >>> reverse([1,2,3])
    [3, 2, 1]
    """
    rs = []
    for element in s:
        rs = [element] + rs
    return rs


# Question 6

def pythagorean_triple(a,b,c):
    """
    >>> pythagorean_triple(3,4,5)
    True
    >>> pythagorean_triple(3,4,6)
    False
    """
    return a*a + b*b == c*c


# Question 7

def temperature_converter(f_temp):
    """
    >>> celsius_temp1 = temperature_converter(32)
    >>> celsius_temp1
    0.0
    """
    return (f_temp - 32) * 5 / 9


# Question 8

def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    return n-1


# Questions 9, 10

from random import randint

LOWER = 1
UPPER = 10

def guess_random():
    """Guess randomly and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)   # asks the user to choose a number
    num_guesses, correct = 0, False
    while not correct:
        guess = randint(LOWER, UPPER) # randomly guess
        correct = is_correct(guess)   # ask user if guess is correct
        num_guesses = num_guesses + 1
    return num_guesses

def guess_linear():
    """Guess in increasing order and return the number of guesses."""
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    guess = LOWER
    while not is_correct(guess):
        guess += 1
        num_guesses += 1
    return num_guesses

def guess_binary():
    """Return the number of attempted guesses. Implement a faster search
    algorithm that asks the user whether a guess is less than or greater than
    the correct number.

    Hint: If you know the guess is greater than the correct number, then your
    algorithm doesn't need to try numbers that are greater than guess.
    """
    prompt_for_number(LOWER, UPPER)
    num_guesses = 1
    lower, upper = LOWER, UPPER
    guess = (lower + upper) // 2
    while not is_correct(guess):
        if is_too_high(guess):
            upper = guess - 1
        else:
            lower = guess + 1
        guess = (lower + upper) // 2
        num_guesses += 1
    return num_guesses

# Receive user input. You do not need to understand the code below this line.

def prompt_for_number(lower, upper):
    """Prompt the user for a number between lower and upper. Return None."""
    is_valid_number = False
    while not is_valid_number:
        # You don't need to understand the following two lines.
        number = input('Pick an integer between {0} and {1} (inclusive) for me to guess: '.format(lower, upper))
        number = int(number)
        if lower <= number <= upper:
            is_valid_number = True

def is_correct(guess):
    """Ask the user if a guess is correct and return whether they respond y."""
    return is_yes('Is {0} your number? [y/n] '.format(guess))

def is_too_high(guess):
    """Ask the user if a guess is too high and return whether they say yes."""
    return is_yes('Is {0} too high? [y/n] '.format(guess))

def is_yes(prompt):
    """Ask the user a yes or no question and return whether they say yes."""
    while True: # This while statement will loop until a "return" is reached.
        yes_no = input(prompt).strip()
        if yes_no == 'y':
            return True
        elif yes_no == 'n':
            return False
        print('Please type y or n and press return/enter')

