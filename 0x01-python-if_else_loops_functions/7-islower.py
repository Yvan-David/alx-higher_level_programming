#!/usr/bin/python3
def islower(c):
    if c + 'a' is True:
        n = ord(c)
        if n in range(97, 123):
            return True
        else:
            return False
    else:
        return False
