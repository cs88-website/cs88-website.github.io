################
#### Person ####
################

class Person(object):
    """Person class.

    >>> steven = Person("Steven")
    >>> steven.say("Hello")
    'Hello'
    >>> steven.repeat()
    'Hello'
    >>> steven.greet()
    'Hello, my name is Steven'
    >>> steven.repeat()
    'Hello, my name is Steven'
    >>> steven.ask("preserve abstraction barriers")
    'Would you please preserve abstraction barriers'
    >>> steven.repeat()
    'Would you please preserve abstraction barriers'
    """
    def __init__(self, name):
        self.name = name
        "*** YOUR CODE HERE ***"

    def say(self, stuff):
        "*** YOUR CODE HERE ***"
        return stuff

    def ask(self, stuff):
        return self.say("Would you please " + stuff)

    def greet(self):
        return self.say("Hello, my name is " + self.name)

    def repeat(self):
        "*** YOUR CODE HERE ***"


##############
#### Errors ####  
##############

class Error:
    """
    >>> err1 = Error(12, "error.py")
    >>> err1.write()
    Traceback (most recent call last):
        error.py line 12

    """
    def __init__(self, line, file):
        "*** YOUR CODE HERE ***"

    def write(self):
        trace = 'Traceback (most recent call last):\n '
        print(trace + '   ' + self.file + ' line ' + str(self.line))

class SyntaxError(Error):
    """
    >>> err1 = SyntaxError(17, "HW10.py")
    >>> err1.write()
    Traceback (most recent call last):
        HW10.py line 17
        SyntaxError : Invalid syntax
    >>> err1.add_code(4, "EOL while scanning string literal")
    >>> err2 = SyntaxError(18, "HW10.py", 4)
    >>> err2.write()
    Traceback (most recent call last):
        HW10.py line 18
        SyntaxError : EOL while scanning string literal

    """
    type = 'SyntaxError'
    msgs = {0 : "Invalid syntax", 1: "Unmatched parentheses", 2: "Incorrect indentation", 3: "missing colon"}

    def __init__(self, line, file, code=0):
        "*** YOUR CODE HERE ***"

    def write(self):
        "*** YOUR CODE HERE ***"
        print('    ' + self.type + ' : ' + self.message)

    def add_code(self, code, msg):
        "*** YOUR CODE HERE ***"

class ZeroDivisionError(Error):
    """
    >>> err1 = ZeroDivisionError(273, "HW10.py")
    >>> err1.write()
    Traceback (most recent call last):
        HW10.py line 273
        ZeroDivisionError : division by zero
    """
    type = 'ZeroDivisionError'

    def __init__(self, line, file, message='division by zero'):
        "*** YOUR CODE HERE ***"

    def write(self):
        "*** YOUR CODE HERE ***"
        print('    ' + self.type + ' : ' + self.message)

