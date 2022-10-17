#!/usr/bin/python3

<<<<<<< HEAD

def divisible_by_2(my_list=[]):
    return [(i % 2) == 0 for i in my_list]
=======
def divisible_by_2(my_list=[]):
    new_l = my_list.copy()
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new_l[i] = 1
        else:
            new_l[i] = 0
    return new_l
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
