#!/usr/bin/env python

flag = 'maintenance'

def to_bool(string):
    first = str(string).lower()[:1]
    print first
    if first in ('t', 'y', '1'):
        return True
    elif first in ('f', 'n', '0'):
        return False
    else:
        raise ValueError("Invalid value for boolean: {0}".format(string))


def to_bool_rep(value):
    """
    Transformation function for global metadata.  Serves to verify input as
    a parsable boolean representation and normalize it to 0 or 1.
    """
    return 1 if to_bool(value) else 0

global_flags = {
    'maintenance': to_bool_rep,
}

transform_fn = global_flags[flag]
transform_fn('True')

print transform_fn
print global_flags