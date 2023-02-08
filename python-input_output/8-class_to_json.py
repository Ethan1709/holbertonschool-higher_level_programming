#!/usr/bin/python3
""" class to json """


def class_to_json(obj):
    """ class to json """
    data = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value
        else:
            raise TypeError("Attribute {} is not serializable".format(attr))

    return data
