# Lookup table representation
#

# Constructors

def lut():
    """Construct a lookup table."""
    return {}

def lut_add(lut, key, value):
    """Return a new lut with (key,value) binding added."""
    assert key not in lut_keys(lut), "Duplicate key in binding"
    new_lut = lut.copy()
    new_lut[key] = value
    return new_lut

def lut_del(lut, key):
    """Return a new lut with (key, *) binding removed."""
    assert key in lut_keys(lut), "Attempt to delete missing key"
    new_lut = lut.copy()
    del new_lut[key]
    return new_lut

# Selectors

def lut_get(lut, key):
    """Return the value bound to key in lut or None if binding not present."""
    return lut.get(key, None)

def lut_keys(lut):
    """Return a list of keys in lookup table lut."""
    return list(lut.keys())

def lut_values(lut):
    """Return a list of values in lookup table lut."""
    return list(lut.values())

def lut_items(lut):
    """Return a list of (key,value) items in lookup table lut."""
    return list(lut.items())

