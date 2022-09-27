def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = '',
    if len(tuple_a) > len(tuple_b):
        n = len(tuple_a)
    else:
        n = len(tuple_b)
    for i in range(2):
        tuple_d = str(int(tuple_a[i]) + int(tuple_b[i]))
        tuple_d[1] = '',
        tuple_c = tuple_d

    return(tuple_c)