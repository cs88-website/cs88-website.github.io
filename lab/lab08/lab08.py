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
    >>> get_mail("Amir")
    >>> deliver_mail("Amir", ["postcard"])
    >>> get_mail("Amir")
    ['postcard']
    >>> get_mail("Amir")
    >>> deliver_mail("Ting", ["paycheck", "ads"])
    >>> get_mail("Ting")
    ['paycheck', 'ads']
    >>> deliver_mail("Ting", ["bills"])
    >>> get_mail("Ting")
    ['bills']
    >>> deliver_mail("Alex", ["survey"])
    >>> get_mail("Alex")
    ['survey']
    >>> get_mail("Alex")
    >>> get_mail("John")
    >>> deliver_mail("John", ["postcard", "paycheck"])
    >>> deliver_mail("John", ["ads"])
    >>> get_mail("John")
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
