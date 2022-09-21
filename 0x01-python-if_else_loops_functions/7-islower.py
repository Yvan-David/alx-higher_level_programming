#!/usr/bin/python3
from turtle import up


def islower(c):
    n = ord(c)
    if n in range(97, 123):
        return True
    else:
        return False
