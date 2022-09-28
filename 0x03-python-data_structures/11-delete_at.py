#!/usr/bin/python3

<<<<<<< HEAD

def delete_at(my_list=[], idx=0):
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
=======
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
