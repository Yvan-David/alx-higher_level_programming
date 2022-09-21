#!/usr/bin/python3
def uppercase(str):
    st = ''
    for i in range(0, len(str)):
        b = ord(str[i])
        if b in range(97, 123):
            b = b - 32
        st = st + chr(b)
    print(st)
