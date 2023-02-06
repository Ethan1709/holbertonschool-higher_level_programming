#!/usr/bin/python3
<<<<<<< HEAD
""" inherit """


class MyList(list):
    """ inherit """
    def print_sorted(self):
        print(MyList)
=======
""" My list """


class MyList(list):
    """ My list """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))
>>>>>>> 61bf2fcd95ddac16bc853b27c6d1b85afdbd8fdb
