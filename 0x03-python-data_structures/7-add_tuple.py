#!/usr/bin/python3
<<<<<<< HEAD


def add_tuple(tuple_a=(), tuple_b=()):
    tup1 = tuple_a + (0, 0)
    tup2 = tuple_b + (0, 0)
    result = (tup1[0] + tup2[0], tup1[1] + tup2[1])
    return (result)
=======
def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds two tuples."""

    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
