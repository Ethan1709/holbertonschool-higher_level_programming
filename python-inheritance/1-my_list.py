#!/usr/bin/python3
""" My list """


class MyList(list):
    """ My list """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))