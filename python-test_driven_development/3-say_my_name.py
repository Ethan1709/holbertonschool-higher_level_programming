#!/usr/bin/python3
""" print name """


def say_my_name(first_name, last_name=""):
    """ print name """
    if first_name == None and last_name == None:
        raise TypeError("say_my_name() missing 2 required positional arguments:\
                'first_name' and 'last_name'")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is " + first_name + " " + last_name)
