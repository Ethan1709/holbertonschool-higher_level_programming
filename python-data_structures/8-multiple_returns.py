#!/usr/bin/python3


def multiple_returns(sentence):
    i = 0
    for i in range(len(sentence)):
        i += 1
    if i == 0:
        return (0, None)
    return (i, sentence[0])
