#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    return {key: value for key, value in obj.__dict__.items() if\
            isinstance(value, (list, dict, str, int, bool))}
