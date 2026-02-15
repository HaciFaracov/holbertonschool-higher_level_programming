#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by adding (0, 0)
    # and then taking only the first two elements.
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Perform the addition
    res_1 = a[0] + b[0]
    res_2 = a[1] + b[1]

    return (res_1, res_2)
