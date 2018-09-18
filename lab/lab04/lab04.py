# Question 1

<question This Question is so Derivative>

Define a function `make_derivative` that returns a function: the derivative of a
function `f`. Assuming that `f` is a single-variable mathematical function, its
derivative will also be a single-variable function. When called with a number
`a`, the derivative will estimate the slope of `f` at point `(a, f(a))`.

Recall that the formula for finding the derivative of `f` at point `a` is:

![Derivative](assets/derivative.png)

where `h` approaches 0. We will approximate the derivative by choosing a very
small value for `h`. The closer `h` is to 0, the better the estimate of the
derivative will be.

<solution>
    def make_derivative(f, h=1e-5):
        """Returns a function that approximates the derivative of f.

        Recall that f'(a) = (f(a + h) - f(a)) / h as h approaches 0. We will
        approximate the derivative by choosing a very small value for h.

        >>> square = lambda x: x*x
        >>> derivative = make_derivative(square)
        >>> result = derivative(3)
        >>> round(result, 3) # approximately 2*3
        6.0
        """
        "*** YOUR CODE HERE ***"
        return _____

</solution>

<p>Use OK to test your code:</p><pre><code>python3 ok -q make_derivative --local</code></pre>


# Question 2

<question Intersect>

Two functions intersect at an argument `x` if they return equal values.
Implement `intersects`, which takes a one-argument functions `f` and a value
`x`. It returns a function that takes another function `g` and returns whether
`f` and `g` intersect at `x`.

<solution>
    def intersects(f, x):
        """Returns a function that returns whether f intersects g at x.

        >>> at_three = intersects(square, 3)
        >>> at_three(triple) # triple(3) == square(3)
        True
        >>> at_three(increment)
        False
        >>> at_one = intersects(identity, 1)
        >>> at_one(square)
        True
        >>> at_one(triple)
        False
        """
        "*** YOUR CODE HERE ***"
        return _____

</solution>

<p>Use OK to test your code:</p><pre><code>python3 ok -q intersects --local</code></pre>


# Question 3

<question Piecewise>

Implement `piecewise`, which takes two one-argument functions, `f` and `g`,
along with a number `b`. It returns a new function that takes a number `x` and
returns either `f(x)` if `x` is less than `b`, or `g(x)` if `x` is greater than
or equal to `b`.

<solution>
    def piecewise(f, g, b):
        """Returns the piecewise function h where:

        h(x) = f(x) if x < b,
               g(x) otherwise

        >>> def negate(x):
        ...     return -x
        >>> abs_value = piecewise(negate, identity, 0)
        >>> abs_value(6)
        6
        >>> abs_value(-1)
        1
        """
        "*** YOUR CODE HERE ***"
        return _____

</solution>

<p>Use OK to test your code:</p><pre><code>python3 ok -q piecewise --local</code></pre>


# Question 4

<question Converter>
Given a list of temperatures in Celsius format, convert each temperature value in a list from Celsius to Fahrenheit.

A couple tips:
- Make sure to use the `map` keyword for this solution!
- The temperature converter function will be passed in as a method, so there is no need for you to write it again!

If you're feeling stuck, think about the parameters of `map`. This is meant to be a simple problem that provides hands-on experience of understanding what `map` does.

<solution>
    def converter(temperatures, convert):
        """Returns a function that converts each Celsius temperature to Fahrenheit

        >>> convert = lambda x: 9.0*x/5.0 + 32
        >>> temperatures = [10, 20, 30, 40, 50]
        >>> converter(temperatures, convert)
        [50.0, 68.0, 86.0, 104.0, 122.0]
        """
        "*** YOUR CODE HERE ***"
        return _____

</solution>

<p>Use OK to test your code:</p><pre><code>python3 ok -q converter --local</code></pre>


# Question 5

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    "*** YOUR CODE HERE ***"
    return _____

