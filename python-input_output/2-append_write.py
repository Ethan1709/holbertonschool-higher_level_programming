#!/usr/bin/python3
""" write """


def append_write(filename="", text=""):
    """ write """
    with open(filename, 'a', encoding="utf-8") as f:
        f = f.write(text)
        return f
