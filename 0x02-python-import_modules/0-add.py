#!/usr/bin/python3
if __name__ == '__main__':
    import add_0 as c
    a = 1
    b = 2
    #print(c(a,b))
    if  (type(a)) == int and (type(b) == int): 
        print(f'{a} + {b} = {c.add(a,b)}')
