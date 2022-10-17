#!/usr/bin/python3

<<<<<<< HEAD

def element_at(my_list, idx):
    if (idx < 0 or idx >= len(my_list)):
        return (None)
    return (my_list[idx])
=======
# that retrieves an element from a list like in C.

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return
    return my_list[idx]
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
