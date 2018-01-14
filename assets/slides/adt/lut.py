"""
Lookup Table Abstract Data Type

    Unordered collection of unique key => value bindings

Constructors:

    lut() - Return an empty lut
    lut_add(lut, key, value) - Return a lut with new key => value binding
    lut_del(lut, key) - Return a lut without a binding for key

Selectors:

    lut_get(lut, key) - Return value in lut bound to key or None if none exists.
    lut_keys(lut) - Return a list of keys for bindings in lut
    lut_values(lut) - Return a list of values for bindings in lut
    lut_items(lut) - Return a list of (key, value) for bindings in lut

Operations:

    lut_with_bindings(bindings) - Return a lut containing k => v for (k, v) in bindings
    lut_len(lut) - Return the number of bindings in lut.
    lut_print(lut) - Print a representaion of bindings in lut.
    lut_map_values(lit, fun) - Return a lut of bindings (k, fun(v)) for k => v bindings in lut_to_map.
    lut_sorted(lut, fun) - Return a list of (k,v) for bindings in lut sorted by <= over fun(k, v).

    lut_update(lut, key, value) - Return a new lut with new or updated key=>value binding.
    lut_fuzzy_get(lut, fuzz_key, dist_fun) - Return (key, value) for the key closest to fuzz_key under dist_fun.

"""
#from lut_tuples import *    # ADT representation
from lut_lists import *    # ADT representation
#from lut_dict import *    # ADT representation

from mersort import msort

def lut_with_bindings(bindings):
    """Construct a lookup table initialized with (key,val) bindings."""
    new_lut = lut()
    for k,v in bindings:
        new_lut = lut_add(new_lut, k, v)
    return new_lut

def lut_sorted(lut, fun):
    """Return a list of (k,v) for bindings in lut sorted by <= over fun(k, v)."""
    return msort(lut_items(lut), lambda b: fun(b[0],b[1]))

def lut_print(lut):
    """Print a representaion of bindings in lut."""
    for k,v in lut_sorted(lut, lambda k,v:k):
        print(k,"=>",v)

def lut_map_values(lut_to_map, fun):
    """Return a lut of bindings (k, fun(v)) for k => v bindings in lut_to_map."""
    return lut_with_bindings([(k,fun(v)) for k,v in lut_items(lut_to_map)])

def lut_len(lut):
    """Return a count of the number of bindings in lut."""
    return len(lut_items(lut))

def lut_update(lut, key, value):
    """Return a new lut with new or updated key=>value binding."""
    if lut_get(lut, key) is None:
        return lut_add(lut, key, value)
    else:
        return lut_add(lut_del(lut, key), key, value)

def lut_fuzzy_get(lut, fuzz_key, dist_fun):
    """Return (key, value) for the key of most like fuzz_key under dist_fun."""
    min_dist, min_key, min_val = None, None, None
    for k,v in lut_items(lut):
        dist = dist_fun(fuzz_key, k)
        if min_dist is None or dist < min_dist:
            min_dist, min_key, min_val = dist, k, v
    return (min_key, min_val)





