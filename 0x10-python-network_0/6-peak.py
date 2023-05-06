#!/usr/bin/python3
""" function that finds the peak """

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    c = None
    statu = 0
    status = 0
    stat = 0
    top = list_of_integers[0]
    last = list_of_integers[len(list_of_integers) - 1]
    for i in list_of_integers:
        if top > i:
            statu = 1
        elif top < i:
            statu = 0
        if last > i:
            stat = 1
        elif last < i:
            stat = 0
        if (i + 2) <= len(list_of_integers):
            if list_of_integers[i] < list_of_integers[i + 1] and list_of_integers[i + 1] > list_of_integers[2]:
                status = 1
                c = list_of_integers[i + 1]
    if stat and statu and status:
        return (c)
    elif stat and not statu and not status:
        return (last)
    elif statu and not stat and not status:
        return (top)
    elif status:
        return (c)
    else:
        return (list_of_integers[0])
