#!/usr/bin/python3
"""
a module for MYlist
"""


class MyList(list):
    """
    a class for mylist
    """
    def print_sorted(self):
        """
    a function for printing sorted mylist
    """
        n = self.copy()
        n.sort()
        return (n)
