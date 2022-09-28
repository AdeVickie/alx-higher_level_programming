#!/usr/bin/python3
def multiple_returns(sentence):
<<<<<<< HEAD
    if len(sentence) == 0:
        return len(sentence), None
    for i in sentence:
        return (len(sentence), i)
=======
    """Returns a tuple with the length of a string and its first character.
    """

    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
>>>>>>> af1b35f3e5ccd023f3f80dfa47c204b3d082c22a
