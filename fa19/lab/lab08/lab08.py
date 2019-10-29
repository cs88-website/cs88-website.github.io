# Lambda
def compose(f, g):
    """Write a function that takes in 2 single-argument functions, f and g, and returns another lambda function 
    that takes in a single argument x. The returned function should return the output of applying f(g(x)). 
    Hint: The staff solution is only 1 line!

    Return the composition function which given x, computes f(g(x)). 

    >>> add_two = lambda x: x + 2  		# adds 2 to x
    >>> square = lambda x: x ** 2 		# squares x
    >>> a = compose(square, add_two) 	# (x + 2 ) ^ 2
    >>> a(5) 
    49
    >>> mul_ten = lambda x: x * 10 		# multiplies 10 with x
    >>> b = compose(mul_ten, a) 		# ((x + 2 ) ^ 2) * 10
    >>> b(5)
    490
    >>> b(2)
    160
    """
    "*** YOUR CODE HERE ***"
    

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
    


# Map
def map(fn, lst):
    """Maps fn onto lst using mutation.
    >>> original_list = [5, -1, 2, 0]
    >>> map(lambda x: x * x, original_list)
    >>> original_list
    [25, 1, 4, 0]
    """
    "*** YOUR CODE HERE ***"


# Reverse
def todo():
    """Returns add and reverse, which add to and reverse the list
    >>> add, get_list, reverse = todo()
    >>> add("clean")
    >>> add("homework")
    >>> add("cook")
    >>> add("sleep")
    >>> get_list()
    ['clean', 'homework', 'cook', 'sleep']
    >>> reverse()
    >>> get_list()
    ['sleep', 'cook', 'homework', 'clean']
    >>> add("wake up")
    >>> get_list()
    ['sleep', 'cook', 'homework', 'clean', 'wake up']
    >>> reverse()
    >>> get_list()
    ['wake up', 'clean', 'homework', 'cook', 'sleep']
    """
    lst = []
    def get_list():
        return lst
    def add(item):
        lst.append(item)
    def reverse():
        "*** YOUR CODE HERE ***"
        
    return add, get_list, reverse
    


# Mailbox

def mailbox():
    """
    >>> get_mail, deliver_mail = mailbox()
    >>> get_mail("Sophia")
    >>> deliver_mail("Sophia", ["postcard"])
    >>> get_mail("Sophia")
    ['postcard']
    >>> get_mail("Sophia")
    >>> deliver_mail("Lyric", ["paycheck", "ads"])
    >>> get_mail("Lyric")
    ['paycheck', 'ads']
    >>> deliver_mail("Lyric", ["bills"])
    >>> get_mail("Lyric")
    ['bills']
    >>> deliver_mail("Julia", ["survey"])
    >>> get_mail("Julia")
    ['survey']
    >>> get_mail("Julia")
    >>> get_mail("Amir")
    >>> deliver_mail("Amir", ["postcard", "paycheck"])
    >>> deliver_mail("Amir", ["ads"])
    >>> get_mail("Amir")
    ['postcard', 'paycheck', 'ads']
    """
    "*** YOUR CODE HERE ***"
    
    return get_mail, deliver_mail

def _deliver_mail(mailbox, name, mail):
    "*** YOUR CODE HERE ***"
    

def _get_mail(mailbox, name):
    "*** YOUR CODE HERE ***"
    



# Mutation Mystery
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

