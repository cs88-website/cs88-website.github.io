import string
from collections import OrderedDict
#
# Utility functions
#
def lowercase(s):
    """Return string s converted all to lowercase.

    >>> lowercase("Hello")
    'hello'
    """
    ls = ""
    for c in s:
        if c in string.ascii_uppercase:
            ls = ls + string.ascii_lowercase[string.ascii_uppercase.index(c)]
        else:
            ls = ls + c
    return ls

def key_of_max(d):
    """Return key associated with maximum value in d.

    >>> key_of_max({'a':1, 'b':2})
    'b'
    """
    max_key, max_val = None, None
    for k,v in d.items():
        if max_val is None or v > max_val:
            max_key, max_val = k,v
    return max_key


