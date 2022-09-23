#!/usr/bin/python3
if __name__ == '__main__':
    import add_0
    a = 1
    b = 2
    #print(c(a,b))
    if  (type(a)) == int and (type(b) == int): 
        print("{} + {} = {}".format(a, b, add_0.add(a, b)))
