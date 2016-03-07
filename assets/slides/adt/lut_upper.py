from lut_tuples import *

def lut_update(lut, key, value):
    """Return a new lut with new or updated key=>value binding."""
    if lut[key] is None:
        return lut_add(lut, key, value)
    else:
        return lut_add(lut_del(lut, key), value)




