#!/usr/bin/python3
def no_c(my_string):
<<<<<<< HEAD
    return ("".join(c for c in my_string if c not in "Cc"))
=======
    """Removes all characters c and C from a string."""
    return my_string.translate({ord(c): None for c in "cC"})
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
