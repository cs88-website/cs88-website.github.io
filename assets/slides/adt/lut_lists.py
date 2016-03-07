# Lookup table representation
#

# Constructors

def lut():
    """Construct a lookup table."""
    return ([], [])

def lut_add(lut, key, value):
    """Return a new lut with (key,value) binding added."""
    assert key not in lut_keys(lut), "Duplicate key in binding"
    return ([key] + lut_keys(lut), [value] + lut_values(lut))

def lut_del(lut, key):
    """Return a new lut with (key, *) binding removed."""
    assert key in lut_keys(lut), "Attempt to delete missing key"
    keys, values = lut
    key_index = keys.index(key)
    return (keys[0:key_index] + keys[key_index+1:], values[0:key_index] + values[key_index+1:])

# Selectors

def lut_get(lut, key):
    """Return the value bound to key in lut or None if binding not present."""
    for k,val in zip(lut[0],lut[1]):
        if k == key:
            return val
    return None

def lut_keys(lut):
    """Return a list of keys in lookup table lut."""
    return lut[0]

def lut_values(lut):
    """Return a list of values in lookup table lut."""
    return lut[1]

def lut_items(lut):
    """Return a list of (key,value) items in lookup table lut."""
    return list(zip(lut[0],lut[1]))




