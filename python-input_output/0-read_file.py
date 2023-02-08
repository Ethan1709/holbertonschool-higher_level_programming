#!/usr/bin/python3
""" read """


def read_file(filename=""):
    """ read """
    with open(filename, encoding="utf-8") as f:
        if filename == "":
            pass
        print (f.read()[:-1])
