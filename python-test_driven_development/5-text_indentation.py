#!/usr/bin/python3
""" text indentation """


def text_indentation(text):
    """ text indentation """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        i = 0
        for k in text:
            if i == 0:
                if k == " ":
                    continue
                else:
                    i = 1
            if i == 1:
                if k == '.' or k == '?' or k == ':':
                    print(k + '\n')
                    i = 0
                else:
                    print(k, end="")
