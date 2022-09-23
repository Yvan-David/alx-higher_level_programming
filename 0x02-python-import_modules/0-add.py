#!/usr/bin/python3
if __name__ == '__main__':
    from add_0 import add as c
    a = 1
    b = 2
    #print(c(a,b))
    if  (type(a)) == int and (type(b) == int): 
        print("{} + {} = {}".format(a, b, c(a, b)))
