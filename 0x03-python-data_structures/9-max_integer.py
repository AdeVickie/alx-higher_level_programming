#!/usr/bin/python3
def max_integer(my_list=[]):
<<<<<<< HEAD
    if len(my_list) == 0:
        return None
    maxm = my_list[0]
    for num in my_list:
        if maxm < num:
            maxm = num
    return maxm
=======
    """Finds the biggest integer of a list."""

    if not my_list:
        return None

    max_i = my_list[0]
    for i in my_list:
        if i > max_i:
            max_i = i
    return max_i
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
