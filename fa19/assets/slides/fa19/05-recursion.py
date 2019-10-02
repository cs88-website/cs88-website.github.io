# Some handy imports, don't worry about these
# This file needs to be run locally on you machine,
# it displays graphical output.
### Docs: https://docs.python.org/3.7/library/turtle.html

# Run with python3 lecture4.py
# A new window opens, click in there once.
# Press SPACE to redraw things
# Press UP/DOWN to add or remove "VEE" from the list of functions
# Press R to clear the screen

from turtle import *
from math import sin, cos, tan, pi, sqrt
from random import choice # pick something random

#### HOFs and Recusion Vee Demo ######

def reset():
    pencolor('black')
    pensize(1)
    speed("fastest")
    setheading(90) # 90 degrees, facing "north"
    goto(0, -100)
    clear()
    penup()
    display_functions()
    goto(0, -100)
    pendown()

def triangle():
    """Draw a filled triangle with a side length of 12."""
    n = 3
    fillcolor(choice(colors))
    begin_fill()
    while n > 0:
        forward(12) # size 10
        left(120)
        n -= 1
    end_fill()

def dot():
    """Draw a filled circle with radius 6."""
    fillcolor(choice(colors))
    begin_fill()
    circle(6) # this is a built in turtle function, size 8 a little smaller
    end_fill()

def square():
    """Draw a square of length 12"""
    n = 4
    fillcolor(choice(colors))
    begin_fill()
    while n > 0:
        forward(12)
        left(90)
        n -= 1
    end_fill()

def draw_polygon(sides):
    "Return a generic draw a polygon function like the ones above"
    def draw_shape():
        n = sides
        fillcolor(choice(colors))
        begin_fill()
        while n > 0:
            forward(12)
            left(sides / 360)
            n -= 1
        end_fill()
    return draw_shape

# Some colors, `choice(colors)` returns a random color.
colors = [
    '#003262', # Hex code color "Berkeley Blue"
    '#FDB515' # Hex code for "California Gold"
]

# A list of HOFs
draw_functions = [
    triangle,
    dot,
    square
]

def vee():
    """Draw a 'v' shape, with random shapes at the end of each leg."""
    angle = 15
    size = 45
    left(angle)
    forward(size)
    shape = choice(draw_functions) # A random shape
    shape() # Call a HOF, with a size input
    backward(size)
    right(angle * 2) # turn where we strated, then to the right again.
    forward(size)
    choice(draw_functions)() # We can also stack parens together
    backward(size)
    left(angle)

def add_vee():
    if len(draw_functions) == 3:
        draw_functions.append(vee)
        draw_functions.append(vee)
    display_functions()

def remove_vee():
    if len(draw_functions) == 5:
        draw_functions.pop() # remove the last item, twice.
        draw_functions.pop()
    display_functions()

def display_functions():
    clear()
    penup()
    goto(-240, 300)
    for func in draw_functions:
        write(func, move=False, font=('Courier', 20, 'normal'))
        goto(-240, ycor() - 20)
    goto(0, -100)
    pendown()

def draw_new():
    reset()
    vee()

# simple interactivity
onkey(draw_new, 'space')
onkey(reset, 'r')
onkey(add_vee, 'Up')
onkey(remove_vee, 'Down')
listen()

### This is what does the actual work when you run the program.
# reset()
# vee()

# This runs the file when started.
if __name__ == '__main__':
    reset()
    vee()

######################## Some extra stuff for later

##### More HOFs
def vee_hof():
    """Draw a 'v' shape, with random shapes at the end of each leg."""
    angle = 15
    size = 45
    def draw_leg():
        forward(size)
        choice(draw_functions)() # Call a HOF
        backward(size)

    left(angle)
    draw_leg()
    right(angle * 2) # face the direction where we strated, then to the right.
    draw_leg()
    left(angle)
