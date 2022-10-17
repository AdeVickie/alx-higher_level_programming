#!/usr/bin/python3
<<<<<<< HEAD
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
=======

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
