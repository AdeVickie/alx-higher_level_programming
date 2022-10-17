#!/usr/bin/python3


def new_in_list(my_list, idx, element):
<<<<<<< HEAD
    my_list_cpy = my_list[:]
    if (idx < 0 or idx >= len(my_list)):
        return (my_list_cpy)
    my_list_cpy[idx] = element
    return (my_list_cpy)
=======
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
