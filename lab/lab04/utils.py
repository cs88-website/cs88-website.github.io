def first(s):
    return s[0]

def rest(s):
    return s[1:]

def last(s):
    return s[-1]

def index(s, value):
    """Return the index of value in sequence s, None if not present"""
    for i,element in zip(range(len(s)),s):
        if element == value:
            return i

def map(f, s):
    return [f(x) for x in s]

