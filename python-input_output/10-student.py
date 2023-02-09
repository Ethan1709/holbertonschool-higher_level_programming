#!/usr/bin/python3
""" class student """


class Student:
    """ class student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return vars(self)
        else:
            return {k: v for k, v in vars(self).items() if k in attrs}
