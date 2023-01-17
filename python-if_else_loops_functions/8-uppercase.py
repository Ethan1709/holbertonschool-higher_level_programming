#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= ord('A') and ord(str) <= ord('Z'):
        str = ord(str) + 0
        str = chr(str)
        print("{}".format(str))
    else:
        str = ord(str) - 32
        str = chr(str)
        print("{}".format(str))
