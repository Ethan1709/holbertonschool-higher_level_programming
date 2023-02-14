#!/usr/bin/python3
""" Base class """
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ dict to json string """
        if list_dictionaries is None or list_dictionaries == "":
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        l = []
        if list_objs:
            [l.append(v.to_dictionary()) for v in list_objs]

        with open("%s.json" % (cls.__name__), 'w') as f:
            f.write(cls.to_json_string(l))
    
    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return json.loads([])
        return json.loads(json_string)
