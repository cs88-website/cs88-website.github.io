"""
Lecture 4 Python Interpreter Script.

As presented in lecture, with some mistakes cleaned up. :)
"""

from itertools import reduce

def summation(n, func): # Sum from 1 to N.
    total = 0
    for i in range(1, n + 1):
        total = total + func(i)
    return total

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n, cube)

sum_cubes(3)

#### Lambdas

inc_maker(4)
# OUTPUT: <function inc_maker.<locals>.<lambda> at 0x102ef6c20>
func_a = inc_maker(4)
func_a(4)
# OUTPUT:  8
inc_maker(1)(2)
# OUTPUT: 3
school = 'The University of California at Berkeley'
len(school)
# OUTPUT:  40

school
# OUTPUT: 'The University of California at Berkeley'
words = school.split(' ')
# OUTPUT:  ['The', 'University', 'of', 'California', 'at', 'Berkeley']
[ word for word in words if len(word) > 3 ]
# OUTPUT:  ['University', 'California', 'Berkeley']
filter
# Filter is a function that takes a function and a list
# OUTPUT: <class 'filter'>
filter(lambda x: len(x) > 3, words)
# <filter object at 0x101c4cd50>
# Filter outputs a "filter object", to see the values we turn them into a list.
list(filter(lambda x: len(x) > 3, words))
# OUTPUT:  ['University', 'California', 'Berkeley']
long_word = lambda w: len(w) > 3
list(filter(long_word, words))
# OUTPUT: ['University', 'California', 'Berkeley']

# We can name our lambdas
first_letter = lambda s: s[0]
'Hello, there'[0]
# OUTPUT:  'H'
f = filter(long_word, words)
f
# OUTPUT: <filter object at 0x101c4cc90>

map
# Map is a lot like a list comprehension, and it takes a function and a list as input.
map(first_letter, f)
# OUTPUT: <map object at 0x102efda50>
list(map(first_letter, f))
# OUTPUT: ['U', 'C', 'B']

reduce
# OUTPUT:  <built-in function reduce>
def add(x, y):
    return x + y

add(1, 2)
# OUTPUT: 3
reduce(add, [1, 2, 3, 4])
# OUTPUT: 10
'U' + 'C'
# OUTPUT:  'UC'
letters = map(first_letter, filter(long_word, words))
list(letters)
# OUTPUT:  ['U', 'C', 'B']
# NOTE: this "executes" the map, meaning that if we call it again, list is empty.

letters = map(first_letter, filter(long_word, words))
reduce(lambda x, y : x + y, letters)
# OUTPUT:  'UCB'

# Let's put it all together!
def acronym(text):
    words = text.split(' ')
    return reduce( lambda x, y: x + y, map(first_letter, filter(long_word, words)))

acronym(school)

# OUTPUT:  'UCB'
reduce( lambda x, y: x+y, map(first_letter, filter(long_word, text.split(' '))))

# Q&A Time!
# Why do we need filter?
# What's the difference between filter an map?
# map returns a list of exactly the same length AND modifies the items
# filter can shorten a list, but not chage the items.
reduce( lambda x, y: x+y, map(first_letter,  school.split(' ')))
# OUTPUT: 'TUoCaB'
words
# OUTPUT: ['The', 'University', 'of', 'California', 'at', 'Berkeley']

def first_letter_if_long(w):
    if len(w) > 3:
        return first_letter(w)
    else:
        return False

first_letter_if_long('Hello')
# OUTPUT: 'H'
first_letter_if_long('at')
# OUTPUT: False
words
# OUTPUT: ['The', 'University', 'of', 'California', 'at', 'Berkeley']
map(first_letter_if_long, words)
# OUTPUT: <map object at 0x102f02c90>
list(map(first_letter_if_long, words))
# OUTPUT: [False, 'U', False, 'C', False, 'B']
list(filter(first_letter_if_long, words))
[# OUTPUT: 'University', 'California', 'Berkeley']

# What's different from list comprehensions?
# A: Not much, just different sytnax. map/filter/reduce support lambda more easily.
[ word for word in words if len(word) > 3 ]
# OUTPUT: ['University', 'California', 'Berkeley']
[ first_letter(word) for word in words if len(word) > 3 ]
# OUTPUT: ['U', 'C', 'B']
# What if we define a lambda inline?
# It works, but we need to then _call_ it.
[ lambda w: w[0] for word in words if len(word) > 3 ]
# OUTPUT: [<function <listcomp>.<lambda> at 0x102f089e0>, <function <listcomp>.<lambda> at 0x102f08a70>, <function <listcomp>.<lambda> at 0x102f08b00>]

# Calling a lambda defined inline works, but is funny looking.
[ (lambda w: w[0])(word) for word in words if len(word) > 3 ]
# OUTPUT:  ['U', 'C', 'B']
