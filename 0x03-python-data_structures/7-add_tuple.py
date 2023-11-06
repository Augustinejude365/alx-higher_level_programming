#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    element_1 = tuple_a[0] + tuple_b[0] if len(tuple_a) >= 1 and
len(tuple_b) >= 1 else 0
    element_2 = tuple_a[1] + tuple_b[1] if len(tuple_a) >= 2 and
len(tuple_b) >= 2 else 0
    new_tuple = (element_1, element_2)
    return new_tuple
