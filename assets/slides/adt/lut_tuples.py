# Lookup table representation
#

# Constructors

def lut():
    """Construct a lookup table."""
    return []

def lut_add(lut, key, value):
    """Return a new lut with (key,value) binding added."""
    assert key not in lut_keys(lut), "Duplicate key in binding"
    return [(key, value)] + lut

def lut_del(lut, key):
    """Return a new lut with (key, *) binding removed."""
    assert key in lut_keys(lut), "Attempt to delete missing key"
    return [(k, v) for k,v in lut if k != key]

# Selectors

def lut_get(lut, key):
    """Return the value bound to key in lut or None if binding not present."""
    for k,val in lut:
        if k == key:
            return val
    return None

def lut_keys(lut):
    """Return a list of keys in lookup table lut."""
    return map(lambda x:x[0], lut)

def lut_values(lut):
    """Return a list of values in lookup table lut."""
    return map(lambda x:x[1], lut)

def lut_items(lut):
    """Return a list of (key,value) items in lookup table lut."""
    return lut


